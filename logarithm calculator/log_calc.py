import math
import numbers
import decimal
import tkinter as tk
from tkinter import *
from tkinter import ttk

def log():
    window2 = tk.Tk()
    window2.title("Logarithm Calcuator")
    window2.geometry("700x450")
    def cal_log():
        b = int(b2.get())
        y = int(y2.get())
        log_with_base = math.log(y, b)
        label.config(text=log_with_base)
    Label(window2, text="What is the log base?", font=('Calibri 10'), padx= 20, pady= 20).pack()
    b2=tk.Entry(window2, width=35,)
    b2.pack()
    # Create an tk.Entry widget and label for r
    Label(window2, text="What is the y value of the log?", font=('Calibri 10'), padx= 20, pady= 20).pack()
    y2=tk.Entry(window2, width=35)
    y2.pack()
    label=ttk.Label(window2, text="X =  ", font=('Calibri 15'))
    label.pack(pady=20)
    ttk.Button(window2, text="Calculate Logarithm", command=cal_log).pack()
    ttk.Button(window2, text="Back 🔙", command=setup).pack()
    window2.mainloop()

def ln():
    window3 = tk.Tk()
    window3.title("Natural Log Calculator")
    window3.geometry("700x450")
    def cal_ln():
        b = math.e
        y = int(y2.get())
        ln_e_base = math.log(y, b)
        label.config(text=ln_e_base)
    Label(window3, text="What is the y value of the log?", font=('Calibri 10'), padx= 20, pady= 20).pack()
    y2=tk.Entry(window3, width=35)
    y2.pack()
    label = Label(window3, text="X =  ", font=('Calibri 15'))
    label.pack(pady=20)
    ttk.Button(window3, text="Calculate Logarithm", command=cal_ln).pack()
    ttk.Button(window3, text="Back 🔙", command=setup).pack()
    window3.mainloop()
    
def setup():
    # Create an instance of tkinter frame or window
    window=tk.Tk()
    window.title("Logarithm Calculator")
    window.geometry("700x450")
    # Set the size of the tkinter window
    tk.Button(window, text="Log with Base", font=("Calibri 12"), command=log).pack(side=TOP, expand=YES)
    tk.Button(window, text="Natural Log", font=("Calibri 12"), command=ln).pack(side=TOP, expand=YES)
    window.mainloop()

setup()