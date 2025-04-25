from cnf import to_cnf
from formula_ast import Not
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
