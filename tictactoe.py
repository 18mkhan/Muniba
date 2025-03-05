#  the TicTacToe board
TicTacToe = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

current_player = "X"

# Displays the current state of the TicTacToe board
def displayBoard():
    print(TicTacToe[0][0], "|", TicTacToe[0][1], "|", TicTacToe[0][2])
    print("----------")
    print(TicTacToe[1][0], "|", TicTacToe[1][1], "|", TicTacToe[1][2])
    print("----------")
    print(TicTacToe[2][0], "|", TicTacToe[2][1], "|", TicTacToe[2][2])


# check if there is a winner and returns the winning player's symbol
def checkWin():
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner or column_winner or diagonal_winner:
        return current_player
    else:
        return None

#  check for a winner in rows, columns and in diagonal and returns the winning position
def check_rows():
    if TicTacToe[0][0] == TicTacToe[0][1] == TicTacToe[0][2] != " ":
        return (0, 0)
    elif TicTacToe[1][0] == TicTacToe[1][1] == TicTacToe[1][2] != " ":
        return (1, 0)
    elif TicTacToe[2][0] == TicTacToe[2][1] == TicTacToe[2][2] != " ":
        return (2, 0)
    else:
        return None

def check_columns():
    if TicTacToe[0][0] == TicTacToe[1][0] == TicTacToe[2][0] != " ":
        return (0, 0)
    elif TicTacToe[0][1] == TicTacToe[1][1] == TicTacToe[2][1] != " ":
        return (0, 1)
    elif TicTacToe[0][2] == TicTacToe[1][2] == TicTacToe[2][2] != " ":
        return (0, 2)
    else:
        return None

def check_diagonals():
    if TicTacToe[0][0] == TicTacToe[1][1] == TicTacToe[2][2] != " ":
        return (0, 0)
    elif TicTacToe[0][2] == TicTacToe[1][1] == TicTacToe[2][0] != " ":
        return (0, 2)
    else:
        return None
def checkDraw():
    row_index = 0
    while row_index < 3:
        if " " in TicTacToe[row_index]:
            return False  # there is an empty space, the game is not a draw
        row_index = row_index + 1

    return True  # all spaces are filled, the game is a draw

# Switch the current player
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


while True:
    displayBoard()
    # Get row input from the player
    row = int(input("Player " + current_player + " enter the row (1-3): ")) - 1

    # Get column input from the player
    col = int(input("Player " + current_player + " enter the column (1-3): ")) - 1
    # Check if the move is valid and update the board
    if 0 <= row < 3 and 0 <= col < 3 and TicTacToe[row][col] == " ":
        TicTacToe[row][col] = current_player
        # Check if the current player has won

        winner = checkWin()

        # If there is a winner or if it is a draw, display the board and end the game
        if winner:
            displayBoard()
            print("Player", winner, "wins!")
            break  # ends the game
        if checkDraw():
            displayBoard()
            print("It's a draw!")
            break

            # Switch to the other player for the next turn
        flip_player()
    else:
        print("Invalid move. Try again.")


    def placecounter():
         displayBoard()
     # Get row input from the player
    row = int(input("Player " + current_player + " enter the row (1-3): ")) - 1

     # Get column input from the player
 col = int(input("Player " + current_player + " enter the column (1-3): ")) - 1
    # Check if the move is valid and update the board
    if 0 <= row < 3 and 0 <= col < 3 and TicTacToe[row][col] == " ":
        TicTacToe[row][col] = current_player
        # Check if the current player has won

        winner = checkWin()

        # If there is a winner or if it is a draw, display the board and end the game
        if winner:
            displayBoard()
            print("Player", winner, "wins!")
            break  # ends the game
        if checkDraw():
            displayBoard()
            print("It's a draw!")
            break

            # Switch to the other player for the next turn
        flip_player()
    else:
        print("Invalid move. Try again.")
