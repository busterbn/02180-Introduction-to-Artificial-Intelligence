
# Belief Base Engine — Propositional Logic & AGM Theory

This project is a belief base engine that supports expansion, contraction, and revision of propositional logic formulas based on AGM theory. It simulates how humans manage beliefs using ranked priorities and models logical inference using CNF transformation and resolution.

## 📂 Directory Structure

```
src/
├── belief.py             # Belief object with ranking logic
├── belief_base.py        # BeliefBase class with AGM operations
├── cnf.py                # CNF transformation utilities
├── formula_ast.py        # Formula AST node definitions
├── parser.py             # Propositional formula parser
├── resolution.py         # Resolution-based entailment algorithm
├── master_mind.py        # Master Mind Code breaker
└── main.py               # Terminal user interface and entry point
```

## 🚀 Requirements 

- Python 3.13.2 (Developed and tested with)
- No external dependencies required; using a virtual environment is recommended for isolation.

## ▶️ Getting Started

1. Clone the repository:
   ```bash
    git clone -b belief_revision --single-branch https://github.com/busterbn/02180-Introduction-to-Artificial-Intelligence.git
    cd 02180-Introduction-to-Artificial-Intelligence
   ```

2. Run the belief base engine:
   ```bash
   python3 src/main.py
   ```

3. You will now be presented with Menu:
   ```
    Menu
    1: Start with empty belief base
    2: Start with a premade belief base
    3: Run Master Mind solver

    Enter number: 
    ```

4. Choose:
- To test the belief base engine enter either 1 og 2 and press enter.
- To test our master mind solver enter 3 and press enter.

## ✍️ Formula Syntax

| Operator        | Symbols      | Example            |
|----------------|--------------|--------------------|
| Negation        | `¬`, `~`     | `~A`               |
| Conjunction     | `∧`, `&`     | `A & B`            |
| Disjunction     | `∨`, `\|`     | `A \| B`           |
| Implication     | `→`, `->`    | `A -> B`           |
| Biconditional   | `↔`, `<->`   | `A <-> B`          |

Parentheses can be used to group expressions.

## 🔬 Example

```text
> Add new formula: (A ∧ B) -> C
> Add new formula: A
> Add new formula: B
# Belief base now entails C due to resolution
```

## 📄 License

This project is developed as part of the DTU course **02180 - Introduction to Artificial Intelligence** and is intended for educational purposes.

## 👤 Author

Buster Bøgild Nielsen  
Technical University of Denmark (DTU)
