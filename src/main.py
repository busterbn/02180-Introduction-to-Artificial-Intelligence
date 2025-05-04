from belief_base import BeliefBase
from parser import parse_formula
from time import sleep
from master_mind import run_mastermind_with_belief_base

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
        print("2: Start with a premade belief base")
        print("3: Run Master Mind solver")
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
            print("Running Master Mind Solver")
            sleep(1)
            run_mastermind_with_belief_base()
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
