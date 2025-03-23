import random

class Kalah:
    def __init__(self):
        # Board: [Player 1 pits (0-5), P1 store (6), Player 2 pits (7-12), P2 store (13)]
        self.board = [4] * 6 + [0] + [4] * 6 + [0]  # 4 seeds in each pit, 0 in stores
        self.current_player = 1  # 1 for Player 1, 2 for Player 2
        self.is_first_move = True

    def display_board(self, line1="", line2=""):
        print("\n\n    ", end="")
        for i in range(12, 6, -1):
            print(f"{self.board[i]:2}", end=" ")
        print("\n", end="")
        print(f"{self.board[13]}                        {self.board[6]}", end="")
        print("\n    ", end="")
        for i in range(0, 6):
            print(f"{self.board[i]:2}", end=" ")
        print("\n\n", end="")


    def is_valid_move(self, pit):
        if self.current_player == 1 and 0 <= pit <= 5:
            return self.board[pit] > 0
        elif self.current_player == 2 and 7 <= pit <= 12:
            return self.board[pit] > 0
        return False
    
    def switch_start_position(self):
        if self.is_first_move == True:
            self.current_player = 3 - self.current_player


    def make_move(self, pit):
        if not self.is_valid_move(pit):
            return False
        
        self.is_first_move = False
        seeds = self.board[pit]
        self.board[pit] = 0
        current_pos = pit

        while seeds > 0:
            current_pos = (current_pos + 1) % 14
            # Skip opponent's store
            if (self.current_player == 1 and current_pos == 13) or \
               (self.current_player == 2 and current_pos == 6):
                continue
            self.board[current_pos] += 1
            seeds -= 1

        # Capture rule
        if self.current_player == 1 and 0 <= current_pos <= 5 and self.board[current_pos] == 1:
            opposite_pit = 12 - current_pos
            if self.board[opposite_pit] > 0:
                self.board[6] += self.board[opposite_pit] + 1
                self.board[opposite_pit] = 0
                self.board[current_pos] = 0
        elif self.current_player == 2 and 7 <= current_pos <= 12 and self.board[current_pos] == 1:
            opposite_pit = 12 - current_pos
            if self.board[opposite_pit] > 0:
                self.board[13] += self.board[opposite_pit] + 1
                self.board[opposite_pit] = 0
                self.board[current_pos] = 0

        # Check if move ended in player's store for extra turn
        extra_turn = (self.current_player == 1 and current_pos == 6) or \
                     (self.current_player == 2 and current_pos == 13)
        
        if not extra_turn:
            self.current_player = 3 - self.current_player  # Switch player (1->2 or 2->1)
        
        return True

    def is_game_over(self):
        return sum(self.board[0:6]) == 0 or sum(self.board[7:13]) == 0

    def collect_remaining_seeds(self):
        # Collect remaining seeds to respective stores
        self.board[6] += sum(self.board[0:6])
        self.board[13] += sum(self.board[7:13])
        for i in range(0, 6):
            self.board[i] = 0
        for i in range(7, 13):
            self.board[i] = 0

    def get_winner(self):
        if self.board[6] > self.board[13]:
            return "Player 1 wins!"
        elif self.board[13] > self.board[6]:
            return "Player 2 wins!"
        else:
            return "It's a tie!"
        

def play_game():
    game = Kalah()
    
    while not game.is_game_over():
        game.display_board()
        while True:
            try:
                if game.current_player == 1:
                    pit = int(input("Player 1, choose a pit (1-6): ")) - 1
                else:
                    pit = int(input("Player 2, choose a pit (1-6): ")) + 6
                if game.make_move(pit):
                    break
                print("Invalid move! Try again.")
            except ValueError:
                print("Please enter a valid number!")
    
    game.collect_remaining_seeds()
    game.display_board()
    print(game.get_winner())
    return  


if __name__ == "__main__":
    play_game()
