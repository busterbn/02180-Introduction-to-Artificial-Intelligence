# Base‐Class for all formulas
class Formula:
    pass

class Var(Formula):
    def __init__(self, name: str):
        self.name = name
    def __repr__(self):
        return self.name

class Not(Formula):
    def __init__(self, phi: Formula):
        self.phi = phi
    def __repr__(self):
        return f"¬{self.phi}"

class And(Formula):
    def __init__(self, *args: Formula):
        self.conj = list(args)
    def __repr__(self):
        return "(" + " ∧ ".join(map(str, self.conj)) + ")"

class Or(Formula):
    def __init__(self, *args: Formula):
        self.disj = list(args)
    def __repr__(self):
        return "(" + " ∨ ".join(map(str, self.disj)) + ")"

class Imp(Formula):
    def __init__(self, phi: Formula, psi: Formula):
        self.phi, self.psi = phi, psi
    def __repr__(self):
        return f"({self.phi} → {self.psi})"

class Iff(Formula):
    def __init__(self, phi: Formula, psi: Formula):
        self.phi, self.psi = phi, psi
    def __repr__(self):
        return f"({self.phi} ↔ {self.psi})"
    
if __name__ == '__main__':
    # Create example formulas
    a = Var("a")
    b = Var("b")
    not_b = Not(b)
    conj = And(a, not_b)
    disj = Or(a, b)
    implication = Imp(a, b)
    equivalence = Iff(conj, disj)
    
    # Print the results
    print("Variable a:", a)
    print("Variable b:", b)
    print("Negation (¬b):", not_b)
    print("Conjunction (a ∧ ¬b):", conj)
    print("Disjunction (a ∨ b):", disj)
    print("Implication (a → b):", implication)
    print("Biconditional ((a ∧ ¬b) ↔ (a ∨ b)):", equivalence)