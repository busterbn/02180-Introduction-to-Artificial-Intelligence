# belief_revision.py

# --- 1. Formula AST ---------------------------------------------------------
# Formula AST: classes representing propositional logic formulas as a tree structure

class Formula:
    pass

class Atom(Formula):
    # Represents a propositional variable/atom
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class Not(Formula):
    # Logical negation of a formula
    def __init__(self, f):
        self.f = f
    def __repr__(self):
        return f"¬{self.f}"

class And(Formula):
    # Logical conjunction (AND) of two subformulas
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return f"({self.left} ∧ {self.right})"

class Or(Formula):
    # Logical disjunction (OR) of two subformulas
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return f"({self.left} ∨ {self.right})"

class Implies(Formula):
    # Logical implication (IF left THEN right)
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return f"({self.left} → {self.right})"

class Bicond(Formula):
    # Logical biconditional (if and only if)
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return f"({self.left} ↔ {self.right})"


# --- 2. Parser --------------------------------------------------------------
# Tokenizer: split input string into tokens (operators, parentheses, identifiers)

def tokenize(s):
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


# --- 3. CNF conversion ------------------------------------------------------
# Eliminate biconditional by replacing (A↔B) with (A→B)∧(B→A)

def elim_bicond(f):
    if isinstance(f, Bicond):
        a, b = elim_bicond(f.left), elim_bicond(f.right)
        # (A ↔ B) ≡ (A → B) ∧ (B → A)
        return And(Implies(a, b), Implies(b, a))
    if isinstance(f, Implies):
        return Implies(elim_bicond(f.left), elim_bicond(f.right))
    if isinstance(f, And):
        return And(elim_bicond(f.left), elim_bicond(f.right))
    if isinstance(f, Or):
        return Or(elim_bicond(f.left), elim_bicond(f.right))
    if isinstance(f, Not):
        return Not(elim_bicond(f.f))
    return f  # Atom

# Eliminate implications: replace (A→B) with (¬A∨B)
def elim_imp(f):
    if isinstance(f, Implies):
        # (A → B) ≡ (¬A ∨ B)
        return Or(elim_imp(Not(f.left)), elim_imp(f.right))
    if isinstance(f, And):
        return And(elim_imp(f.left), elim_imp(f.right))
    if isinstance(f, Or):
        return Or(elim_imp(f.left), elim_imp(f.right))
    if isinstance(f, Not):
        return Not(elim_imp(f.f))
    return f

# Push negations inward to obtain negation normal form (NNF)
def push_not(f):
    if isinstance(f, Not):
        inner = f.f
        if isinstance(inner, Not):
            return push_not(inner.f)
        if isinstance(inner, And):
            return Or(push_not(Not(inner.left)), push_not(Not(inner.right)))
        if isinstance(inner, Or):
            return And(push_not(Not(inner.left)), push_not(Not(inner.right)))
        return f  # Not(Atom)
    if isinstance(f, And):
        return And(push_not(f.left), push_not(f.right))
    if isinstance(f, Or):
        return Or(push_not(f.left), push_not(f.right))
    return f  # Atom

# Distribute OR over AND to produce conjunctive normal form (CNF)
def distribute(f):
    if isinstance(f, Or):
        A, B = distribute(f.left), distribute(f.right)
        if isinstance(A, And):
            return And(distribute(Or(A.left, B)), distribute(Or(A.right, B)))
        if isinstance(B, And):
            return And(distribute(Or(A, B.left)), distribute(Or(A, B.right)))
        return Or(A, B)
    if isinstance(f, And):
        return And(distribute(f.left), distribute(f.right))
    return f

