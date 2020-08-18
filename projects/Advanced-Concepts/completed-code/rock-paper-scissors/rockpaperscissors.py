import random
import tkinter

def get_winner(call):
    #global wins, win, output
    comp_call = random.randint(1,3)
    print(comp_call)
    if comp_call == 1:
        throw = "rock"
    elif comp_call == 2:
        throw = "scissors"
    else:
        throw = "paper"

    if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissors") or (throw == "scissors" and call == "rock"):
        result = "You won!"
        win+=1
    elif throw == call:
        result = "It's a draw"
    else:
        result = "You lost!"

    output.config(text=f"Computer did: {throw} \n {result}")
    wins.config(text=f"Wins: {win}")


def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

window = tkinter.Tk()

win = 0

scissors = tkinter.Button(window, text = "Scissors", bg = "#ff9999", padx=10, pady=5, command=pass_s, width=20)
rock = tkinter.Button(window, text = "Rock", bg = "#80ff80", padx=10, pady=5, command=pass_r, width=20)
paper = tkinter.Button(window, text = "Paper", bg = "#3399ff", padx=10, pady=5, command=pass_p, width=20)
output = tkinter.Label(window, width=20, fg = "red", text="What's your call?")
wins = tkinter.Label(window, width = 20, fg="black", text="Wins:0")

scissors.grid(row=0, column=0)
rock.grid(row=0, column=1)
paper.grid(row=0, column=2)
output.grid(row=1, column=0)
wins.grid(row=1, column=2)
window.mainloop()
