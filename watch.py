import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Menu
import time
import datetime

# Define the application class where we will implement our widgets
class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.current_time = StringVar() # the variable which displays the current time on the stopwatch
        self.current_time.set("00:00")

        self.chosen_gui = "StopWatch"
        self.canvas = Canvas(self, width=800, height = 640, bg="gray") # IF YOU DO .PACK() HERE IT WILL RETURN NONE AND THEN YOU WILL HAVE PROBLEMS BECAUSE .PACK() RETURNS A 'NONE' TYPE OBJECT
        self.create_buttons()
        self.canvas.grid()

    def selectOption(self, passed_option):
        self.chosen_gui = passed_option
        self.update_tool_gui()

    def create_buttons(self):
        # The 'menu' of the application. The selection labels
        stopwatch_select = tk.Button(self, text="Stopwatch", bg="gold4", command=lambda : self.selectOption("StopWatch"))
        countdown_select = tk.Button(self, text="CountDown", bg="gold4", command=lambda : self.selectOption("CountDown"))
        watch_select = tk.Button(self, text="Watch", bg="gold4", command=lambda : self.selectOption("Watch"))

        stopwatch_window = self.canvas.create_window(0, 0, anchor="nw", width=250, height=50, window=stopwatch_select) # see the python reference book to understand about the canvas
        countdown_window = self.canvas.create_window(250, 0, anchor="nw", width=300, height=50, window=countdown_select)
        watch_window = self.canvas.create_window(550, 0, anchor="nw", width=250, height=50, window=watch_select)

    def startCounter(self, start_from):
        #start_from = type str: represents the time from which to re(start) the timer
        start_time = time.time()
        print(start_time)


    # This function updates the gui to correspond to the chosen app type: stopwatch, countdown or watch
    def update_tool_gui(self):
        if self.chosen_gui == "StopWatch":
            #print("Chosen functionality: %s" % self.chosen_gui)
            digits = Label(self, textvariable=self.current_time, background="lavender", anchor=CENTER)
            digits.config(font=("Courier", 200))

            digits_window = self.canvas.create_window(0, 320, anchor="w", width=800, height=540, window=digits)

            start_button = tk.Button(self, text="Start", bg="green2", command=lambda : self.startCounter(self.current_time.get()))
            stop_button = tk.Button(self, text="Stop/Reset", bg="red")
            start_button_window = self.canvas.create_window(0, 640, anchor="sw", width=400, height=50, window=start_button)
            stop_button_window = self.canvas.create_window(400, 640, anchor="sw", width=400, height=50, window=stop_button)

        elif self.chosen_gui == "CountDown":
            print("Chosen functionality: %s" % self.chosen_gui)
        else:
            print("Chosen functionality: %s" % self.chosen_gui)

watch = Tk()
watch.title("Watch")
app = Application(watch)
app_width = 800
app_height = 640

screen_width = watch.winfo_screenwidth()
screen_height = watch.winfo_screenheight()

x_coord = (screen_width/2) - (app_width/2)
y_coord = (screen_height/2) - (app_height/2)

watch.geometry("%dx%d+%d+%d" % (app_width, app_height, x_coord, y_coord))
watch.mainloop()
