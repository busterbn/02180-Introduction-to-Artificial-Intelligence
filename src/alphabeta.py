from kalah import Kalah


def evaluate_board(board, player):
    if player == 1:
        return board[6] - board[13]
    else:
        return board[13] - board[6]


def alphabeta(board, depth, alpha, beta, is_maximizing, player):
    if depth == 0 or Kalah().is_game_over():
        return evaluate_board(board, player)

    if is_maximizing:
        max_eval = float('-inf')
        for pit in range(6):
            if board[pit] > 0:
                new_board = board[:]
                Kalah().make_move(pit)
                eval = alphabeta(new_board, depth - 1, alpha, beta, False, player)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for pit in range(7, 13):
            if board[pit] > 0:
                new_board = board[:]
                Kalah().make_move(pit)
                eval = alphabeta(new_board, depth - 1, alpha, beta, True, player)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


def find_best_move(game, depth):
    best_move = -1
    best_value = float('-inf') if game.current_player == 1 else float('inf')
    alpha = float('-inf')
    beta = float('inf')

    for pit in range(6) if game.current_player == 1 else range(7, 13):
        print(f"Evaluating pit {pit-6}")
        if game.board[pit] > 0:
            new_board = game.board[:]
            Kalah().make_move(pit)
            board_value = alphabeta(new_board, depth - 1, alpha, beta, game.current_player == 2, game.current_player)
            if (game.current_player == 1 and board_value > best_value) or \
                (game.current_player == 2 and board_value < best_value):
                best_value = board_value
                best_move = pit
                if game.current_player == 1:
                    alpha = max(alpha, board_value)
                else:
                    beta = min(beta, board_value)
                if beta <= alpha:
                    break

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
            print("AlphaBeta is thinking...")
            pit = find_best_move(game, depth)
            game.make_move(pit)
    
    game.collect_remaining_seeds()
    game.display_board()
    print(game.get_winner())


if __name__ == "__main__":
    depth = int(input("Enter MiniMax search depth: "))
    play_game(depth)
