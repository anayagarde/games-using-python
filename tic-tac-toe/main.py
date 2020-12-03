# -----LIST TO DO------
# Board display
# game
# handle turn
# check for win
  # checking row
  # checking column
  # checking diagonals
# check for tie
# flip player


#----------GLOBAL VARIABLES--------

# Our Game Board
board =["-","-","-",
        "-","-","-",
        "-","-","-"]

game_going = True  #false when game is over
winner = None
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
def display_position():
    print("1"+" | "+ "2" + " | "+"3")
    print("4" + " | " + "5" + " | " + "6" )
    print("7" + " | " + "8" + " | " + "9" )

#---------Play game Tic Tac Toe-----------

def play_game():

   global winner
   # Display initial Board
   print("--------------------------")
   print("POSITIONS ON BOARD")
   display_position()
   print("--------------------------")
   print("BOARD")
   display_board()
   print("--------------------------")

   while game_going:
       handle_turn(current_player)  #give turn to player
       game_over()  #check for whether game is over
       change_player()  #flip the turn from X to O

    #game has ended
   if winner == "X" or winner == "O":
       print("----------------------")
       print("Yay "+winner + " WON!")
       print("----------------------")

   elif winner == None:
       print("---------------------")
       print("Oops ! It's a Tie.")
       print("---------------------")



def handle_turn(player):

    print(player + "'s Turn")
    pos = input("Choose a position from 1-9:")
    valid = False
    while not valid:

      while pos not in ["1","2","3","4","5","6","7","8","9"]:
         pos = input("Choose a position from 1-9:")

      pos = int(pos) - 1  # since list starts from 0

      if board[pos] == "-":
          valid = True
      else:
         print("You can't go there.")

    board[pos] = player
    display_board()

def game_over():
    winner_fn()
    tie()

def winner_fn():
    global winner
    row_winner = rows() #check rows
    column_winner = columns() #check columns
    diagonal_winner = diagonals() #check diagonals
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # No win
        winner = None
    return

def rows():
    global game_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:  # game finished since some row have all equal
        game_going = False
    #return winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def columns():
    global game_going

    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:  # game finished since some row have all equal
        game_going = False
    # return winner X or O
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]


def diagonals():
    # set global variables
    global game_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2 :  # game finished since some row have all equal
        game_going = False
    # return winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]


def tie():
    global game_going
    if "-" not in board:
        game_going = False


def change_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()