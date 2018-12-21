import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Menu
import re
import datetime
from tkinter.font import Font

from tkinter import *


# Define the application class where we will implement our widgets
class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()

        ###### StopWatch variables ########
        self.pause_reset_command = -1
        self.current_time = StringVar() # the variable which displays the current time on the stopwatch
        self.current_time.set("00:00")
        ###################################

        ######## Watch variables ########
        self.local_time = StringVar()
        self.local_time.set("00:00:00")
        self.current_date = StringVar()
        self.current_date.set("2012/10/30")
        ##################################

        self.chosen_gui = "StopWatch"
        self.canvas_funct_buttons = Canvas(self, width=800, height = 50, bg="gray") # IF YOU DO .PACK() HERE IT WILL RETURN NONE AND THEN YOU WILL HAVE PROBLEMS BECAUSE .PACK() RETURNS A 'NONE' TYPE OBJECT
        self.canvas_funct_app = Canvas(self, width=800, height = 590, bg="lavender")
        self.create_buttons()
        self.canvas_funct_buttons.pack()
        self.canvas_funct_app.pack()

    def selectOption(self, passed_option):
        self.chosen_gui = passed_option
        self.update_tool_gui()

    def create_buttons(self):
        # The 'menu' of the application. The selection labels
        stopwatch_select = tk.Button(self, text="Stopwatch", bg="gold4", command=lambda : self.selectOption("StopWatch"))
        countdown_select = tk.Button(self, text="CountDown", bg="gold4", command=lambda : self.selectOption("CountDown"))
        watch_select = tk.Button(self, text="Watch", bg="gold4", command=lambda : self.selectOption("Watch"))

        stopwatch_window = self.canvas_funct_buttons.create_window(0, 0, anchor="nw", width=250, height=50, window=stopwatch_select) # see the python reference book to understand about the canvas_funct_buttons
        countdown_window = self.canvas_funct_buttons.create_window(250, 0, anchor="nw", width=300, height=50, window=countdown_select)
        watch_window = self.canvas_funct_buttons.create_window(550, 0, anchor="nw", width=250, height=50, window=watch_select)

    ########################################################## StopWatch functionality ################################################################################
    def startCounter(self):
        self.pause_reset_command = 0

    def stopCounter(self):
        if self.pause_reset_command != -1: # if the counter is in idle don't need to stop it
            self.pause_reset_command += 1

    def stopWatchCyclic(self):
        if self.chosen_gui == "StopWatch":
            if self.pause_reset_command == 0:
                current_time = self.current_time.get()
                regex_seconds = r"\d+$"
                regex_minutes = r"^\d+"
                seconds = re.findall(regex_seconds, current_time)
                minutes = re.findall(regex_minutes, current_time)

                if seconds[0][0] == '0':
                    seconds = seconds[0][1]
                else:
                    seconds = seconds[0]
                seconds = int(seconds) # check the value of seconds
                seconds += 1

                if minutes[0][0] == '0':
                    minutes = minutes[0][1]
                else:
                    minutes = minutes[0]
                minutes = int(minutes) # check the value of minutes

                if minutes <= 98:
                    if seconds == 60:
                        minutes = minutes+1
                        seconds = 0
                else:
                    pass

                self.current_time.set("{0:0>2}".format(minutes) + ":" + "{0:0>2}".format(seconds))

            if self.pause_reset_command == 1:
                pass

            if self.pause_reset_command == 2:
                self.current_time.set("00:00")
                self.pause_reset_command = -1

            if self.pause_reset_command == -1:
                pass

            self.master.after(1000, self.stopWatchCyclic)
    ########################################################## StopWatch functionality ################################################################################

    ########################################################## CountDown functionality ################################################################################



    ########################################################## CountDown functionality ################################################################################


    ########################################################## Gui Functionality       ################################################################################
    def update_tool_gui(self):
        if self.chosen_gui == "StopWatch":
            self.canvas_funct_app.delete("all")
            self.current_time.set("00:00") # when you reset to stopwatch the timer gets reseted
            digits = Label(self, textvariable=self.current_time, background="lavender", anchor=CENTER)
            digits.config(font=("Courier", 200))

            digits_window = self.canvas_funct_app.create_window(0, 0, anchor="nw", width=800, height=540, window=digits)

            start_button = tk.Button(self, text="Start", bg="#458B74", command=lambda : self.startCounter())
            stop_button = tk.Button(self, text="Stop/Reset", bg="#CD3333", command=lambda : self.stopCounter())
            start_button_window = self.canvas_funct_app.create_window(20, 520, anchor="sw", width=360, height=50, window=start_button)
            stop_button_window = self.canvas_funct_app.create_window(420, 520, anchor="sw", width=360, height=50, window=stop_button)

            self.pause_reset_command = -1
            self.stopWatchCyclic()

        elif self.chosen_gui == "CountDown":
            self.canvas_funct_app.delete("all")
            self.current_time.set("00:00") # when you reset to countdown the timer gets reseted

            minutes = Entry(self, bg="lavender", font=("Courier", 150),justify=RIGHT)
            minutes_window = self.canvas_funct_app.create_window(80, 200, anchor="w",width=260, height=140, window=minutes)

            label =  Label(self, text=":", bg="lavender", font=("Courier", 150), anchor=CENTER)
            label_window = self.canvas_funct_app.create_window(340, 200, anchor="w",width=120, window=label)

            seconds = Entry(self, bg="lavender", font=("Courier", 150),justify=RIGHT)
            seconds_window = self.canvas_funct_app.create_window(460, 200, anchor="w",width=260, height=140, window=seconds)

            start_button = tk.Button(self, text="Start", bg="#458B74", command=lambda : self.startCounter())
            stop_button = tk.Button(self, text="Stop/Reset", bg="#CD3333", command=lambda : self.stopCounter())
            start_button_window = self.canvas_funct_app.create_window(20, 520, anchor="sw", width=360, height=50, window=start_button)
            stop_button_window = self.canvas_funct_app.create_window(420, 520, anchor="sw", width=360, height=50, window=stop_button)

        else:
            self.canvas_funct_app.delete("all")
            local_time = Label(self, textvariable=self.local_time, background="lavender", anchor=CENTER)
            local_time.config(font=("Courier", 100))
            local_time_window = self.canvas_funct_app.create_window(0, 0, anchor="nw", width=800, height=450, window=local_time) ### HOUR:MINUTES:SECONDS

            date = Label(self, textvariable=self.current_date, background="lavender", anchor=CENTER) #### YEAR/MONTH/DATY
            date.config(font=("Courier", 30))
            date_time_window = self.canvas_funct_app.create_window(0, 320, anchor="nw", width=800, height=90, window=date)

            alarm_label = Label(self, text="Alarm: ", background="lavender", anchor=CENTER)
            alarm_label.config(font=("Courier", 20))
            alarm_label_window = self.canvas_funct_app.create_window(60, 500, anchor="nw", width=100, height=50, window=alarm_label)

            select_year = Spinbox(self, from_=2018, to=2050)
            select_year_window = self.canvas_funct_app.create_window(170, 500, anchor="nw", width=50, height=40, window=select_year)

            slash_label = Label(self, text="/", background="lavender", anchor=CENTER)
            slash_label.config(font=("Courier", 25))
            slash_label_window = self.canvas_funct_app.create_window(220, 500, anchor="nw", height=50, window=slash_label)

            select_month = Spinbox(self, from_=1, to=12)
            select_month_window = self.canvas_funct_app.create_window(240, 500, anchor="nw", width=50, height=40, window=select_month)

            slash_label2 = Label(self, text="/", background="lavender", anchor=CENTER)
            slash_label2.config(font=("Courier", 25))
            slash_label_window2 = self.canvas_funct_app.create_window(290, 500, anchor="nw", height=50, window=slash_label2)

            select_day = Spinbox(self, from_=1, to=31)
            select_day_window = self.canvas_funct_app.create_window(310, 500, anchor="nw", width=50, height=40, window=select_day)

            select_hour = Spinbox(self, from_=1, to=24)
            select_hour_window = self.canvas_funct_app.create_window(380, 515, anchor="nw", width=50, height=25, window=select_hour)

            colon_label = Label(self, text="/", background="lavender", anchor=CENTER)
            colon_label.config(font=("Courier", 15))
            colon_label = self.canvas_funct_app.create_window(430, 505, anchor="nw", height=50, window=colon_label)

            select_minute = Spinbox(self, from_=1, to=59)
            select_minute_window = self.canvas_funct_app.create_window(450, 515, anchor="nw", width=50, height=25, window=select_minute)

            set_button = tk.Button(self, text="Set", bg="#E3CF57")
            set_button_window = self.canvas_funct_app.create_window(520, 540, anchor="sw", width=100, height=70, window=set_button)

            clear_button = tk.Button(self, text="Clear", bg="#CD3333")
            clear_button_window = self.canvas_funct_app.create_window(650, 540, anchor="sw", width=100, height=70, window=clear_button)

            #now = datetime.datetime.now()
            #print(now)
     ########################################################## Gui Functionality       ################################################################################


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
