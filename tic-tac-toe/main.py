# -----TO DO------
# display board
# game
# handle turn
# check for win
  # checking row
  # checking column
  # checking diagonals
# check for tie
# flip player


#----------GLOBAL VARIABLES--------

#Game Board
board =["-","-","-",
        "-","-","-",
        "-","-","-"]

game_still_going = True  #false when game is over
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
   print("GAME BOARD")
   display_board()
   print("--------------------------")

   while game_still_going:

       handle_turn(current_player)  #give turn to player
       check_if_game_over()  #check for whether game is over
       flip_player()  #flip the turn from X to O

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
    position = input("Choose a position from 1-9:")
    valid = False
    while not valid:

      while position not in ["1","2","3","4","5","6","7","8","9"]:
         position = input("Choose a position from 1-9:")

      position = int(position) - 1  # since list starts from 0

      if board[position] == "-":
          valid = True
      else:
         print("You can't go there.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #set global variables
    global winner
    #check rows
    row_winner = checking_rows()
    #check columns
    column_winner = checking_columns()
    #check diagonals
    diagonal_winner = checking_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a winner
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    return

def checking_rows():
    #set global variables
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:  # game finished since some row have all equal
        game_still_going = False
    #return winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def checking_columns():
    # set global variables
    global game_still_going

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:  # game finished since some row have all equal
        game_still_going = False
    # return winner X or O
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]


def checking_diagonals():
    # set global variables
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2 :  # game finished since some row have all equal
        game_still_going = False
    # return winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()