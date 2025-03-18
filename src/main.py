from min_max import play_game as play_game_PvP
from min_max import play_game as play_game_PvMiniMax
from alphabeta import play_game as play_game_PvAlphaBeta
from kalah import Kalah

import min_max
import alphabeta
from time import time


def MiniMax_vs_AlphaBeta(MiniMax_depth, AlphBeta_depth):
    game = Kalah()
    
    while not game.is_game_over():
        game.display_board()
        if game.current_player == 1:
            game.flip_board()
            print("Minimax is thinking...")
            pit = min_max.find_best_move(game, MiniMax_depth)
            print(f"MiniMax will move pit {pit}")
            game.make_move(pit)
            game.flip_board()
        else:
            print("AlphaBeta is thinking...")
            pit = alphabeta.find_best_move(game, AlphBeta_depth)
            print(f"AlphaBeta will move pit {pit}")
            game.make_move(pit)

        
    game.collect_remaining_seeds()
    game.display_board()
    print(game.get_winner())


def MiniMax_vs_MiniMax(depth1, depth2):
    game = Kalah()
    
    while not game.is_game_over():
        game.display_board()
        time.sleep(1.5)
        print(f"Player {game.current_player} is thinking...")
        if game.current_player == 1:
            pit = min_max.find_best_move(game, depth1)
            print(f"Player 1 will move pit {pit}")
            game.make_move(pit)
        else:
            pit = alphabeta.find_best_move(game, depth2)
            print(f"Player 2 will move pit {pit}")
            game.make_move(pit)
    
    game.collect_remaining_seeds()
    game.display_board()
    print(game.get_winner())



if __name__ == "__main__":
    while True:
        print("Chose a game mode:")
        print("1: Player vs. Player")
        print("2: Player vs. MiniMax")
        print("3: Player vs. Alpha Beta")
        print("4: MiniMax vs. Alpha Beta")
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
        elif cmd == '4':
            MiniMax_depth = int(input("Enter MiniMax search depth: "))
            AlphBeta_depth = int(input("Enter AlphaBeta search depth: "))
            MiniMax_vs_AlphaBeta(MiniMax_depth, AlphBeta_depth)
        elif cmd == 'Q':
            print("Exiting...")
            break
        else:
            print("Invalid command.")