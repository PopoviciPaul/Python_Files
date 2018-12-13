from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Menu


# Define the application class where we will implement our widgets
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.chosen_gui = "StopWatch"
        self.canvas = Canvas(self, width=800, height = 640, bg="gray") # IF YOU DO .PACK() HERE IT WILL RETURN NONE AND THEN YOU WILL HAVE PROBLEMS BECAUSE .PACK() RETURNS A 'NONE' TYPE OBJECT
        self.create_buttons()
        self.canvas.grid()

    def selectOption(self, passed_option):
        self.chosen_gui = passed_option
        self.update_tool_gui()

    def create_buttons(self):
        # The 'menu' of the application. The selection labels
        stopwatch_select = Button(self, text="Stopwatch", command=lambda : self.selectOption("StopWatch"))
        countdown_select = Button(self, text="CountDown", command=lambda : self.selectOption("CountDown"))
        watch_select = Button(self, text="Watch", command=lambda : self.selectOption("Watch"))

        stopwatch_window = self.canvas.create_window(0, 0, anchor="nw", width=250, window=stopwatch_select, height=50) # see the python reference book to understand about the canvas
        countdown_window = self.canvas.create_window(250, 0, anchor="nw", width=300, window=countdown_select, height=50)
        watch_window = self.canvas.create_window(550, 0, anchor="nw", width=250, window=watch_select, height=50)

    # This function updates the gui to correspond to the chosen app type: stopwatch, countdown or watch
    def update_tool_gui(self):
        if self.chosen_gui == "StopWatch":
            #print("Chosen functionality: %s" % self.chosen_gui)
            digits = Label(self, text="00:00", anchor=CENTER)
            digits.config(font=("Courier", 200))
            digits_window = self.canvas.create_window(0, 320, anchor="w", width=800, height=540, window=digits)
            start_button = Button(self, text="Start")
            stop_button = Button(self, text="Stop/Reset")

            start_button_window = self.canvas.create_window(0, 640, anchor="sw", width=400, window=start_button, height=50)

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
