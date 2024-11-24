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
    # The line def button_clear(): This is defining a function named button_clear. When this function is called,
    # a block of code indented underneath it will be executed; however, this depends on the implementation inside the function.
    e.delete(0, END)
    # The line e.delete(0, END) deletes the text inside the Entry widget e,
    # starting from index 0 (the beginning of the text) to END (the end of the text), effectively clearing the entire input field.

# 5 Document what the following lines of code do here
def button_operator(operator):
    first_number = e.get()
    # Gets the number currently in the entry field
    global f_num
    # Declares a global variable to store the first number for later use
    global num_operator
    # Declares a global variable to store the chosen operator (e.g., +, -, *, /)
    f_num = int(first_number)
    # Converts the first number to an integer and store it in 'f_num'
    num_operator = operator
    # Stores the operator in 'num_operator' to be used in the calculation
    e.delete(0, END)
    # Clear the entry field to allow the user to enter the second number

# 6 Document what the following lines of code do here

# you might want to consider adding documentation on a line by line basis since
# this is a critical function for the program
def button_equal():
    # This line of code defines a function named button_equal which should execute a certain action upon calling, for example,
    # handling the logic of the equal button in a calculator.
    second_number = e.get()
    # The code second_number = e.get() retrieves the current value from a user interface element
    # like an entry field or text box represented by 'e' and assigns that value to the variable second_number.
    e.delete(0, END)
    # The line of code e.delete(0, END) removes all the text from the user interface element e,
    # starting from the first character (index 0) up to the end of the text, effectively clearing the entry field or text box.
    if num_operator == '+':
        # if num_operator == '+': The said line is a conditional statement that checks the variable num_operator
        # whether it is equal to the string '+'.
        e.insert(0, f_num + int(second_number))
        # This line of code inserts the result of an addition into an interface element e:
        # usually an entry field in a GUI, using e.insert(0, f_num + int(second_number)).
    elif num_operator == '*':
        # The line elif num_operator == '*': represents a conditional structure where
        # the variable num_operator is being tested for equality to the string '*'. Normally, this comparison would be done 
        # within a program that selects an arithmetic operation to perform based on user input or some set of predefined choices.
        e.insert(0, f_num * int(second_number))
        # This line of code inserts the result of a multiplication operation into a GUI entry field e
        # e.insert(0, f_num * int(second_number)).
    elif num_operator == '/':
        # Line elseif num_operator == '/': is a part of a conditional structure; that normally
        # can be found inside a function handling some arithmetic operation in
        # a calculator application.
        # This line specifically checks if the current operator-holding variable num_operator is a division operator /.
        e.insert(0, f_num / int(second_number))
        # The line e.insert(0, f_num / int(second_number)) is responsible for displaying the result of a division operation
        # in a GUI application such as a calculator.
    elif num_operator == '-':
        # The line elif num_operator == '-': is another conditional statement that checks whether the operator chosen by the user is the
        # minus operator -. This line would normally be part of a larger conditional structure within a function
        #  aimed at performing arithmetic operations in an application, such as a calculator.
        e.insert(0, f_num - int(second_number))
        # This line, e.insert(0, f_num - int(second_number)), is part of the logic that performs a subtraction operation in some GUI
        # application-a calculator.
    else:
        # The else: statement in Python is used to complete an if.elif chain of conditional statements and defines the block of code that
        # will be executed when all the previous conditions are false.
        e.insert(0, "Invalid!!!")
        #The line e.insert(0, "Invalid!!!") is a specific instruction usually appearing within user interface contexts, such as in
        # a graphical calculator application implemented using Tkinter in Python. 
        # It shows an error message for the user when any invalid input or operation has been detected.

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
# Create a button for the "+" operator. When clicked, it calls `button_operator("+")`.
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
# Create the "=" button. It spans more space (`padx=79`) and calls the `button_equal()` function.
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)
# Create a "Clear" button to reset the entry field when clicked.

# 8 Document what the following lines of code do here

# See the description of a Lambda function above
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
# This is a line of code that creates a button labeled "/" in the Tkinter GUI application with specified padding, 
# and when clicked it calls the function button_operator with the argument "/".
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
# It makes this line of code create a button labeled "-",
#  having specified padding, which calls a function button_operator with an argument "-" upon clicking.
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))
# This is a line of code that creates a button labeled "/" in the Tkinter GUI application with specified padding, 
# and when clicked it calls the function button_operator with the argument "/".

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