# Convert a formula AST into a list of CNF clauses (frozensets of literals)
def to_cnf(formula):
    f1 = elim_bicond(formula)
    f2 = elim_imp(f1)
    f3 = push_not(f2)
    f4 = distribute(f3)
    # now f4 is a ∧ of ∨s; extract clauses
    clauses = []
    def collect(f):
        if isinstance(f, And):
            collect(f.left); collect(f.right)
        else:
            clauses.append(extract_clause(f))
    def extract_clause(g):
        lits = set()
        def go(x):
            if isinstance(x, Or):
                go(x.left); go(x.right)
            elif isinstance(x, Not) and isinstance(x.f, Atom):
                lits.add(f"-{x.f.name}")
            elif isinstance(x, Atom):
                lits.add(x.name)
            else:
                raise ValueError("Unexpected in clause: " + repr(x))
        go(g)
        return frozenset(lits)
    collect(f4)
    return clauses


# --- 4. Resolution ----------------------------------------------------------
# Standard resolution algorithm for propositional entailment (KB ⊨ α)

def pl_resolution(kb_clauses, alpha):
    # Check KB ⊨ alpha by seeing if KB ∪ {¬alpha} is unsatisfiable
    clauses = set(kb_clauses)
    neg_alpha = to_cnf(Not(alpha))
    clauses |= set(neg_alpha)
    new = set()
    while True:
        pairs = [(c1, c2) for c1 in clauses for c2 in clauses if c1 != c2]
        for (c1, c2) in pairs:
            for lit in c1:
                comp = ("-" + lit if not lit.startswith("-") else lit[1:])
                if comp in c2:
                    resolvent = (c1 | c2) - {lit, comp}
                    if not resolvent:
                        return True
                    new.add(frozenset(resolvent))
        if new.issubset(clauses):
            return False
        clauses |= new


# --- 5. Belief base ---------------------------------------------------------
# BeliefBase supports expansion, contraction, and AGM revision

class Belief:
    def __init__(self, formula, priority):
        self.f = formula
        self.p = priority
    def __repr__(self):
        return f"[{self.p}] {self.f}"

class BeliefBase:
    # AGM expansion: add new belief without checking consistency
    def __init__(self):
        self.beliefs = []  # list of Belief

    # AGM expansion: add new belief without checking consistency
    def expand(self, formula, priority=0):
        """Just add a new belief."""
        self.beliefs.append(Belief(formula, priority))

    # AGM contraction: remove lowest-priority beliefs until formula is no longer entailed
    def contract(self, formula):
        """
        Priority‐based contraction: remove low‐priority beliefs
        until formula is no longer entailed.
        """
        # if not entailed, nothing to do
        if not self.entails(formula):
            return
        # sort beliefs ascending by priority
        for b in sorted(self.beliefs, key=lambda B: B.p):
            # try removing b
            trial = [x for x in self.beliefs if x is not b]
            if not BeliefBase._entails_list(trial, formula):
                # removing b makes formula no longer entailed: keep it removed
                self.beliefs = trial
                return self.contract(formula)  # might need to remove more
        # if we get here, we couldn't unknot entailment
        # leaving base empty
        self.beliefs = []

    # AGM revision (Levi identity): contract ¬formula then expand formula
    def revise(self, formula, priority=0):
        """AGM revision: contract ¬formula, then expand."""
        self.contract(Not(formula))
        self.expand(formula, priority)

    def entails(self, formula):
        return BeliefBase._entails_list(self.beliefs, formula)

    @staticmethod
    def _entails_list(beliefs, formula):
        clauses = []
        for b in beliefs:
            clauses.extend(to_cnf(b.f))
        return pl_resolution(clauses, formula)

    def __repr__(self):
        return "\n".join(repr(b) for b in sorted(self.beliefs, key=lambda B: -B.p))


# --- 6. Example usage ------------------------------------------------------

if __name__ == "__main__":
    bb = BeliefBase()
    # B0: A ∧ B  (prio 1), C → A (prio 2)
    bb.expand(parse_formula("A & B"), priority=1)
    bb.expand(parse_formula("C -> A"), priority=2)
    print("Base:")
    print(bb, "\n")

    # Check entailment: Does the base entail A?
    print("Entails A?", bb.entails(parse_formula("A")))

    # Revise by ¬B (prio 3)
    bb.revise(parse_formula("~B"), priority=3)
    print("\nAfter revising with ¬B:")
    print(bb)