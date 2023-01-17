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
    window2.geometry("800x550")
    window2.configure(background="#E7E058")
    def cal_si():
        p=int(a.get())
        r=float(b.get())
        r=float(r/100)
        t=int(c.get())
        simple_interest=(p*(1+(r*t)))
        simple_interest=round(simple_interest,2)
        label.config(text=f"A = ${simple_interest}", background="#E7E058")
    # Create an tk.Entry widget and label for p
    Label(window2, text="Principal Amount", font=('Rockwell 10'), padx= 20, pady= 20, background="#E7E058").pack()
    a=tk.Entry(window2, width=35)
    a.pack()
    # Create an tk.Entry widget and label for r
    Label(window2, text="Interest Rate (without `%` sign)", font=('Rockwell 10'), padx= 20, pady= 20, background="#E7E058").pack()
    b=tk.Entry(window2, width=35)
    b.pack()
    # Create an tk.Entry widget and label for t
    Label(window2, text="How long has rate been applied (in years)?", font=('Rockwell 10'), padx= 20, pady= 20, background="#E7E058").pack()
    c=tk.Entry(window2, width=35)
    c.pack()

    label=ttk.Label(window2, text="Interest: ", font=('Rockwell 15'), background="#E7E058")
    label.pack(pady=20, padx=20)

    ttk.Button(window2, text="Calculate Simple Interest", command=cal_si).pack()
    ttk.Button(window2, text="Back 🔙", command=lambda:[window2.destroy(),setup()]).pack(pady=10)
    window2.mainloop()

# Non-Continual Compound Interest
def nc():
    window3 = tk.Tk()
    window3.title("Non-Continual Compound Interest")
    window3.geometry("800x550")
    window3.configure(background="#4BF381")
    def cal_nc():
        p=int(a.get())
        r=float(b.get())
        r=float(r/100)
        n=int(c.get())
        t=int(d.get())
        nc_interest=(p*((1+(r/n))**(n*t)))
        nc_interest = round(nc_interest, 2)
        label.config(text=f"A = ${nc_interest}", background="#4BF381")
    # Create an tk.Entry widget
    Label(window3, text="Principal Amount", font=('Rockwell 10'), padx= 20, pady= 20, background="#4BF381").pack()
    a=tk.Entry(window3, width=35,)
    a.pack()
    Label(window3, text="Interest Rate (without `%` sign)", font=('Rockwell 10'), padx= 20, pady= 20, background="#4BF381").pack()
    b=tk.Entry(window3, width=35)
    b.pack()
    Label(window3, text="How many times is this money being compounded per year (1, 2, 4, 12, 52, 365)?", font=('Rockwell 10'), padx= 20, pady= 20, background="#4BF381").pack()
    c=tk.Entry(window3, width=35)
    c.pack()
    Label(window3, text="How long has this money been compounding (in years)?", font=('Rockwell 10'), padx= 20, pady= 20, background="#4BF381").pack()
    d=tk.Entry(window3, width=35)
    d.pack()

    label=ttk.Label(window3, text="Interest: ", font=('Rockwell 15'), background="#4BF381")
    label.pack(pady=20)

    ttk.Button(window3, text="Calculate Compounded Interest", command=cal_nc).pack()
    ttk.Button(window3, text="Back 🔙", command=lambda:[window3.destroy(), setup()]).pack(pady=10)

def cc():
    window4 = tk.Tk()
    window4.title("Continual Compound Interest")
    window4.geometry("800x550")
    window4.configure(background="#F36A4B")
    def cal_cc():
        p=int(a.get())
        r=float(b.get())
        r=float(r/100)
        e = math.e
        t=int(d.get())
        cc_interest=(p*(e**(r*t)))
        cc_interest = round(cc_interest, 2)
        label.config(text=f"A = ${cc_interest}", background="#F36A4B")
    # Create an tk.Entry widget
    Label(window4, text="Principal Amount", font=('Rockwell 10'), padx= 20, pady= 20, background="#F36A4B").pack()
    a=tk.Entry(window4, width=35,)
    a.pack()
    Label(window4, text="Interest Rate (without `%` sign)", font=('Rockwell 10'), padx= 20, pady= 20, background="#F36A4B").pack()
    b=tk.Entry(window4, width=35)
    b.pack()
    Label(window4, text="How long has this money been compounding (in years)?", font=('Rockwell 10'), padx= 20, pady= 20, background="#F36A4B").pack()
    d=tk.Entry(window4, width=35)
    d.pack()

    label=ttk.Label(window4, text="Interest: ", font=('Rockwell 15'), background="#F36A4B")
    label.pack(pady=20)

    ttk.Button(window4, text="Calculate Continual Compounded Interest", command=cal_cc).pack()
    ttk.Button(window4, text="Back 🔙", command=lambda:[window4.destroy(), setup()]).pack(pady=10)

def setup():
    # Create an instance of tkinter frame or window
    root=tk.Tk()
    root.title("Interest Calculator")
    root.geometry("800x550")
    root.configure(background='#57D0F3')
    # Set the size of the tkinter window
    tk.Button(root, text="Simple Interest", font=("Rockwell 15"), command=lambda:[root.destroy(), si()], background='#19B3E0').pack(side=TOP, expand=YES)
    tk.Button(root, text="Non-Continual Compound Interest", font=("Rockwell 15"), command=lambda:[root.destroy(), nc()], background='#19B3E0').pack(side=TOP, expand=YES)
    tk.Button(root, text="Continual Compound Interest", font=("Rockwell 15"), command=lambda:[root.destroy(), cc()], background='#19B3E0').pack(side=TOP, expand=YES)
    root.mainloop()

setup()

# What tkinter functions have I learned here? ^^^
# Button
# Label
# Entry
# Basic Options (side, expand, text, (windowname), command, pack)
# get() partially understood
# There is a way to have everything in one window, but that involves classes. (need more experience)

# Need to better understand lambda function