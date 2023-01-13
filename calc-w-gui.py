# CURRENT: --V
# Solves for balance (A) with given rate, principal, time, (optionally: compound rate).
# Complex full interest calc will have ability to solve for variables other than A.
# Back and check functions to cc() and nc(), to ensure the user actually wants to do that, and so they don't have to exit to restart.
# Importing formulas separately.
# 99% complete GUI support.
# Modes added in GUI support, no need for check() and back() functions --- see archived.cfic

# TO-DO: --V
# Add a monthly/yearly report feature
# Use PyPlot to graph per year and rate all that
# Add Error Handler

# tk shorthand
import tkinter as tk
# import all
from tkinter import *
# themed tkinter (more color options)
from tkinter import ttk
# for e
import math

# si function
def si():
    window2 = tk.Tk()
    window2.title("Simple Interest")
    window2.geometry("700x450")
    def cal_si():
        p=int(a.get())
        r=float(b.get())
        r=float(r/100)
        t=int(c.get())
        simple_interest=(p*(1+(r*t)))
        label.config(text=simple_interest)
    # Create an tk.Entry widget and label for p
    Label(window2, text="Principal Amount", font=('Calibri 10'), padx= 20, pady= 20).pack()
    a=tk.Entry(window2, width=35,)
    a.pack()
    # Create an tk.Entry widget and label for r
    Label(window2, text="Interest Rate (without `%` sign)", font=('Calibri 10'), padx= 20, pady= 20).pack()
    b=tk.Entry(window2, width=35)
    b.pack()
    # Create an tk.Entry widget and label for t
    Label(window2, text="How long has rate been applied (in years)?", font=('Calibri 10'), padx= 20, pady= 20).pack()
    c=tk.Entry(window2, width=35)
    c.pack()

    label=ttk.Label(window2, text="Interest: ", font=('Calibri 15'))
    label.pack(pady=20)

    ttk.Button(window2, text="Calculate Simple Interest", command=cal_si).pack()
    ttk.Button(window2, text="Back 🔙", command=setup).pack()
    window2.mainloop()

# Non-Continual Compound Interest
def nc():
    window3 = tk.Tk()
    window3.title("Non-Continual Compound Interest")
    window3.geometry("700x450")
    def cal_nc():
        p=int(a.get())
        r=float(b.get())
        r=float(r/100)
        n=int(c.get())
        t=int(d.get())
        nc_interest=(p*((1+(r/n))**(n*t)))
        label.config(text=nc_interest)

    # Create an tk.Entry widget
    Label(window3, text="Principal Amount", font=('Calibri 10'), padx= 20, pady= 20).pack()
    a=tk.Entry(window3, width=35,)
    a.pack()
    Label(window3, text="Interest Rate (without `%` sign)", font=('Calibri 10'), padx= 20, pady= 20).pack()
    b=tk.Entry(window3, width=35)
    b.pack()
    Label(window3, text="How many times is this money being compounded per year (1, 2, 4, 12, 52, 365)?", font=('Calibri 10'), padx= 20, pady= 20).pack()
    c=tk.Entry(window3, width=35)
    c.pack()
    Label(window3, text="How long has this money been compounding (in years)?", font=('Calibri 10'), padx= 20, pady= 20).pack()
    d=tk.Entry(window3, width=35)
    d.pack()

    label=ttk.Label(window3, text="Interest: ", font=('Calibri 15'))
    label.pack(pady=20)

    ttk.Button(window3, text="Calculate Compounded Interest", command=cal_nc).pack()
    ttk.Button(window3, text="Back 🔙", command=setup).pack()

def cc():
    window4 = tk.Tk()
    window4.title("Continual Compound Interest")
    window4.geometry("700x450")
    def cal_cc():
        p=int(a.get())
        r=float(b.get())
        r=float(r/100)
        e = math.e
        t=int(d.get())
        cc_interest=(p*(e**(r*t)))
        label.config(text=cc_interest)
    # Create an tk.Entry widget
    Label(window4, text="Principal Amount", font=('Calibri 10'), padx= 20, pady= 20).pack()
    a=tk.Entry(window4, width=35,)
    a.pack()
    Label(window4, text="Interest Rate (without `%` sign)", font=('Calibri 10'), padx= 20, pady= 20).pack()
    b=tk.Entry(window4, width=35)
    b.pack()
    Label(window4, text="How long has this money been compounding (in years)?", font=('Calibri 10'), padx= 20, pady= 20).pack()
    d=tk.Entry(window4, width=35)
    d.pack()

    label=ttk.Label(window4, text="Interest: ", font=('Calibri 15'))
    label.pack(pady=20)

    ttk.Button(window4, text="Calculate Continual Compounded Interest", command=cal_cc).pack()
    ttk.Button(window4, text="Back 🔙", command=setup).pack()

def setup():
    # Create an instance of tkinter frame or window
    window=tk.Tk()
    window.title("Interest Calculator")
    # Set the size of the tkinter window
    window.geometry("700x450")
    tk.Button(window, text="Simple Interest", font=("Calibri 20"), command=si).pack(side=TOP, expand=YES)
    tk.Button(window, text="Non-Continual Compound Interest", font=("Calibri 20"), command=nc).pack(side=TOP, expand=YES)
    tk.Button(window, text="Continual Compound Interest", font=("Calibri 20"), command=cc).pack(side=TOP, expand=YES)
    window.mainloop()

setup()

# What tkinter functions have I learned here? ^^^
# Button
# Label
# Entry
# Basic Options (side, expand, text, (windowname), command, pack)
# get() partially understood
# There is a way to have everything in one window, but that involves classes. (need more experience)