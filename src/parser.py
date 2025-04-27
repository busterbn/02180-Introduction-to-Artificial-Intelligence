from formula_ast import Atom, Not, And, Or, Implies, Bicond
# --- 2. Parser --------------------------------------------------------------
# Tokenizer: split input string into tokens (operators, parentheses, identifiers)

def tokenize(s):
    # normalize Unicode negation symbol to ASCII tilde
    s = s.replace('¬', '~')
    s = s.replace('∧', '&')
    s = s.replace('∨', '|')
    s = s.replace('→', '->')
    s = s.replace('↔', '<->')
    
    # Initialize token list and index
    tokens = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
            continue
        # multi-char operators
        if s.startswith('<->', i):
            tokens.append('<->'); i += 3; continue
        if s.startswith('->', i):
            tokens.append('->'); i += 2; continue
        if c in ('(', ')', '~', '&', '|'):
            tokens.append(c); i += 1; continue
        # identifier
        j = i
        while j < len(s) and (s[j].isalnum() or s[j]=='_'):
            j += 1
        tokens.append(s[i:j])
        i = j
    return tokens

# Recursive-descent parser for propositional formulas using the above token stream
def parse_formula(s):
    tokens = tokenize(s)
    pos = 0
    def peek():
        return tokens[pos] if pos < len(tokens) else None
    def consume(t=None):
        nonlocal pos
        if t and tokens[pos] != t:
            raise ValueError(f"Expected {t}, got {tokens[pos]}")
        pos += 1
        return tokens[pos-1]

    def parse_bicond():
        # Parse biconditional '<->' by first handling implications
        left = parse_implies()
        while peek() == '<->':
            consume('<->')
            right = parse_implies()
            left = Bicond(left, right)
        return left

    def parse_implies():
        # Parse right-associative implication '->'
        left = parse_or()
        while peek() == '->':
            consume('->')
            right = parse_implies()
            left = Implies(left, right)
        return left

    def parse_or():
        # Parse left-associative disjunction '|'
        left = parse_and()
        while peek() == '|':
            consume('|')
            right = parse_and()
            left = Or(left, right)
        return left

    def parse_and():
        # Parse left-associative conjunction '&'
        left = parse_not()
        while peek() == '&':
            consume('&')
            right = parse_not()
            left = And(left, right)
        return left

    def parse_not():
        # Parse negation '~' with highest precedence
        if peek() == '~':
            consume('~')
            return Not(parse_not())
        return parse_atom()

    def parse_atom():
        # Parse atomic formulas: parentheses or identifiers
        if peek() == '(':
            consume('(')
            f = parse_bicond()
            consume(')')
            return f
        name = consume()
        return Atom(name)

    root = parse_bicond()
    if pos != len(tokens):
        raise ValueError("Extra tokens after parsing: " + str(tokens[pos:]))
    return root