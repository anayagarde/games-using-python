from tkinter import *
import random

# Global Variable
score_comp = 0
score_player = 0
count = 0
computer = ''
# 1 - Rock, 2 - Paper, 3 - Scissor

def player(y):
    global score_comp
    global score_player
    global count
    global computer
    x = comp()
    count = count+1
    if count <= 5:  # Game has 5 chances
        data1 = 'ROUND ' + str(count)
        if x == 1:  # Rock chosen by Comp
            if y == 1:  # Player chose Rock
                data1 += '\nYou and Computer both chose Rock\nTIE!'
            elif y == 2:  # Player chose Paper
                data1 += '\nComputer chose Rock\nYou get a point! :)'
                score_player += 1
            elif y == 3:  # Player chose Scissor
                data1 += '\nComputer chose Rock\nComputer gets a point!'
                score_comp += 1

        if x == 2:  # Paper chosen by Comp
            if y == 1:  # Player chose Rock
                data1 += '\nComputer chose Paper\nComputer gets a point!'
                score_comp += 1
            elif y == 2:  # Player chose Paper
                data1 += '\nYou and Computer both chose Paper\nTIE!'
            elif y == 3:  # Player chose Scissor
                data1 += '\nComputer chose paper\nYou get a point! :)'
                score_player += 1

        if x == 3:  # Scissor chosen by Comp
            if y == 1:  # Player chose Rock
                data1 += '\nComputer chose Scissor\nYou get a point! :)'
                score_player += 1
            elif y == 2:  # Player chose Paper
                data1 += '\nComputer chose Scissor\nComputer gets a point!'
                score_comp += 1
            elif y == 3:  # Player chose Scissor
                data1 += '\nYou and Computer both chose Scissor\nTIE!'
        value1.set(data1)
        computer = 'Computer Score : ' + str(score_comp)
        computer += '\nYour Score : ' + str(score_player)
        value2.set(computer)
    else:
        value2.set(computer)
        if score_comp > score_player:
            d = 'COMPUTER WINS !'
        elif score_comp < score_player:
            d = 'YOU WIN !'
        else:
            d = 'Tie !'
        d += '\nNew Game?\nStart Playing Again '
        value1.set(d)
        clear()

def clear():
    global score_player
    global score_comp
    global count

    score_comp = 0
    score_player = 0
    count = 0

def comp():
    c = random.randint(1, 3)
    print(c)
    return c


root = Tk()
root.title('Rock Paper Scissor')
root.geometry('400x450')

# 2 Labels

#Label 1
value1 = StringVar()
label1 = Label(root,text = "Label",anchor = CENTER,font = "Helvetica 15 bold", textvariable = value1,background = '#F9F3F9')
label1.pack(expand = True, fill = 'both')

#Label 2
value2 = StringVar()
label2 = Label(root,text = "Label",anchor = CENTER,font = "Helvetica 13 bold", textvariable = value2,background = '#F9F3F9')
label2.pack(expand = True, fill = 'both')



# 3 Frames and each Frame has 1 Button
f1 = Frame(root,bg = 'black')
f1.pack(expand = True, fill = 'both')

f2 = Frame(root,bg = 'black')
f2.pack(expand = True, fill = 'both')

f3 = Frame(root,bg = 'black')
f3.pack(expand = True, fill = 'both')



#3 Buttons
button1 = Button(f1,text = 'Rock',font = "Calibri 15 bold",bg = '#E8C6EB',command = lambda: player(1),border = 0,)
button1.pack(side = LEFT,expand = True,fill='both')

button2 = Button(f2,text = 'Paper',font = "Calibri 15 bold",bg = '#E5B2EB',command = lambda: player(2),border = 0,)
button2.pack(side = LEFT,expand = True,fill='both')

button3 = Button(f3,text = 'Scissor',font = "Calibri 15 bold",bg = '#E0A2E4',command = lambda: player(3),border = 0)
button3.pack(side = LEFT,expand = True,fill='both')

root.mainloop()