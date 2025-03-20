import copy
from kalah import Kalah
import math
import time

def evaluate_board(board, player):
    utility = 0
    player_store = 6 if player == 1 else 13
    opponent_store = 13 if player == 1 else 6
    player_side = range(0, 6) if player == 1 else range(7, 13)
    opponent_side = range(7, 13) if player == 1 else range(0, 6)

    # Add points for counters in player's store
    utility += board[player_store] * 4

    # Add points for holes with 13 counters on player's side
    utility += sum(4 for pit in player_side if board[pit] == 13)

    # Add points for holes with exact counters to receive another move
    for pit in player_side:
        if board[pit] > 0 and (pit + board[pit]) == player_store:
            utility += 2

    # Add points for empty holes on player's side
    utility += sum(1 for pit in player_side if board[pit] == 0)

    # Subtract points for opponent's store and advantageous positions
    utility -= board[opponent_store] * 4
    utility -= sum(4 for pit in opponent_side if board[pit] == 13)
    utility -= sum(1 for pit in opponent_side if board[pit] == 0)

    return utility

# def evaluate_board(board, player):
#     pit_weight = 0.2
#     penalty_factor = 100  # Penalty for leaving an empty pit opposite a filled one


#     # Rewards
#     store_diff =  board[6] - board[13]
#     pits_score = sum(board[0:6]) - sum(board[7:13])
    
#     # Penalty
#     penalty = 0

#     if player == 1:
#         for i in range(7, 13):
#             if board[i] == 0 and board[12 - i] > 0:
#                 penalty += penalty_factor * board[12 - i]
    
#     elif player == 2:
#         for i in range(0, 6):
#             if board[i] == 0 and board[12 - i] > 0:
#                 penalty -= penalty_factor * board[12 - i]

    
#     return store_diff + pit_weight * pits_score + penalty

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
        # print(f"Evaluating pit {pit}")
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
    last_to_move = '0'
    while not game.is_game_over():
        if game.current_player == 1:
            while True:
                try:
                    if last_to_move == 1:
                        game.display_board("You get an extra turn !!", "Please choose a pit (1-6)")
                    else:
                        game.display_board("It's your turn", "Please choose a pit (1-6)")
                    pit = int(input()) - 1
                    if game.make_move(pit):
                        game.display_board("", f"You moved pit {pit+1}")
                        time.sleep(2)
                        last_to_move = 1
                        break
                    print("Invalid move! Try again.")
                except ValueError:
                    print("Please enter a valid number!")
        else:
            if last_to_move == 2:
                game.display_board("The AI get's an extra turn !!", "Please wait for it to make a move :)")
            else:
                game.display_board("It's the AI's turn", "Please wait for it to make a move :)")
            time.sleep(4)
            pit = find_best_move(game, depth)
            game.make_move(pit)
            game.display_board(f"The AI moved its pit {pit-6}")
            last_to_move = 2
            time.sleep(4)
    
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
    play_game(3)

