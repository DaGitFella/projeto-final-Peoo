from tkinter import *


all_values = ''
python_values = ''

def display_values(value, expression):
    
    convert = {
        'x':'*',
        '÷':'/'    
    }
    
    global all_values, python_values
    
    all_values = all_values + str(value)
    
    if value in convert:
        python_values += str(convert[value])
    else:
        python_values += str(value)  
    
    expression.set(all_values)
    
def clear(expression, screen):
    global all_values, python_values
    all_values, python_values = "", ""
    expression.set("")
    screen.set("")
    
def delete(expression, screen):
    global all_values, python_values
    all_values, python_values = all_values[:-1], python_values[:-1]
    expression.set(all_values)
    screen.set("")
    
def calculate(screen):
    try:
        result = round(eval(python_values), 5)
    except ZeroDivisionError:
        screen.set('∞')
    screen.set(result)