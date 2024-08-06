from tkinter import *

window = Tk() #intial

data = ""
def get_data(value):
    global data
    
    data = data+str(value)
    var.set(data)

def equal_data():
    global data
    
    try:
        total = str(eval(data))
        var.set(total)
        data = ""
    except :
        var.set("Not division by zero")
def clear():
    global data
    data = ""
    var.set("")

window.title("Calculator made by kartik") # title
window.iconbitmap(r"C:\Users\mrkar\Downloads\calculator.ico") # Set icon
window.config(bg="yellow")
window.resizable(False, False) # Off resize function
width = 500
height = 550

system_width = window.winfo_screenwidth()
system_height = window.winfo_screenheight()

center_x = int(system_width/2 - width/2)
center_y = int(system_height/2 - height/2)
window.geometry(f"{width}x{height}+{center_x}+{center_y}")

# Create Heading

label_title = Label(window, text="Calculator", font=("Times New Roman",50,"bold"), bg="yellow")
label_title.place(x=80,y=20,height=70,width=340)


# Create Display
var = StringVar()
entry = Entry(window,relief="sunken",font=("Times New Roman",30,"bold"),bd=5
              ,textvariable=var)
entry.place(x=20,y=100,height=70,width=460)


button_7 = Button(window, text="7",font=("Times New Roman",20,"bold"),
                  command=lambda:get_data(7))
button_7.place(x=20, y=190,height=70, width=115)

button_8 = Button(window, text="8",font=("Times New Roman",20,"bold"),
                  command=lambda:get_data(8))
button_8.place(x=135, y=190,height=70, width=115)

button_9 = Button(window, text="9",font=("Times New Roman",20,"bold"),
                  command=lambda:get_data(9))
button_9.place(x=250, y=190,height=70, width=115)

button_addition = Button(window, text="+",font=("Times New Roman",20,"bold"),
                  command=lambda:get_data("+"))
button_addition.place(x=365, y=190,height=70, width=115)

#--------------------------------------------------------------

button_4 = Button(window, text="4",font=("Times New Roman",20,"bold"),
                  command=lambda:get_data(4))
button_4.place(x=20, y=260,height=70, width=115)

button_5 = Button(window, text="5",font=("Times New Roman",20,"bold"),
                  command=lambda:get_data(5))
button_5.place(x=135, y=260,height=70, width=115)

button_6 = Button(window, text="6", font=("Times New Roman",20,"bold"),
                  command=lambda:get_data(6))
button_6.place(x=250, y=260,height=70, width=115)

button_sub = Button(window, text="-", font=("Times New Roman",20,"bold"),
                  command=lambda:get_data("-"))
button_sub.place(x=365, y=260,height=70, width=115)

#--------------------------------------------------------------

button_1 = Button(window, text="1", font=("Times New Roman",20,"bold"),
                  command=lambda:get_data(1))
button_1.place(x=20, y=330,height=70, width=115)

button_2 = Button(window, text="2", font=("Times New Roman",20,"bold"),
                  command=lambda:get_data(2))
button_2.place(x=135, y=330,height=70, width=115)

button_3 = Button(window, text="3", font=("Times New Roman",20,"bold"),
                  command=lambda:get_data(3))
button_3.place(x=250, y=330,height=70, width=115)

button_multi = Button(window, text="x", font=("Times New Roman",20,"bold"),
                  command=lambda:get_data("*"))
button_multi.place(x=365, y=330,height=70, width=115)

#--------------------------------------------------------------

button_clr = Button(window, text="Clear", font=("Times New Roman",20,"bold"),
                  command=lambda:clear())
button_clr.place(x=20, y=400,height=70, width=115)

button_0 = Button(window, text="0", font=("Times New Roman",20,"bold"),
                  command=lambda:get_data(0))
button_0.place(x=135, y=400,height=70, width=115)

button_dot = Button(window, text=".", font=("Times New Roman",20,"bold"),
                  command=lambda:get_data("."))
button_dot.place(x=250, y=400,height=70, width=115)

button_div = Button(window, text="/", font=("Times New Roman",20,"bold"),
                  command=lambda:get_data("/"))
button_div.place(x=365, y=400,height=70, width=115)

button_equal = Button(window, text="=", font=("Times New Roman",20,"bold"),
                  command=lambda:equal_data())
button_equal.place(x=135, y=470,height=70, width=230)


window.mainloop()
