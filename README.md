# 02180 - Introduction to Artificial Intelligence

Welcome to my repository for the DTU course **02180 - Introduction to Artificial Intelligence**. This repository contains projects completed as part of the course.

---

## Branches

This repository is organized into two primary branches, each corresponding to a different home assignment.

### 1. Board Game Assignment
- **Branch:** `board_game`
- **Description:**  
    Implementation of the game **Kalaha** using a Terminal User Interface (TUI) and then creating an AI opponent to play against. The AI still remains unbeaten to this day.
- **Content:**
    ```
    ├── LICENSE         → Contains the legal licensing information for the project.
    ├── README.md       → Provides an overview and instructions for the repository.
    ├── dockerfile      → Defines the instructions to build the Docker image.
    ├── justfile        → Contains task definitions for the Just command runner.
    └── src             → Directory holding the source code:
        ├── alphabeta.py → Implements the alpha-beta pruning algorithm for decision making.
        ├── kalah.py     → Contains the core logic and rules for the Kalah game.
        ├── main.py      → Serves as the main entry point of the application.
        └── min_max.py   → Implements the minimax algorithm for game strategy.
    ```
### 2. Belief Revision Assignment
- **Branch:** `belief_revision`
- **Description:**  
    Design and implementation of a belief revision engine that updates an agent's beliefs based on a given propositional formula.

---

Feel free to explore the projects and reuse my code!
