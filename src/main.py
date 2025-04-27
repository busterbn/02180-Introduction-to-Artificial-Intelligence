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
    

def expand_knowledge_base(bb):
    # New beliefs to try adding:
    bb.expand(parse_formula("D & O"),         source='heard')
    bb.expand(parse_formula("(A | P) -> S"),  source='heard')
    bb.expand(parse_formula("~(B & C)"),      source='heard')



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


if __name__ == '__main__':
    run_terminal_user_inteface()
