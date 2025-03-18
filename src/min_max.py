import copy
from kalah import Kalah
import math

# def evaluate_board(board, player):
#     # Weight factors for seeds in pits vs. seeds in the store.
#     pit_weight = 0.2

#     if player == 1:
#         store_diff = board[6] - board[13]
#         pits_score = sum(board[0:6]) - sum(board[7:13])

#     else:
#         store_diff = board[13] - board[6]
#         pits_score = sum(board[7:13]) - sum(board[0:6])
    
#     return store_diff + pit_weight * pits_score

def evaluate_board(board, player):
    pit_weight = 0.2
    penalty_factor = 0.3  # Penalty for leaving an empty pit opposite a filled one
    
    if player == 1:
        store_diff = board[6] - board[13]
        pits_score = sum(board[0:6]) - sum(board[7:13])
        penalty = 0
        # For player 1, pits are 0 to 5; opposite pits are index 12 down to 7.
        for i in range(0, 6):
            if board[i] == 0 and board[12 - i] > 0:
                penalty += penalty_factor * board[12 - i]
    else:
        store_diff = board[13] - board[6]
        pits_score = sum(board[7:13]) - sum(board[0:6])
        penalty = 0
        # For player 2, pits are 7 to 12; opposite pits are index 5 down to 0.
        for i in range(7, 13):
            if board[i] == 0 and board[12 - i] > 0:
                penalty += penalty_factor * board[12 - i]
    
    return store_diff + pit_weight * pits_score - penalty

def minimax(game, depth, is_maximizing, player):
    if depth == 0 or game.is_game_over():
        return evaluate_board(game.board, player)

    if is_maximizing:
        max_eval = float('-inf')
        pits = range(0, 6) if game.current_player == 1 else range(7, 13)
        for pit in pits:
            if game.board[pit] > 0:
                game_copy = copy.deepcopy(game)
                if game_copy.make_move(pit):
                    evaluation = minimax(game_copy, depth - 1, False, player)
                    max_eval = max(max_eval, evaluation)
        # print(f"MiniMax (maximizing) returns {max_eval}")
        return max_eval
    else:
        min_eval = float('inf')
        pits = range(0, 6) if game.current_player == 1 else range(7, 13)
        for pit in pits:
            if game.board[pit] > 0:
                game_copy = copy.deepcopy(game)
                if game_copy.make_move(pit):
                    evaluation = minimax(game_copy, depth - 1, True, player)
                    min_eval = min(min_eval, evaluation)
        # print(f"MiniMax (minimizing) returns {min_eval}")
        return min_eval

def find_best_move(game, depth):
    best_move = -1
    best_value = float('-inf') if game.current_player == 1 else float('inf')
    pits = range(0, 6) if game.current_player == 1 else range(7, 13)
    
    for pit in pits:
        print(f"Evaluating pit {pit}")
        if game.board[pit] > 0:
            game_copy = copy.deepcopy(game)
            if game_copy.make_move(pit):
                board_value = minimax(game_copy, depth - 1, game.current_player == 2, game.current_player)
                if (game.current_player == 1 and board_value > best_value) or \
                   (game.current_player == 2 and board_value < best_value):
                    best_value = board_value
                    best_move = pit
    return best_move

def play_game(depth):
    game = Kalah()
    
    while not game.is_game_over():
        game.display_board()
        if game.current_player == 1:
            while True:
                try:
                    pit = int(input("Player 1, choose a pit (1-6): ")) - 1
                    if game.make_move(pit):
                        break
                    print("Invalid move! Try again.")
                except ValueError:
                    print("Please enter a valid number!")
        else:
            print("Minimax is thinking...")
            pit = find_best_move(game, depth)
            game.make_move(pit)
    
    game.collect_remaining_seeds()
    game.display_board()
    print(game.get_winner())

def play_game_minimax_vs_minimax(depth):
    game = Kalah()
    
    while not game.is_game_over():
        game.display_board()
        if game.current_player == 1:
            print(f"Player 1 is thinking...")
            pit = find_best_move(game, depth)
            print(f"Pit {pit} seems best")
            game.make_move(pit)
        else:
            print(f"Player 2 is thinking...")
            pit = find_best_move(game, depth)
            print(f"Pit {pit} seems best")
            game.make_move(pit)
    
    game.collect_remaining_seeds()
    game.display_board()
    print(game.get_winner())
    return game.get_winner()

if __name__ == "__main__":
    play_game(7)

