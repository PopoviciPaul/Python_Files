from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Menu

# Define the application class where we will implement our widgets
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        # CANVAS COLOUR DEFAULTS TO THE COLOUR OF THE WORKING WINDOW
        canvas = Canvas(master, width=800, height = 640, bg="gray") # IF YOU DO .PACK() HERE IT WILL RETURN NONE AND THEN YOU WILL HAVE PROBLEMS BECAUSE .PACK() RETURNS A 'NONE' TYPE OBJECT
        canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

        # The 'menu' of the application. The selection labels
        stopwatch_label = Label(master, text="Stopwatch", font=("Helvetica", 20))
        stopwatch_window = canvas.create_window(0,0, window=stopwatch_label)


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
