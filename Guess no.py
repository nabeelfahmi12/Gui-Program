# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
from tkinter import *
import random
import math

Gess = Tk()
Gess.title("Gess No")

# helper function to start and restart the game
def new_game(fl=0) :
    # initialize global variables used in your code here
    # remove this when you add your code
    global secret_number
    global f
    f = fl
    global n
    if f == 0 :
        secret_number = random.randrange(0 , 100)
        n = math.ceil(math.log(101 , 2))
        print("range(0,100)")
    else :
        secret_number = random.randrange(0 , 1000)
        n = math.ceil(math.log(1001 , 2))
        print("range(0,1000)")
    global c
    c = 0

    print("remain:") , n
    # print "s:", secret_number


# define event handlers for control panel
def range100() :
    # button that changes the range to [0,100) and starts a new game
    print('\n')
    new_game()

    # print "remain:", n
    # print "s:", secret_number


def range1000() :
    # button that changes the range to [0,1000) and starts a new game
    print('\n')
    new_game(1)
    # print "s:", secret_number


def input_guess(gues) :
    # main game logic goes here
    global n
    global c
    guesss = inp.get()
    guess = int(guesss)
    if c < n :
        global secret_number
        c = c + 1
        n_guess = int(guess)
        print("Guess was" , n_guess)
        if secret_number < n_guess :
            print("Lower")
            print("remain:" , n - c)
            print('\n')
        if secret_number > n_guess :
            print("Higher")
            print("remain:" , n - c)
            print('\n')
        if secret_number == n_guess :
            print("Correct")
            print("remain:" , n - c)
            print("You win! start new game!")
            print('\n')
            new_game(f)

        if c == n :
            print("You run out ot times! start new game! correct is" , secret_number)
            print('\n')
            new_game(f)


# create frame
frame = LabelFrame(Gess, text='Guess the number!' , padx=200 ,pady= 200).grid()
# register event handlers for control elements and start frame
inp = Entry(frame, text='My Guess' ,width=45 , borderwidth=5,)
inp.bind("<Return>",input_guess)
inp.grid(row=0 , columnspan=3)
range100 = Button(frame, text='range100' , command=range100 , padx=20).grid(row=1, column=0)
range1000 = Button(frame ,text='range1000' , command=range1000 , pady=10).grid(row=1, column=1)
# call new_game
new_game()

Gess.mainloop()