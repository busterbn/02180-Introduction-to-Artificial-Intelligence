from min_max import play_game as play_game_PvP
from min_max import play_game as play_game_PvMiniMax
from alphabeta import play_game as play_game_PvAlphaBeta

if __name__ == "__main__":
    while True:
        print("Chose a game mode:")
        print("1: Player vs. Player")
        print("2: Player vs. MiniMax")
        print("3: Player vs. Alpha Beta")
        print("Q: Quit")
        cmd = input("Enter number: ").upper()
        if cmd == '1':
            play_game_PvP()
        elif cmd == '2':
            depth = int(input("Enter MiniMax search depth: "))
            play_game_PvMiniMax(depth)
        elif cmd == '3':
            depth = int(input("Enter MiniMax search depth: "))
            play_game_PvAlphaBeta(depth)
        elif cmd == 'Q':
            print("Exiting...")
            break
        else:
            print("Invalid command.")