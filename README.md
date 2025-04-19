# Board Game with AI opponent

This repository contains the following files with brief explanations:

```
02180-Introduction-to-Artificial-Intelligence
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

## Requirements

This project is setup to require a minimal number of utilities installed
locally. To do this, most of the task done during local development is performed
in [Docker](https://www.docker.com/). The requirements are thus:

- [🐳 Docker](https://www.docker.com/)
- [🤖 Just](https://github.com/casey/just)
  

## Build instructions

Follow these steps to build the project:

1. Clone this repository:
    ```bash
    git clone -b board_game --single-branch https://github.com/busterbn/02180-Introduction-to-Artificial-Intelligence.git
    cd 02180-Introduction-to-Artificial-Intelligence
    ```

2. Build the Docker image:
    ```bash
    just build
    ```

## How to play
1. Run the following command to start the game:
    ```zsh
    just run
    ```

2. You should now be able to choose a game mode by typisk 1, 2 or 3 and then hit Enter.

3. When playing against the AI, the TUI also allows you to pick a search depth.

4. The last configuration is who should start the game.

5. You should now be prompted to make the first move:
    ```txt
        4  4  4  4  4  4 
    0                        0
        4  4  4  4  4  4 

    It's your turn
    Please choose a pit (1-6)
    ```

## How to interpret the TUI
```txt
    4  4  4  4  4  4 
0 <--(a)                 0 <--(b)
    4  4  4  4  4  4 <--(c)
```
1. (a) This is your opponent's store.
2. (b) This is your own store.
3. (c) These are your pits from 1 to 6.

4. If you are unfamiliar with the Kalah rules, you can read them [here](https://www.rose-hulman.edu/class/cs/archive/other-old/archive/winter99/kalah/KalahRules.html).
