#import libraries 
from tkinter import *
from tkinter import ttk
import math

#initiate list
calcList = []

#function to add calculations to string and update the calculator window
def calculation_String(num):
    global calcList
    #allows you to change answer to pos/neg by multiplying by negative one
    if num == '+/-':
        num = '*(-1)'
        #adds item to list and then updates label to be displayed
        calcList.append(str(num))
        calculationResults.configure(text = "".join(calcList))
    #else is for all other entries pos/neg needed to be changed to multiply by -1
    #updates the list and displays
    else:
        calcList.append(str(num))
        calculationResults.configure(text = "".join(calcList))

#function clears all entries and updates list to be empty and displays the list
def clear_List():
    global calcList
    calcList.clear()
    calculationResults.configure(text = "".join(calcList))

#function to remove last item entered
def clear_Last():
    #exception handling because if you .pop() list is empty and throws error
    try:
        global calcList
        calcList.pop()
        calculationResults.configure(text = "".join(calcList))
    except:
        calculationResults.configure(text = "".join(calcList))

#function when equals is pressed
def equal_Pressed():
    #exception is when eval() is not a valid equation it throws error so if its invalid display ERROR instead and clear the list to start agian
    try:
        global calcList
        equation = "".join(calcList)
        equation = str(eval(equation))
        calcList.clear()
        calcList.append(equation)
        calculationResults.configure(text = "".join(calcList))
    except:
        calcList.clear()
        calcList.append('ERROR')
        calculationResults.configure(text = "".join(calcList))
        calcList.clear()

#initializes window and sets attributes   
calculator = Tk()
calculator.geometry('455x550')
calculator.title('Calculator')
calculator.configure(bg = '#4e4f52')

#sets buttons and attributes and passes number to the calculations function
zero = Button(calculator, text = '0', width = 23, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String(0))
zero.place(x = 25, y = 450)
decimal = Button(calculator, text= '.', width = 10, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String('.'))
decimal.place(x = 235, y = 450)
one = Button(calculator, text = '1', width = 10, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String(1))
one.place(x = 25, y = 380)
two = Button(calculator, text = '2', width = 10, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String(2))
two.place(x = 130, y = 380)
three = Button(calculator, text = '3', width = 10, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String(3))
three.place(x = 235, y = 380)
four = Button(calculator, text = '4', width = 10, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String(4))
four.place(x = 25, y = 310)
five = Button(calculator, text = '5', width = 10, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String(4))
five.place(x = 130, y = 310)
six = Button(calculator, text = '6', width = 10, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String(6))
six.place(x = 235, y = 310)
seven = Button(calculator, text = '7', width = 10, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String(7))
seven.place(x = 25, y = 240)
eight = Button(calculator, text = '8', width = 10, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String(8))
eight.place(x = 130, y = 240)
nine = Button(calculator, text = '9', width = 10, height = 2, bg = '#36373a', fg = '#edf7fc', command = lambda: calculation_String(9))
nine.place(x = 235, y = 240)
posNeg = Button(calculator, text = '+/-', width = 10, height = 2, bg = '#edf7fc', command = lambda: calculation_String('+/-'))
posNeg.place(x = 130, y = 170)

#sets buttons and passes the function to clear all or clear entry
reset = Button(calculator, text = 'A/C', width = 10, height = 2, bg = '#edf7fc', command = lambda: clear_List())
reset.place(x = 25, y = 170)
clear = Button(calculator, text = 'CE', width = 10, height = 2, bg = '#edf7fc', command = lambda: clear_Last())
clear.place(x = 235, y = 170)

#sets operator buttons and passes it to calculation function
divide = Button(calculator, text = '/', width = 10, height = 2, bg = '#ff0259', fg = '#edf7fc', command = lambda: calculation_String('/'))
divide.place(x = 340, y = 170)
multi = Button(calculator, text = '*', width = 10, height = 2, bg = '#ff0259', fg = '#edf7fc', command = lambda: calculation_String('*'))
multi.place(x = 340, y = 240)
minus = Button(calculator, text = '-', width = 10, height = 2, bg = '#ff0259', fg = '#edf7fc', command = lambda: calculation_String('-'))
minus.place(x = 340, y = 310)
plus = Button(calculator, text = '+', width = 10, height = 2, bg = '#ff0259', fg = '#edf7fc', command = lambda: calculation_String('+'))
plus.place(x = 340, y = 380)

#sets equal button and passes it to the equal pressed function
equalSign = Button(calculator, text= '=', width = 10, height = 2, bg = '#ff0259', fg = '#edf7fc', command = lambda: equal_Pressed())
equalSign.place(x = 340, y = 450)

#sets the calculation label to display to user
calculationResults = Label(calculator, text = '', width = 50, height = 3, relief = 'sunken', bg = '#edf7fc', anchor = 'e')
calculationResults.place(x = 25, y = 60)

#keeps it running
calculator.mainloop()


