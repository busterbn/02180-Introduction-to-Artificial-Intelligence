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
    # 1) Opret nogle atomare variable
    A = Var("A")
    B = Var("B")
    C = Var("C")
    D = Var("D")

    # 2) Byg en sammensat formel: (A ∧ ¬B) → (C ∨ D)
    phi  = And(A, Not(B))
    psi  = Or(C, D)
    f1   = Imp(phi, psi)

    print("Formel f1:", f1)
    # Output: Formel f1: ((A ∧ ¬B) → (C ∨ D))

    # 3) Byg en bikonditional: A ↔ B
    f2 = Iff(A, B)
    print("Formel f2:", f2)
    # Output: Formel f2: (A ↔ B)

    # 4) Kombinér Imp og Iff i en større formel
    f3 = Or( Imp(A, And(B, C)), Iff(Not(D), A) )
    print("Formel f3:", f3)
    # Output: Formel f3: ((A → (B ∧ C)) ∨ (¬D ↔ A))

    # 5) Du kan også tilgå indholdet direkte:
    print("f1 antecedent (phi):", f1.phi)   # And(A, Not(B))
    print("f1 consequent (psi):", f1.psi)   # Or(C, D)
    print("f2 argumenter:", f2.phi, f2.psi) # A B