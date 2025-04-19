from data_structures import *

def eliminate_iff(formula: Formula) -> Formula:
    if isinstance(formula, Iff):
        A, B = formula.phi, formula.psi
        # A ↔ B  ≡  (A → B) ∧ (B → A)
        return And( Imp(eliminate_iff(A), eliminate_iff(B)),
                    Imp(eliminate_iff(B), eliminate_iff(A)) )
    if isinstance(formula, (And, Or)):
        ctor = And if isinstance(formula, And) else Or
        return ctor(*(eliminate_iff(p) for p in formula.conj if isinstance(formula, And)
                                   else (formula.disj)))
    if isinstance(formula, Not):
        return Not(eliminate_iff(formula.phi))
    if isinstance(formula, Imp):
        return Imp(eliminate_iff(formula.phi), eliminate_iff(formula.psi))
    return formula  # Var

def eliminate_imp(formula: Formula) -> Formula:
    if isinstance(formula, Imp):
        # A → B ≡ ¬A ∨ B
        return Or( Not(eliminate_imp(formula.phi)), eliminate_imp(formula.psi) )
    if isinstance(formula, (And, Or)):
        ctor = And if isinstance(formula, And) else Or
        args = formula.conj if isinstance(formula, And) else formula.disj
        return ctor(*(eliminate_imp(p) for p in args))
    if isinstance(formula, Not):
        return Not(eliminate_imp(formula.phi))
    return formula

def push_negations(formula: Formula) -> Formula:
    # Sørg for kun ¬ foran Var ved hjælp af De Morgan
    if isinstance(formula, Not):
        inner = formula.phi
        if isinstance(inner, Not):
            return push_negations(inner.phi)           # ¬¬A ≡ A
        if isinstance(inner, And):
            return Or(*(push_negations(Not(p)) for p in inner.conj))
        if isinstance(inner, Or):
            return And(*(push_negations(Not(p)) for p in inner.disj))
        return formula  # ¬Var
    if isinstance(formula, (And, Or)):
        ctor = And if isinstance(formula, And) else Or
        args = formula.conj if isinstance(formula, And) else formula.disj
        return ctor(*(push_negations(p) for p in args))
    return formula

def distribute_or_over_and(formula: Formula) -> Formula:
    # Gør (A ∨ (B ∧ C)) til ((A ∨ B) ∧ (A ∨ C))
    if isinstance(formula, Or):
        # find en conj‑argument
        for p in formula.disj:
            if isinstance(p, And):
                rest = [x for x in formula.disj if x is not p]
                # ( rest ∨ (q ∧ r) ) ≡ ( (rest ∨ q) ∧ (rest ∨ r) )
                return And(
                    distribute_or_over_and( Or(*(rest + [p.conj[0]])) ),
                    distribute_or_over_and( Or(*(rest + [p.conj[1]])) )
                )
        return Or(*(distribute_or_over_and(p) for p in formula.disj))
    if isinstance(formula, And):
        return And(*(distribute_or_over_and(p) for p in formula.conj))
    return formula

def to_cnf(formula: Formula):
    f1 = eliminate_iff(formula)
    f2 = eliminate_imp(f1)
    f3 = push_negations(f2)
    f4 = distribute_or_over_and(f3)
    return f4  # stadig som træ af And/Or/Not/Var