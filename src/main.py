from belief_base import BeliefBase
from parser import parse_formula

bb = BeliefBase()


def test_revi(bb):
    bb.expand(parse_formula("A & B"), source='observation', seniority=1.0)
    bb.expand(parse_formula("C -> A"), source='observation', seniority=1.0)
    print("Base:")
    print(bb, "\n")

    # Check entailment: Does the base entail A?
    print("Entails A?", bb.entails(parse_formula("A")))

    # Revise by ¬B (prio 3)
    bb.revise(parse_formula("~B"), source='observation', )
    print("\nAfter revising with ¬B:")
    print(bb)


def add_initial_beliefs(bb):
    # Initial belief base:
    bb.expand(parse_formula("A"),                  source='observation', seniority=1.0)
    bb.expand(parse_formula("B & C"),              source='expert',      seniority=1.0)
    bb.expand(parse_formula("D -> A"),             source='hypothesis',  seniority=1.0)
    bb.expand(parse_formula("(E | F) -> G"),       source='expert',      seniority=1.0)
    bb.expand(parse_formula("H | I"),              source='observation', seniority=1.0)
    bb.expand(parse_formula("J -> (K & L)"),       source='hypothesis',  seniority=1.0)
    bb.expand(parse_formula("M <-> N"),              source='expert',      seniority=1.0)
    bb.expand(parse_formula("~O"),                 source='inference',   seniority=1.0)
    bb.expand(parse_formula("(P | Q) & R"),        source='observation', seniority=1.0)
    bb.expand(parse_formula("S -> (T | U)"),       source='hypothesis',  seniority=1.0)
    bb.expand(parse_formula("V & (W | X)"),        source='expert',      seniority=1.0)
    bb.expand(parse_formula("(Y -> Z) -> A"),      source='hypothesis',  seniority=1.0)
    bb.expand(parse_formula("B -> ~D"),            source='inference',   seniority=1.0)
    bb.expand(parse_formula("(C & E) -> H"),       source='expert',      seniority=1.0)
    bb.expand(parse_formula("I | (J & K)"),        source='observation', seniority=1.0)
    bb.expand(parse_formula("(L -> M) & (N -> O)"),source='hypothesis',  seniority=1.0)
    

def expand_knowledge_base(bb):
    # New beliefs to try adding:
    bb.expand(parse_formula("D & O"),         source='observation')
    bb.expand(parse_formula("(A | P) -> S"),  source='expert')
    bb.expand(parse_formula("~ (B & C)"),      source='inference')

if __name__ == '__main__':
    add_initial_beliefs(bb)
    print("Base:")
    print(bb, "\n")
    expand_knowledge_base(bb)
    print("After expansion:")
    print(bb, "\n")




