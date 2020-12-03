#------- TO DO -----------
# 1. Game function
# 2. Win function
# 3. User function
# 4. Computer function

#-----Packages----
import random

#----Global Variables-----
game_going = True
winner = None
user_points = 0
comp_points = 0
x = None
y = None
player = None

#-------Game----------
def game():
    global winner
    global game_going
    global player
    print("\t ROCK PAPER SCISSOR GAME ")
    player = input("Enter your name: ")
    for i in range(0 , 5):
      game_going = True
      print("\n\tROUND ",(i+1))
      while game_going:
         check_winner()
         display_points()

    if user_points > comp_points:
        winner = player
        print("\n----------------------")
        print(winner + " WON!")
        print("----------------------")
    elif comp_points > user_points:
        winner = "COMPUTER"
        print("\n----------------------")
        print(winner + " WON!")
        print("----------------------")
    else:
        print("\n----------------------")
        print("It's a tie !")
        print("----------------------")



def display_points():
    global user_points
    global comp_points
    print("\n----------POINTS------------")
    print(player + "'s POINTS : ", user_points)
    print("COMPUTER POINTS : ", comp_points)



def user_ask():
    print("\n****************")
    print(player+"'s TURN")
    print("****************")
    print("1.Stone\n2.Paper\n3.Scissor")

    ans = input("Select option from 1-3: ")
    while ans not in ["1", "2", "3"]:
        ans = input("Select option from 1-3: ")
    ans = int(ans)

    if ans == 1:
        print("\n"+player+" chose Stone")
    elif ans == 2:
        print("\n"+player+" chose Paper")
    elif ans == 3:
        print("\n"+player+" chose Scissor")
    return ans

def comp_ask():
    print("\n****************")
    print("COMPUTER'S TURN")
    print("****************")
    ans = random.randint(1, 3)
    if ans == 1:
        print("\nComputer chose Stone")
    elif ans == 2:
        print("\nComputer chose Paper")
    elif ans == 3:
        print("\nComputer chose Scissor")
    return ans

def check_winner():
    global x
    global y
    global game_going
    global user_points
    global comp_points
    x = user_ask()
    y = comp_ask()
    if x == y:
        print("\nPlay again!")
        game_going = True
    elif (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
        comp_points = comp_points + 1
        game_going = False
    else:  # (x == 2 and y == 1) or (x == 3 and y == 2) or (x == 1 and y == 3):
        user_points = user_points + 1
        game_going = False

game()
