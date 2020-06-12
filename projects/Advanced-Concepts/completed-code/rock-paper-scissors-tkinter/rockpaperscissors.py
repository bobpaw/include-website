#!/usr/bin/python3
from random import *
from tkinter import *
from PIL import Image
from PIL import ImageTk

score = 0

#choice section
def userChoiceRock():
    userChoice = "rock"
    turn(userChoice)
    userImage.configure(image = rockImage)

def userChoicePaper():
    userChoice = "paper"
    turn(userChoice)
    userImage.configure(image = paperImage)

def userChoiceScissors():
    userChoice = "scissors"
    turn(userChoice)
    userImage.configure(image = scissorsImage)

#gameplay setion
def turn(userChoice):
    global score
    opponent = ['rock', 'paper', 'scissors']
    opponentChoice = opponent[randint(0,2)]

    if(opponentChoice == 'rock'):
        opponentImage.configure(image = rockImage)
    elif(opponentChoice == 'paper'):
        opponentImage.configure(image = paperImage)
    else:
        opponentImage.configure(image = scissorsImage)

    if(opponentChoice == userChoice):
        turnResult.configure(text = "It's a draw.", fg = "gray")
        compare.configure(text = "=")
        scoreBoard.configure(text = "You've won "+ str(score) + " times", fg = "grey")
    elif((opponentChoice == 'rock' and userChoice == 'scissors') or (opponentChoice == 'paper' and userChoice == 'rock') or (opponentChoice == 'scissors' and userChoice == 'paper')):
        turnResult.configure(text = "You are defeated!", fg = "red")
        compare.configure(text="<")
        scoreBoard.configure(text = "You've won "+ str(score) + " times", fg = "grey")
    else:
        turnResult.configure(text = "You win!", fg = "green")
        compare.configure(text = ">")
        score+=1
        scoreBoard.configure(text = "You've won "+ str(score) + " times", fg = "grey")

#main program
mainWindow = Tk()
mainWindow.title("Rock-Paper-Scissors by Nrehtron")
rockButton = Button(mainWindow, width = 20, text = "ROCK!", justify = CENTER, command = userChoiceRock, activebackground = 'black', activeforeground = 'white')
paperButton = Button(mainWindow, width = 20, text = "PAPER!", justify = CENTER, command = userChoicePaper, activebackground = 'black', activeforeground = 'white')
scissorsButton = Button(mainWindow, width = 20, text = "SCISSORS!", justify = CENTER, command = userChoiceScissors, activebackground = 'black', activeforeground = 'white')

#images
width = 100
height = 100
width2 = 300
height2 = 300
rockImage2 = Image.open("nrehtron/rps/rock.png")
rockImage2 = rockImage2.resize((width2,height2), Image.ANTIALIAS)
rockImage = ImageTk.PhotoImage(rockImage2)


rockIcon2 = Image.open("nrehtron/rps/rock.png")
rockIcon2 = rockIcon2.resize((width,height), Image.ANTIALIAS)
rockIcon = ImageTk.PhotoImage(rockIcon2)
rock = Label(image = rockIcon)
rock.image = rockIcon

paperImage2 = Image.open("nrehtron/rps/paper.png")
paperImage2 = paperImage2.resize((width2,height2), Image.ANTIALIAS)
paperImage = ImageTk.PhotoImage(paperImage2)

paperIcon2 = Image.open("nrehtron/rps/paper.png")
paperIcon2 = paperIcon2.resize((width,height), Image.ANTIALIAS)
paperIcon = ImageTk.PhotoImage(paperIcon2)
paper = Label(image = paperIcon)
paper.image = paperIcon

scissorsImage2 = Image.open("nrehtron/rps/scissors.png")
scissorsImage2 = scissorsImage2.resize((width2,height2), Image.ANTIALIAS)
scissorsImage = ImageTk.PhotoImage(scissorsImage2)

scissorsIcon2 = Image.open("nrehtron/rps/scissors.png")
scissorsIcon2 = scissorsIcon2.resize((width,height), Image.ANTIALIAS)
scissorsIcon = ImageTk.PhotoImage(scissorsIcon2)
scissors = Label(image = scissorsIcon)
scissors.image = scissorsIcon

userImage = Label()
compare = Label(mainWindow, justify = CENTER, font = ("Helvetica", 30) )
opponentImage = Label()
turnResult = Label(mainWindow, width = 20, justify = CENTER, font = ("Helvetica", 20))
scoreBoard = Label(mainWindow, width = 20, justify = CENTER, font = ("Helvetica", 20))

    

#Tk GUI grid
rockButton.grid(row = 2, column = 1)
paperButton.grid(row = 2, column = 2)
scissorsButton.grid(row = 2, column = 3)
rock.grid(row = 3, column = 1)
paper.grid(row = 3, column = 2)
scissors.grid(row = 3, column = 3)
userImage.grid(row = 4, column = 1)
compare.grid(row = 4, column = 2)
opponentImage.grid(row = 4, column = 3)
turnResult.grid(row = 5, column = 2)
scoreBoard.grid(row = 6, column = 2)

#mainloop
mainWindow.mainloop()
