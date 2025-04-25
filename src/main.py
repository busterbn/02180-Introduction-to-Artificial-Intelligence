from belief_base import BeliefBase
from parser import parse_formula

# Creates an empty belief base
bb = BeliefBase()


def ranking_demo():
    seniority = 1.0
    DECAY = 0.95

    def add_belief(formula_str, priority=0, source='observation'):
        nonlocal seniority
        formula = parse_formula(formula_str)
        # Pass seniority via the timestamp parameter to Belief
        bb.expand(formula, priority=priority, source=source, timestamp=seniority)
        print(f"Added belief: {formula_str}, priority={priority}, source={source}, seniority={seniority:.2f}")
        seniority *= DECAY

    # Add beliefs of varying complexity and sources
    add_belief("A", priority=1, source='observation')
    add_belief("B & C", priority=2, source='expert')
    add_belief("(D | E) -> F", priority=3, source='hypothesis')
    add_belief("G & (H | (I -> J))", priority=1, source='inference')

    # Display static ranking
    print("\nBeliefs sorted by static rank:")
    for b in sorted(bb.beliefs, key=lambda b: b.compute_static_rank(), reverse=True):
        print(f"{b} | StaticRank={b.compute_static_rank():.2f}")

    # Simulate dynamic updates: boost usage on the first belief
    first_belief = bb.beliefs[0]
    for _ in range(5):
        first_belief.update_usage()

    # Compute dynamic metrics
    for b in bb.beliefs:
        b.compute_strength(bb)
        b.compute_consistency_contrib(bb)

    # Display dynamic ranking contributions
    print("\nBeliefs sorted by dynamic rank contribution:")
    for b in sorted(bb.beliefs, key=lambda b: b.compute_dynamic_rank(), reverse=True):
        print(f"{b} | DynamicRank={b.compute_dynamic_rank():.2f}")

    # Final combined ranking
    print("\nFinal combined ranking (static + dynamic):")
    print(bb)





def test_revi(bb):
    # B0: A ∧ B  (prio 1), C → A (prio 2)
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



if __name__ == '__main__':
    bb = BeliefBase()
    add_initial_beliefs(bb)
    print("Base:")
    print(bb, "\n")


