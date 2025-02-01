class Mancala:
    def __init__(self):
        # Initialize board: 6 pits per player with 4 stones each, and 2 stores (0 stones initially)
        self.board = [4] * 6 + [0] + [4] * 6 + [0]
        self.current_player = 1  # Player 1 starts

    def move(self, pit_index):
        # Ensure the move is valid
        if not self.is_valid_move(pit_index):
            print("Invalid move. Try again.")
            return False

        # Convert pit number (1-6) to board index
        actual_index = pit_index - 1 if self.current_player == 1 else pit_index + 6

        # Pick up the stones
        stones = self.board[actual_index]
        self.board[actual_index] = 0
        index = actual_index

        # Distribute stones
        while stones > 0:
            index = (index + 1) % 14  # Move counterclockwise

            # Skip opponent's store
            if (self.current_player == 1 and index == 13) or (self.current_player == 2 and index == 6):
                continue

            self.board[index] += 1
            stones -= 1

        # Capture Rule: If last stone lands in an empty own pit
        if self.board[index] == 1 and self.is_own_pit(index):
            opposite_index = 12 - index
            if self.board[opposite_index] > 0:
                self.board[self.store_index()] += self.board[opposite_index] + 1
                self.board[index] = 0
                self.board[opposite_index] = 0

        # If last stone lands in player's store, they get another turn
        if index != self.store_index():
            self.current_player = 2 if self.current_player == 1 else 1

        return True

    def is_valid_move(self, pit_index):
        if pit_index < 1 or pit_index > 6:
            return False
        actual_index = pit_index - 1 if self.current_player == 1 else pit_index + 6
        return self.board[actual_index] > 0

    def is_own_pit(self, index):
        return (self.current_player == 1 and 0 <= index <= 5) or (self.current_player == 2 and 7 <= index <= 12)

    def store_index(self):
        return 6 if self.current_player == 1 else 13

    def game_over(self):
        # Check if one side of the board is empty
        if sum(self.board[0:6]) == 0 or sum(self.board[7:13]) == 0:
            # Collect remaining stones
            self.board[6] += sum(self.board[0:6])
            self.board[13] += sum(self.board[7:13])
            for i in range(6):
                self.board[i] = 0
                self.board[i + 7] = 0
            return True
        return False

    def print_board(self):
        print("\nPlayer 2")
        print(" ", self.board[12:6:-1])
        print(self.board[13], " " * 18, self.board[6])
        print(" ", self.board[0:6])
        print("Player 1\n")

def main():
    game = Mancala()
    while not game.game_over():
        game.print_board()
        try:
            pit = int(input(f"Player {game.current_player}, choose a pit (1-6): "))
            if game.move(pit):
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
    game.print_board()
    print("Game over!")
    if game.board[6] > game.board[13]:
        print("Player 1 wins!")
    elif game.board[6] < game.board[13]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
