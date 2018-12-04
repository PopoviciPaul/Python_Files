from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Menu


def convert_meters():
    # get value from entry and convert it to all
    result_in_meters = int(label1_1.get())# integer value
    result_in_km.set(float(result_in_meters/1000))
    result_in_dem.set(float(result_in_meters*10))
    result_in_miles.set(float(result_in_meters*0.000621371))
    result_in_yards.set(float(result_in_meters*1.09361))


def get_value_and_convert():
    if(combo1.get()=="meters"):
        convert_meters()
    elif(combo1.get()=="centimeters"):
        convert_centimeters()
    elif(combo1.get()=="millimeters"):
        convert_millimeters()
    elif(combo1.get()=="inches"):
        convert_inches()
    else:
        result_in_km.set("0")
        result_in_dem.set("0")
        result_in_miles.set("0")
        result_in_yards.set("0")

window = Tk()
window.title("Converter")
result = IntVar()

result_in_km = StringVar()
result_in_dem = StringVar()
result_in_miles = StringVar()
result_in_yards = StringVar()

canvas1 = Canvas(window, width=400, height=320, bd=1, highlightthickness=1, relief='ridge')
canvas1.grid(row=0, column=0, padx=220, pady=160)

#### Things to convert #####
label1 = Label(canvas1, text="Convert ", width=8)
label1_1 = Entry(canvas1, width=4) # between label1 and combobox
combo1 = Combobox(canvas1, width=8)
combo1['values'] = ("meters","centimeters","millimeters","inches")
combo1.current(0)
label2 = Label(canvas1, text=" to:", width=10)
############################

#### Convert to: ####
label3 = Label(canvas1, text="Km: ", width=10)
label4 = Label(canvas1, text="Dem: ", width=10)
label5 = Label(canvas1, text="Miles: ", width=10)
label6 = Label(canvas1, text="Yards: ", width=10)
#####################

#### Displaying labels ####
display1 = Label(canvas1, textvariable=result_in_km, width=40, relief=SUNKEN)
display2 = Label(canvas1, textvariable=result_in_dem, width=40, relief=SUNKEN)
display3 = Label(canvas1, textvariable=result_in_miles, width=40, relief=SUNKEN)
display4 = Label(canvas1, textvariable=result_in_yards, width=40, relief=SUNKEN)
###########################

#### The convert button ####
convert_button = Button(canvas1, width=40, text="Convert", command=get_value_and_convert)
############################

label1_window = canvas1.create_window(100, 10, anchor=NW, window=label1)
label1_1_window = canvas1.create_window(160, 10, anchor=NW, window=label1_1)
combo1_window = canvas1.create_window(200, 10, anchor=NW, window=combo1)
label2_window = canvas1.create_window(300, 10, anchor=NW, window=label2)

label3_window = canvas1.create_window(10, 80, anchor=NW, window=label3)
display1_window = canvas1.create_window(60, 80, anchor=NW, window=display1)

label4_window = canvas1.create_window(10, 120, anchor=NW, window=label4)
display2_window = canvas1.create_window(60, 120, anchor=NW, window=display2)

label5_window = canvas1.create_window(10, 160, anchor=NW, window=label5)
display3_window = canvas1.create_window(60, 160, anchor=NW, window=display3)


label6_window = canvas1.create_window(10, 200, anchor=NW, window=label6)
display4_window = canvas1.create_window(60, 200, anchor=NW, window=display4)

display5_window = canvas1.create_window(50, 250, anchor=NW, window=convert_button)


window.geometry('800x640')


window.mainloop()
