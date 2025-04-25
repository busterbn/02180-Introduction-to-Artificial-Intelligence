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