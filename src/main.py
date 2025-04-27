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
        print("Welcome to my Belief Base Engine\n")
        print("Menu")
        print("1: Start with empty belief base")
        print("2: Use a premade belief base")
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

    print("")
    print("Syntax for entering new formulas:")
    print("~ as Negation")
    print("& as and")
    print("| as or")
    print("-> as implies")
    print("<-> as bi-implies")
    print("Example: ~(B & C) -> A")

    while True:
        print("")
        formula = input("Add new formula: ")
        bb.expand(parse_formula(formula), source='expert')
        print("New belief base:")
        print(bb)

    add_costum_beliefs()

    # while True:
    #     print("1. Add your owf formula")
    #     print("2. Add this formula: D & O")
    #     print("3. Add this formula: (A | P) -> S")
    #     print("4. Add this formula: ~ (B & C)")
    #     print("Q: Quit")
    #     cmd = input("Enter number: ").upper()
    #     if cmd == '1':
    #         add_costum_beliefs()
    #     elif cmd == '2':
    #         bb.expand(parse_formula("D & O"),         source='observation')
    #         print("New belief base:")
    #         print(bb, "\n")
    #     elif cmd == '3':
    #         bb.expand(parse_formula("(A | P) -> S"),  source='expert')
    #         print("New belief base:")
    #         print(bb, "\n")
    #     elif cmd == '4':
    #         bb.expand(parse_formula("~ (B & C)"),      source='inference')
    #         print("New belief base:")
    #         print(bb, "\n")
    #     elif cmd == 'Q':
    #         print("Exiting...")
    #         break
    #     else:
    #         print("Invalid command.")



if __name__ == '__main__':
    run_terminal_user_inteface()
    add_initial_beliefs(bb)
    print("Base:")
    print(bb, "\n")
    expand_knowledge_base(bb)
    print("After expansion:")
    print(bb, "\n")

