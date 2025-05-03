
# Belief Base Engine — Propositional Logic & AGM Theory

This project is a belief base engine that supports expansion, contraction, and revision of propositional logic formulas based on AGM theory. It simulates how humans manage beliefs using ranked priorities and models logical inference using CNF transformation and resolution.

## 📚 Features

- **Belief Base**:
  - Expand beliefs (add new information)
  - Contract beliefs (remove entailed statements)
  - Revise beliefs (AGM-style update using Levi identity)
- **Ranking Mechanism**:
  - Static entrenchment based on:
    - Formula seniority (age)
    - Source trustworthiness
    - Formula complexity
- **Entailment Testing**:
  - CNF conversion
  - Resolution-based entailment algorithm
- **User Interaction**:
  - Terminal interface for entering and revising formulas
  - Built-in AGM postulate tests

## 📂 Directory Structure

```
src/
├── belief.py             # Belief object with ranking logic
├── belief_base.py        # BeliefBase class with AGM operations
├── cnf.py                # CNF transformation utilities
├── formula_ast.py        # Formula AST node definitions
├── parser.py             # Propositional formula parser
├── resolution.py         # Resolution-based entailment algorithm
└── main.py               # Terminal user interface and entry point
```

## 🧠 Static Entrenchment Ranking

Each belief is assigned a rank based on:

- **Seniority**: Older beliefs are less likely to be discarded
- **Source**: More trustworthy sources (e.g., observation) are preferred
- **Complexity**: Structurally richer formulas are prioritized

This ranking affects which beliefs are removed during contraction.

## Requirements 🚀

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

3. Choose between:
   - Starting with an empty belief base
   - Using a pre-made belief base

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
