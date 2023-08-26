from tkinter import *
import math
import subprocess


def click(value):
    ex = entryField.get() 
    answer = ''

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]  
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

        elif value == 'sinh':
            answer = math.sinh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8': 
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(eval(ex))

        elif value == chr(247):  
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mul(a, b):
    return a * b
def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def lcm(a,b):
    l=math.lcm(a,b)
    return l

def hcf(a,b):
    h=math.gcd(a,b)
    return h

operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'LCM':lcm , 'HCF':hcf,
            'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod }


def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l




root = Tk()
root.title('Scientific Calculator')
root.config(bg='#171717')
root.geometry('680x486+100+100')
root.resizable(0,0)

# creating logo for the calculator
photo = PhotoImage(file='logo1.png')
root.iconphoto(False,photo)


entryField = Entry(root, font=('arial', 20, 'bold'), bg='#484848', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)


# creating button list with the help of for loop
button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue = 1
columnvalue = 0
for i in button_text_list:

    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='#171717', fg='#9BD260',
                    font=('arial', 18, 'bold'), activebackground='red', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

# code for history button
def history():
    
    f=open("history.txt","a")
    f.write(entryField.get())
    f.write("\n")
    f.close()
    entryField.delete(0,END)

    f=open("history.txt","r")
    data=f.read()
    entryField.insert(0,data)

    f.close()

button_history = Button(root, text="History", command=history,fg='#9BD260',bg='#171717',font=('arial', 8, 'bold'),relief=SUNKEN)
button_history.grid(row=9, column=0, columnspan=2, pady=1)

# Code for rate us
def run_command():
    subprocess.call(['python', 'D:\\Amin notes\\Sem-2\\adp\\project\\rateus.py'])

button_rateus = Button(root, text="Rate Us",fg='#9BD260',command= run_command,bg='#171717',font=('arial', 8, 'bold'),relief=SUNKEN)
button_rateus.grid(row=0, column=7, columnspan=2, pady=1)

# code for clear button
def clear_history():

    open("history.txt","w").close()

button_clear = Button(root, text="Clear History",fg='#9BD260',bg='#171717',font=('arial', 8, 'bold'),relief=SUNKEN, command=clear_history)
button_clear.grid(row=9, column=2, columnspan=2, pady=1)



root.mainloop()     