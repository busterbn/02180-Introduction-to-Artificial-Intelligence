from formula_ast import Atom, Not, And, Or, Implies, Bicond
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
