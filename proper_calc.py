from tkinter import *
from tkinter import font
from numbers import Number
import operator
import re

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)

        self.ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }
        
        self.UserIn = StringVar();
        self.UserIn.set("")
        self.task = "" # a value that is used to get the final value which will be displayed
        self.result = 0
        self.grid()
        self.create_widgets()

    def buttonClick(self, pressed_button):
        if pressed_button == "C":
            self.UserIn.set("")
            self.task = ""
            self.result = 0
            
        else:
            self.task = str(self.task) + str(pressed_button)
            self.UserIn.set(self.task)
            
            # Check the string for "term+term" form with a regex
            if pressed_button == "=":
               regex = r"(([0-9]+\.?)+[-+*/]([0-9]?\.?[0-9]+)){1}" # use this expression for decimal numbers too: ([0-9]+\.?)+[-+*/]([0-9]+\.?)+ Old: [0-9]+[-+*/][0-9]+. RIGHT REGEX: (([0-9]+\.?)+[-+*/]([0-9]?\.?[0-9]+))
               possible_expression = re.findall(regex, self.task)
               #print(possible_expression[0]) # this is the result we need to check if in the form number <sign> number
               if(possible_expression): # if the expression on the calculator is of this type we identify each term and the sign
                   print(type(possible_expression[0][0]))
                   terms = re.findall(r"[-+]?\d*\.\d+|\d+", possible_expression[0][0]) # This is where the mathematical expression is!!!!
                   #print(possible_expression[0][0])
                   #print(terms)
                   sign = re.findall(r"[-+*/]" , self.task)
                   execute_as_python_commands = "self.task = float(terms[0]) {} float(terms[1])".format(sign[0])
                   exec(execute_as_python_commands)
                   self.UserIn.set(str(self.task))
               else:
                   self.task = ""
                   self.UserIn.set("Invalid Expression")
                  
    def create_widgets(self):
        #print(self.some_var)
        # The entry which will display the result as well as the numbers as they are entered by the user
        self.user_input = Entry(self, bg="#33C4FF", font=("Verdana", 20, "bold"),justify=RIGHT, textvariable=self.UserIn)
        self.user_input.grid(row = 0, columnspan = 4)
        
        # The frame which contains all the button widgets
        self.button_1 = Button(self, text="1", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("1")).grid(row=1, column=0, sticky=N+S+W+E)
        self.button_2 = Button(self, text="2", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("2")).grid(row=1, column=1, sticky=N+S+W+E)
        self.button_3 = Button(self, text="3", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("3")).grid(row=1, column=2, sticky=N+S+W+E)
        self.button_plus = Button(self, text="+", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("+")).grid(row=1, column=3, sticky=N+S+W+E)

        self.button_4 = Button(self, text="4", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("4")).grid(row=2, column=0, sticky=N+S+W+E)
        self.button_5 = Button(self, text="5", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("5")).grid(row=2, column=1, sticky=N+S+W+E)
        self.button_6 = Button(self, text="6", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("6")).grid(row=2, column=2, sticky=N+S+W+E)
        self.button_minus = Button(self, text="-", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("-")).grid(row=2, column=3, sticky=N+S+W+E)

        self.button_7 = Button(self, text="7", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("7")).grid(row=3, column=0, sticky=N+S+W+E)
        self.button_8 = Button(self, text="8", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("8")).grid(row=3, column=1, sticky=N+S+W+E)
        self.button_9 = Button(self, text="9", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("9")).grid(row=3, column=2, sticky=N+S+W+E)
        self.button_mul = Button(self, text="*", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("*")).grid(row=3, column=3, sticky=N+S+W+E)

        self.button_clc = Button(self, text="C", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("C")).grid(row=4, column=0, sticky=N+S+W+E)
        self.button_0 = Button(self, text="0", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("0")).grid(row=4, column=1, sticky=N+S+W+E)
        self.button_equ = Button(self, text="=", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("=")).grid(row=4, column=2, sticky=N+S+W+E)
        self.button_div = Button(self, text="/", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("/")).grid(row=4, column=3, sticky=N+S+W+E)
        

calculator = Tk()

calculator.title("Calculator")
app = Application(calculator)

calculator.resizable(width = False, height=False)
calculator.mainloop()
