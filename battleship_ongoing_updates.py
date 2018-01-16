from random import randint

board = []
#create a 10x10 row of "O"'s
for x in range(0, 10):
    board.append(["O"] * 10)
#separate the rows of "O"'s by a space
def print_board(board):
    for row in board:
        print " ".join(row)

#selects a random row number in positions 0-(length of the board-1)
def random_row(board):
    return randint(0, len(board) - 1)
#selects a random column number in positions 0-(Length of the board-1)
def random_col(board):
    return randint(0, len(board) - 1)
#assigns a random row and column for the ship's placement
ship_row1 = random_row(board)
ship_col1 = random_col(board)
ship_row2 = random_row(board)
ship_col2 = random_col(board)
if ship_row2==ship_row1 and ship_col2==ship_col1:
    ship_row2 = random_row(board)
    ship_col2 = random_col(board)
ship_row3 = random_row(board)
ship_col3 = random_col(board)
if (ship_row3==ship_row1 and ship_col3==ship_col1) or \
(ship_row3==ship_row2 and ship_col3==ship_col2):
    ship_row3 = random_row(board)
    ship_col3 = random_col(board)
#shows the battleship location-used in testing
#print ship_row
#print ship_col
#change the input from the guessed row and column into a integer and assign them
#to the two variables. Gives the user 4 guesses.
for turn in range(4):
    print "Turn", turn+1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
#alternative code for 1st elif statement
#elif (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
    if (guess_row==ship_row1 and guess_col==ship_col1) or \
    (guess_row==ship_row2 and guess_col==ship_col2) or \
    (guess_row==ship_row3 and guess_col==ship_col3):
        print "Congratulations! You sank my battleship!"
        break   #exits the loop after a correct guess
    elif guess_row not in range(10) or guess_col not in range(10):
        print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col]=="X":
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col]="X"
        if turn==3:
            print "Game Over"
#show the board
    print_board(board)
