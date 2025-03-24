import copy
from kalah import Kalah
import math
import time

def minimax_alpha_beta(game, depth, alpha=float("-inf"), beta=float("inf")):
    best_move = -1
    if depth == 0 or game.is_game_over():
        final_score = game.board[13] - game.board[6]
        return final_score, best_move

    if game.current_player == 2:
        best_score = float("-inf")
        for pit in range(7, 13):
            if game.is_valid_move(pit):
                game_copy = copy.deepcopy(game)
                game_copy.make_move(pit)
                if game_copy.current_player == 2:
                    score_temp, _ = minimax_alpha_beta(game_copy, depth, alpha, beta)
                else:
                    score_temp, _ = minimax_alpha_beta(game_copy, depth - 1, alpha, beta)
                if score_temp > best_score:
                    best_score = score_temp
                    best_move = pit
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score, best_move

    elif game.current_player == 1:
        best_score = float("inf")
        for pit in range(0, 6):
            if game.is_valid_move(pit):
                game_copy = copy.deepcopy(game)
                game_copy.make_move(pit)
                if game_copy.current_player == 1:
                    score_temp, _ = minimax_alpha_beta(game_copy, depth, alpha, beta)
                else:
                    score_temp, _ = minimax_alpha_beta(game_copy, depth - 1, alpha, beta)
                if score_temp < best_score:
                    best_score = score_temp
                    best_move = pit
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score, best_move
                

def play_game(depth):
    game = Kalah()
    last_to_move = '0'
        
    while True:
        print("Who should start?")
        print("1: You")
        print("2: The AI")
        val = int(input(""))
        if val == 1:
            break
        elif val == 2:
            game.switch_start_position()
            break
        else:
            print("Invalid choise !!")


    game.display_board()
    while not game.is_game_over():
        if game.current_player == 1:
            while True:
                try:
                    if last_to_move == 1:
                        print("It's your turn again !!")
                    else:
                        print("It's your turn")
                    pit = int(input("Please choose a pit (1-6): ")) - 1
                    if game.make_move(pit):
                        print(f"You moved pit {pit+1}")
                        time.sleep(1)
                        game.display_board()
                        time.sleep(1)
                        last_to_move = 1
                        break
                    print("Invalid move! Try again.")
                except ValueError:
                    print("Please enter a valid number!")
        else:
            if last_to_move == 2:
                print("It's MiniMaxAlphaBeta's turn again !!")
            else:
                print(f"It's MiniMaxAlphaBeta's turn")
            time.sleep(1)
            score, move = minimax_alpha_beta(game, depth)
            print(f"MiniMaxAlphaBeta moves pit {move-6}")
            game.make_move(move)
            time.sleep(1)
            game.display_board()
            time.sleep(1)
            last_to_move = 2
    
    game.collect_remaining_seeds()
    game.display_board()
    print(game.get_winner())

if __name__ == "__main__":
    play_game(8)

