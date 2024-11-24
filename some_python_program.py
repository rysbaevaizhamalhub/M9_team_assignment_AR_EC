# Aizhamal, Emmanuel 
# Nov 19, 2024
# Program description goes here
# Updated on:
# Updated by:
#
#
# 1 Document what the following lines of code do here
from tkinter import *
# Import everything from the tkinter module, which allows us to create GUI applications
root = Tk()
# Create the main application window where all components will appear
root.title("Simple Calculator")
# Set the title of the main window to "Simple Calculator," displayed at the top of the window

# 2 Document what the following lines of code do here
e = Entry(root, width=35, borderwidth=5)
# The line e = Entry(root, width=35, borderwidth=5) creates an Entry widget of width 35 characters
# and border width 5 pixels, placing it inside the parent widget root.

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# The line e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) places the Entry widget e in the grid
# at the position of the 0th row and 0th column, spans it across 3 columns, and adds padding on all sides of 10 pixels.

# 3 Document what the following lines of code do here
def button_click(number):
    current = e.get()
    # Gets the text currently displayed in the entry field
    e.delete(0, END)
    # Clears the entry field to prepare for new input
    e.insert(0, str(current) + str(number))
    # Appends the clicked number to the current text and display it in the entry field

# 4 Document what the following lines of code do here
def button_clear():
    e.delete(0, END)

# 5 Document what the following lines of code do here
def button_operator(operator):
    first_number = e.get()
    global f_num
    global num_operator
    f_num = int(first_number)
    num_operator = operator
    e.delete(0, END)

# 6 Document what the following lines of code do here

# you might want to consider adding documentation on a line by line basis since
# this is a critical function for the program
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if num_operator == '+':
        e.insert(0, f_num + int(second_number))
    elif num_operator == '*':
        e.insert(0, f_num * int(second_number))
    elif num_operator == '/':
        e.insert(0, f_num / int(second_number))
    elif num_operator == '-':
        e.insert(0, f_num - int(second_number))
    else:
        e.insert(0, "Invalid!!!")

# 7 Document what the following lines of code do here
#
# NOTE: We did not cover Lambda functins in class. A Lambda Function 
# in Python programming is an anonymous function
# or a function having no name. It is a small and restricted function 
# having no more than one line. In the case below, the Lambda function code
# is calling the code/function button_click() with the numbers 0-9 as the 
# parameter. Just like a normal function, a Lambda function can have multiple
# arguments with one expression. 

button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# 8 Document what the following lines of code do here

# See the description of a Lambda function above
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# 9 Document what the following lines of code do here

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# 10 Document what the following line of code do here

root.mainloop()
