import random
import tkinter

#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(call):

    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output

    # 1. Create random integer 1-3 to use as computer's play

    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated

    # 3. Determine the winner based on what the user chose and what the computer chose 
    #   Rock beats Scissors
    #   Paper beats Rock
    #   Scissors beats Paper
    #   It's a tie if the computer and user chose the same object

    # If the user wins, increase win by 1
    # Use the output label to write what the computer did and what the result was (win, loss, tie)


# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

window = tkinter.Tk()

#Variable to count the number of wins the user gets
win = 0


#START CODING HERE

# 1. Create 3 buttons for each option (rock, paper, scissors)

# 2. Create 2 labels for the result and the number of wins

# 3. Arrange the buttons and labels using grid

window.mainloop()
