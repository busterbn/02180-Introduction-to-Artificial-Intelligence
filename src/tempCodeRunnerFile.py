import copy
from kalah import Kalah
import math
import time

def minimax(game, depth):
    best_move = -1
    # When the game is over or max depth is reached the board is evaluated
    if depth == 0 or game.is_game_over():
        final_score = game.board[13] - game.board[6]
        return final_score, best_move
    
    # Finding the AI's best move
    if game.current_player == 2:
        best_score = float("-inf")

        # Loop over all moves
        for pit in range(7, 13):

            # Discard impossible moves
            if game.is_valid_move(pit):

                # Simulate the move
                game_copy = copy.deepcopy(game)
                game_copy.make_move(pit)
                
                # The depth is not decremented when a player gets an extra turn
                if game_copy.current_player == 2:
                    score_temp, _ = minimax(game_copy, depth)
                else:
                    score_temp, _ = minimax(game_copy, depth-1)
                
                # Check if the move is the best one yet.
                if score_temp > best_score:
                    best_score = score_temp
                    best_move = pit
        return best_score, best_move
    
    elif game.current_player == 1:
        # Here we do the inverse for the minimizing player
        best_score = float("inf")
        for pit in range(0, 6):
            if game.is_valid_move(pit):
                game_copy = copy.deepcopy(game)
                game_copy.make_move(pit)

                if game_copy.current_player == 1:
                    score_temp, _ = minimax(game_copy, depth)
                else:
                    score_temp, _ = minimax(game_copy, depth-1)

                if score_temp < best_score:
                    best_score = score_temp
                    best_move = pit
        return best_score, best_move

def minimax_alpha_beta(game, depth, alpha=0, beta=0):
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
    game.display_board()
    while not game.is_game_over():
        if game.current_player == 1:
            while True:
                try:
                    if last_to_move == 1:
                        print("It's your turn again !!")
                    else:
                        print("It's your turn")
                    if game.is_first_move:
                        text = input("Please choose a pit (1-6) or write 'skip' to let the AI start: ")
                        if text == "skip":
                            game.switch_start_position()
                            print(f"player={game.current_player}")
                            break
                        pip = int(text) - 1
                    else:
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
                print("It's MiniMax's turn again !!")
            else:
                print(f"It's MiniMax's turn")
            time.sleep(1)
            score, move = minimax(game, depth)
            print(f"MiniMax moves pit {move-6} with anticipated score {score}")
            game.make_move(move)
            time.sleep(1)
            game.display_board()
            time.sleep(1)
            last_to_move = 2
    
    game.collect_remaining_seeds()
    game.display_board()
    print(game.get_winner())

if __name__ == "__main__":
    play_game(6)

