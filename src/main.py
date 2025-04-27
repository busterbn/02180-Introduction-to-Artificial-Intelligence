from belief_base import BeliefBase
from parser import parse_formula
from time import sleep

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
    bb.expand(parse_formula("~(B & C)"),      source='inference')



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
        print("")
        cmd = input("Enter number: ").upper()
        if cmd == '1':
            print("Starting with empty belief base\n")
            sleep(1)
            break
        elif cmd == '2':
            print("Using premade belief base\n")
            sleep(1)
            add_initial_beliefs(bb)
            break
        else:
            print("Invalid command.\n")
            sleep(1)
    
    print("Current belief base:")
    print(bb)
    sleep(1)

    while True:
        print("")
        print("Menu")
        print("1. Add new formula")
        print("2. Check entailment")
        print("")
        cmd = input("Enter number: ")

        if cmd == '1':
            while True:
                print("")
                user_input = input("Enter formula: ")
                try:
                    f = parse_formula(user_input)
                    break
                except ValueError as e:
                    print("Syntax error:", e)
            print(f"\nAdding {f} to belief base\n")
            sleep(1)
            bb.revise(f, source='expert')
            print("New belief base:")
            print(bb)
            sleep(1)

        if cmd == '2':
            while True:
                user_input = input("Enter formula: ")
                try:
                    f = parse_formula(user_input)
                    break
                except ValueError as e:
                    print("Syntax error:", e)
            print(f"Entails {f}?")
            sleep(1)
            print(bb.entails(f))
            sleep(1)


if __name__ == '__main__':
    run_terminal_user_inteface()
    add_initial_beliefs(bb)
    print("Base:")
    print(bb, "\n")
    expand_knowledge_base(bb)
    print("After expansion:")
    print(bb, "\n")

