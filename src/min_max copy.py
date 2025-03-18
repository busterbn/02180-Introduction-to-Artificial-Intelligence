from kalah import Kalah
import random
import math
    

def evaluate_board(board, player):
    # if player == 1:
    #     return sum(board[0:6])
    # else:
    #     return sum(board[7:13])

    if player == 1:
        evaluation = 2 * (board[6] - board[13])
        evaluation
        return board[6] - board[13]
    else:
        return board[13] - board[6]


def minimax(board, depth, is_maximizing, player):
    if depth == 0 or Kalah().is_game_over():
        return evaluate_board(board, player)

    if is_maximizing:
        max_eval = float('-inf')
        for pit in range(6):
            if board[pit] > 0:
                new_board = board[:]
                Kalah().make_move(pit)
                eval = minimax(new_board, depth - 1, False, player)
                max_eval = max(max_eval, eval)
        print(f"MiniMax found max_eval: {max_eval}")
        return max_eval
    else:
        min_eval = float('inf')
        for pit in range(7, 13):
            if board[pit] > 0:
                new_board = board[:]
                Kalah().make_move(pit)
                eval = minimax(new_board, depth - 1, True, player)
                min_eval = min(min_eval, eval)
        print(f"MiniMax found min_eval: {min_eval}")
        return min_eval


def find_best_move(game, depth):
    best_move = -1
    best_value = float('-inf') if game.current_player == 1 else float('inf')

    for pit in range(6) if game.current_player == 1 else range(7, 13):
        print(f"Evaluating pit {pit}")
        if game.board[pit] > 0:
            new_board = game.board[:]
            Kalah().make_move(pit)
            board_value = minimax(new_board, depth - 1, game.current_player == 2, game.current_player)
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
    play_game(4)

