import min_max
import alphabeta
import kalah
from kalah import Kalah
from time import time

if __name__ == "__main__":
    while True:
        print("Chose a game mode:")
        print("1: Player vs. Player")
        print("2: Player vs. MiniMax")
        print("3: Player vs. MiniMax with Alpha Beta pruning")
        print("Q: Quit")
        cmd = input("Enter number: ").upper()
        if cmd == '1':
            kalah.play_game()
        elif cmd == '2':
            depth = int(input("Enter MiniMax search depth (recommended: 6): "))
            min_max.play_game(depth)
        elif cmd == '3':
            depth = int(input("Enter MiniMax search depth (recommended: 8): "))
            alphabeta.play_game(depth)
        elif cmd == 'Q':
            print("Exiting...")
            break
        else:
            print("Invalid command.")