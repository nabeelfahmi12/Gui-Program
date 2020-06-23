import math
from tkinter import *

Cal: Tk = Tk()
Cal.title("Calculator")


def click_but(number) :
    current = Input.get()
    Input.delete(0 , END)
    Input.insert(0 , str(current) + str(number))


def click_clear() :
    Input.delete(0 , END)


def add() :
    first_number = Input.get()
    global f_num
    global Math
    Math = "addition"
    f_num = int(first_number)
    Input.delete(0 , END)



def subtract() :
    first_number = Input.get()
    global f_num
    global Math
    Math = "subtraction"
    f_num = int(first_number)
    Input.delete(0 , END)


def multiply() :
    first_number = Input.get()
    global f_num
    global Math
    Math = "multiplication"
    f_num = int(first_number)
    Input.delete(0 , END)


def divide() :
    first_number = Input.get()
    global f_num
    global Math
    Math = "division"
    f_num = int(first_number)
    Input.delete(0 , END)


def sqare_root() :
    first_number = Input.get()
    global f_num
    global Math
    Math = "Sqare_root"
    f_num = int(first_number)
    Sqrt = math.sqrt(f_num)
    Input.delete(0 , END)
    Input.insert(0 , Sqrt)



def Power() :
    first_number = Input.get()
    global f_num
    global Math
    Math = "Power"
    f_num = int(first_number)
    Input.delete(0 , END)

 

def equals() :
    second_number = Input.get()
    Input.delete(0 , END)

    if Math == "addition" :
        Input.insert(0 , f_num + int(second_number))

    if Math == "subtraction" :
        Input.insert(0 , f_num - int(second_number))

    if Math == "multiplication" :
        Input.insert(0 , f_num * int(second_number))

    if Math == "division" :
        Input.insert(0 , f_num / int(second_number))
    if Math == "Power" :
        Input.insert(0, f_num ** int(second_number))


Input = Entry(Cal , width=40 , borderwidth=5,)
Input.grid(row=0 , columnspan=3 , padx=20 , pady=20)


button1 = Button(Cal , text="1" , padx=40 , pady=20 , command=lambda : click_but(1))
button2 = Button(Cal , text="2" , padx=40 , pady=20 , command=lambda : click_but(2))
button3 = Button(Cal , text="3" , padx=40 , pady=20 , command=lambda : click_but(3))
button4 = Button(Cal , text="4" , padx=40 , pady=20 , command=lambda : click_but(4))
button5 = Button(Cal , text="5" , padx=40 , pady=20 , command=lambda : click_but(5))
button6 = Button(Cal , text="6" , padx=40 , pady=20 , command=lambda : click_but(6))
button7 = Button(Cal , text="7" , padx=40 , pady=20 , command=lambda : click_but(7))
button8 = Button(Cal , text="8" , padx=40 , pady=20 , command=lambda : click_but(8))
button9 = Button(Cal , text="9" , padx=40 , pady=20 , command=lambda : click_but(9))
button0 = Button(Cal , text="0" , padx=40 , pady=20 , command=lambda : click_but(0))
button_add = Button(Cal , text="+" , padx=40 , pady=20 , command=add)
button_equal = Button(Cal , text="=" , padx=40 , pady=20 , command=equals)
button_sub = Button(Cal , text="-" , padx=40 , pady=20 , command=subtract)
button_mul = Button(Cal , text="*" , padx=40 , pady=20 , command=multiply)
button_div = Button(Cal , text="/" , padx=40 , pady=20 , command=divide)
button_power = Button(Cal , text="^" , padx=40 , pady=20 , command=Power)
button_Sqrt = Button(Cal , text="√" , padx=40 , pady=20 , command=sqare_root)
button_clear = Button(Cal , text="C" , padx=40 , pady=20 , command=click_clear)

button1.grid(column=0 , row=4)
button2.grid(row=4 , column=1)
button3.grid(row=4 , column=2)
button4.grid(row=3 , column=2)
button5.grid(row=3 , column=1)
button6.grid(row=3 , column=0)
button7.grid(row=2 , column=2)
button8.grid(row=2 , column=1)
button9.grid(row=2 , column=0)
button0.grid(row=5 , column=0)
button_add.grid(row=5 , column=1)
button_equal.grid(row=6 , column=2)
button_sub.grid(row=5 , column=2)
button_mul.grid(row=6 , column=0)
button_div.grid(row=6 , column=1)
button_power.grid(row=1 , column=1)
button_Sqrt.grid(row=1 , column=0)
button_clear.grid(row=1 , column=2)

Cal.mainloop()
