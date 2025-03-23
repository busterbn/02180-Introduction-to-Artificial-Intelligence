# 02180-Introduction-to-Artificial-Intelligence
This repository contains the course work of group 52 in the DTU course 02180 Introduction to Artificial Intelligence.

## Requirements
You need to have the following installed:
- `just`    >= 1.40.0
- `docker`  >= 27.5.1

Make sure your docker daemon is running

## Build instructions

Follow these steps to build the project:

1. Clone this repository:
    ```bash
    cd ~/
    git clone https://github.com/busterbn/02180-Introduction-to-Artificial-Intelligence.git
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

2. You should now be prompted to make the first move:
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