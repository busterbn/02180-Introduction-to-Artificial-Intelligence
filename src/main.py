from belief_base import BeliefBase
from parser import parse_formula
from time import sleep

# AGM postulate tests
def test_agm_postulates():
    """
    Test the BeliefBase revision operator against AGM postulates:
    Success, Inclusion, Vacuity, Consistency, and Extensionality.
    """
    from formula_ast import Atom, Not, And, Or, Implies, Bicond
    from belief_base import BeliefBase
    print("\nRunning AGM Postulate Tests")
    # Initial belief base with a single atom A
    K = BeliefBase()
    K.expand(Atom('A'))
    # 1. Success: K * φ should entail φ
    phi = Atom('B')
    K1 = BeliefBase()
    K1.beliefs = K.beliefs.copy()
    K1.revise(phi)
    assert K1.entails(phi), "Success postulate failed"
    print("✓ Success postulate passed")
    # 2. Inclusion: K * φ ⊆ K + φ
    K2 = BeliefBase()
    K2.beliefs = K.beliefs.copy()
    K2_expanded = BeliefBase()
    K2_expanded.beliefs = K.beliefs.copy()
    K2_expanded.expand(phi)
    K2.revise(phi)
    assert set(b.f for b in K2.beliefs).issubset(
        set(b.f for b in K2_expanded.beliefs)
    ), "Inclusion postulate failed"
    print("✓ Inclusion postulate passed")
    # 3. Vacuity: if ¬ψ ∉ K, then K * ψ = K + ψ
    psi = Atom('C')
    K3 = BeliefBase()
    K3.beliefs = K.beliefs.copy()
    if not K3.entails(Not(psi)):
        K3.revise(psi)
        K3_expanded = BeliefBase()
        K3_expanded.beliefs = K.beliefs.copy()
        K3_expanded.expand(psi)
        assert set(b.f for b in K3.beliefs) == set(
            b.f for b in K3_expanded.beliefs
        ), "Vacuity postulate failed"
        print("✓ Vacuity postulate passed")
    # 4. Consistency: if φ is consistent, then K * φ is consistent
    phi4 = Atom('D')
    K4 = BeliefBase()
    K4.beliefs = K.beliefs.copy()
    if not K4.entails(Not(phi4)):
        K4.revise(phi4)
        contradiction = And(Atom('X'), Not(Atom('X')))
        assert not K4.entails(contradiction), "Consistency postulate failed"
        print("✓ Consistency postulate passed")
    # 5. Extensionality: logically equivalent formulas yield same revision
    phi1 = Implies(Atom('A'), Atom('B'))
    phi2 = Or(Not(Atom('A')), Atom('B'))
    K5 = BeliefBase()
    K5.beliefs = K.beliefs.copy()
    K5.revise(phi1)
    entails1 = K5.entails(phi2)
    K6 = BeliefBase()
    K6.beliefs = K.beliefs.copy()
    K6.revise(phi2)
    entails2 = K6.entails(phi1)
    assert entails1 and entails2, "Extensionality postulate failed"
    print("✓ Extensionality postulate passed")
    print("All AGM postulates passed successfully.\n")

bb = BeliefBase()

def add_initial_beliefs(bb):
    bb.expand(parse_formula("A"),                  source='observation', seniority=1.0)
    bb.expand(parse_formula("B & C"),              source='observation',      seniority=1.0)
    bb.expand(parse_formula("(E | F) -> G"),       source='observation',      seniority=1.0)
    bb.expand(parse_formula("H | I"),              source='observation', seniority=1.0)
    bb.expand(parse_formula("J -> (K & L)"),       source='observation',  seniority=1.0)
    bb.expand(parse_formula("~O"),                 source='observation',   seniority=1.0)
    bb.expand(parse_formula("(P | Q) & R"),        source='observation', seniority=1.0)
    bb.expand(parse_formula("S -> (T | U)"),       source='observation',  seniority=1.0)
    bb.expand(parse_formula("V & (W | X)"),        source='observation',      seniority=1.0)
    bb.expand(parse_formula("B -> ~D"),            source='observation',   seniority=1.0)
    bb.expand(parse_formula("(C & E) -> H"),       source='observation',      seniority=1.0)
    bb.expand(parse_formula("I | (J & K)"),        source='observation', seniority=1.0)
    bb.expand(parse_formula("(L -> M) & (N -> O)"),source='observation',  seniority=1.0)

def run_terminal_user_inteface():
    while True:
        print("Welcome to this Belief Base Engine")
        print("")
        print("Syntax for entering formulas:")
        print("Negation: ¬ or ~ ")
        print("Conjunction: ∧ or &")
        print("Disjunction: ∨ or |")
        print("Implication: → or ->")
        print("Bi-Implication: ↔ or <->")
        print("Example: ~(B & C) -> A")
        print("")
        print("Menu")
        print("1: Start with empty belief base")
        print("2: Use a premade belief base")
        print("3: Run AGM postulate tests")
        print("")
        cmd = input("Enter number: ").upper()
        if cmd == '1':
            print("Starting with empty belief base")
            sleep(1)
            break
        elif cmd == '2':
            print("Using premade belief base")
            sleep(1)
            add_initial_beliefs(bb)
            break
        elif cmd == '3':
            print("Running AGM postulate tests")
            sleep(1)
            test_agm_postulates()
            return
        else:
            print("Invalid command.\n")
            sleep(1)
    
    print("")
    sleep(1)
    print("Current belief base:")
    sleep(1)
    print(bb)
    sleep(1)

    while True:
        while True:
            print("")
            user_input = input("Add new formula: ")
            try:
                f = parse_formula(user_input)
                break
            except ValueError as e:
                print("Syntax error:", e)
        print(f"Adding {f} to belief base")
        sleep(1)
        print("")
        sleep(1)
        bb.revise(f, source='expert')
        sleep(1)
        print("")
        sleep(1)
        print("New belief base:")
        sleep(1)
        print(bb)
        sleep(1)


if __name__ == '__main__':
    run_terminal_user_inteface()
