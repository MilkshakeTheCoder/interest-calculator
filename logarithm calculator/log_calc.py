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
    window2.configure(background="#E7E058")
    def cal_log():
        b = int(b2.get())
        y = int(y2.get())
        log_with_base = math.log(y, b)
        label.config(text=log_with_base)
    Label(window2, text="What is the log base?", font=('Rockwell 10'), padx= 20, pady= 20, background="#E7E058").pack()
    b2=tk.Entry(window2, width=35,)
    b2.pack()
    # Create an tk.Entry widget and label for r
    Label(window2, text="What is the y value of the log?", font=('Rockwell 10'), padx= 20, pady= 20, background="#E7E058").pack()
    y2=tk.Entry(window2, width=35)
    y2.pack()
    label=ttk.Label(window2, text="X =  ", font=('Rockwell 15'), background="#E7E058")
    label.pack(pady=20)
    ttk.Button(window2, text="Calculate Logarithm", command=cal_log).pack()
    ttk.Button(window2, text="Back 🔙", command=lambda:[window2.destroy(), setup()]).pack(pady=10)
    window2.mainloop()

def ln():
    window3 = tk.Tk()
    window3.title("Natural Log Calculator")
    window3.geometry("700x450")
    window3.configure(background="#F36A4B")
    def cal_ln():
        b = math.e
        y = int(y2.get())
        ln_e_base = math.log(y, b)
        label.config(text=ln_e_base)
    Label(window3, text="What is the y value of the log?", font=('Rockwell 10'), padx= 20, pady= 20, background="#F36A4B").pack()
    y2=tk.Entry(window3, width=35)
    y2.pack()
    label = Label(window3, text="X =  ", font=('Rockwell 15'), background="#F36A4B")
    label.pack(pady=20)
    ttk.Button(window3, text="Calculate Natural Log", command=cal_ln).pack()
    ttk.Button(window3, text="Back 🔙", command=lambda:[window3.destroy(), setup()]).pack(pady=10)
    window3.mainloop()
    
def setup():
    # Create an instance of tkinter frame or window
    root=tk.Tk()
    root.title("Logarithm Calculator")
    root.geometry("700x450")
    root.configure(background='#57D0F3')
    # Set the size of the tkinter window
    tk.Button(root, text="Log with Base", font=("Rockwell 12"), command=lambda:[root.destroy(), log()], background='#19B3E0').pack(side=TOP, expand=YES)
    tk.Button(root, text="Natural Log", font=("Rockwell 12"), command=lambda:[root.destroy(), ln()], background='#19B3E0').pack(side=TOP, expand=YES)
    root.mainloop()

setup()