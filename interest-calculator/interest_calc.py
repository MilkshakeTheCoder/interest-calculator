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

class IntrestCalculator:
    # init so that i could use self.
    def __init__(self):
        pass

    def si(self):
        root2 = tk.Tk()
        root2.title("Simple Interest")
        root2.geometry("800x550")
        root2.configure(background="#E7E058")
        def cal_si():
            p=int(a.get())
            r=float(b.get())
            r=float(r/100)
            t=int(c.get())
            simple_interest=(p*(1+(r*t)))
            simple_interest=round(simple_interest,2)
            label.config(text=f"A = ${simple_interest}", background="#E7E058")
        # Create an tk.Entry widget and label for p
        Label(root2, text="Principal Amount", font=('Rockwell 10'), padx= 20, pady= 20, background="#E7E058").pack()
        a=tk.Entry(root2, width=35)
        a.pack()
        # Create an tk.Entry widget and label for r
        Label(root2, text="Interest Rate (without `%` sign)", font=('Rockwell 10'), padx= 20, pady= 20, background="#E7E058").pack()
        b=tk.Entry(root2, width=35)
        b.pack()
        # Create an tk.Entry widget and label for t
        Label(root2, text="How long has rate been applied (in years)?", font=('Rockwell 10'), padx= 20, pady= 20, background="#E7E058").pack()
        c=tk.Entry(root2, width=35)
        c.pack()

        label=ttk.Label(root2, text="Interest: ", font=('Rockwell 15'), background="#E7E058")
        label.pack(pady=20, padx=20)

        ttk.Button(root2, text="Calculate Simple Interest", command=cal_si).pack()
        ttk.Button(root2, text="Back 🔙", command=lambda:[root2.destroy(),self.setup()]).pack(pady=10)
        root2.mainloop()

    # Non-Continual Compound Interest
    def nc(self):
        root3 = tk.Tk()
        root3.title("Non-Continual Compound Interest")
        root3.geometry("800x550")
        root3.configure(background="#4BF381")
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
        Label(root3, text="Principal Amount", font=('Rockwell 10'), padx= 20, pady= 20, background="#4BF381").pack()
        a=tk.Entry(root3, width=35,)
        a.pack()
        Label(root3, text="Interest Rate (without `%` sign)", font=('Rockwell 10'), padx= 20, pady= 20, background="#4BF381").pack()
        b=tk.Entry(root3, width=35)
        b.pack()
        Label(root3, text="How many times is this money being compounded per year (1, 2, 4, 12, 52, 365)?", font=('Rockwell 10'), padx= 20, pady= 20, background="#4BF381").pack()
        c=tk.Entry(root3, width=35)
        c.pack()
        Label(root3, text="How long has this money been compounding (in years)?", font=('Rockwell 10'), padx= 20, pady= 20, background="#4BF381").pack()
        d=tk.Entry(root3, width=35)
        d.pack()

        label=ttk.Label(root3, text="Interest: ", font=('Rockwell 15'), background="#4BF381")
        label.pack(pady=20)

        ttk.Button(root3, text="Calculate Compounded Interest", command=cal_nc).pack()
        ttk.Button(root3, text="Back 🔙", command=lambda:[root3.destroy(), self.setup()]).pack(pady=10)

    def cc(self):
        root4 = tk.Tk()
        root4.title("Continual Compound Interest")
        root4.geometry("800x550")
        root4.configure(background="#F36A4B")
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
        Label(root4, text="Principal Amount", font=('Rockwell 10'), padx= 20, pady= 20, background="#F36A4B").pack()
        a=tk.Entry(root4, width=35,)
        a.pack()
        Label(root4, text="Interest Rate (without `%` sign)", font=('Rockwell 10'), padx= 20, pady= 20, background="#F36A4B").pack()
        b=tk.Entry(root4, width=35)
        b.pack()
        Label(root4, text="How long has this money been compounding (in years)?", font=('Rockwell 10'), padx= 20, pady= 20, background="#F36A4B").pack()
        d=tk.Entry(root4, width=35)
        d.pack()

        label=ttk.Label(root4, text="Interest: ", font=('Rockwell 15'), background="#F36A4B")
        label.pack(pady=20)

        ttk.Button(root4, text="Calculate Continual Compounded Interest", command=cal_cc).pack()
        ttk.Button(root4, text="Back 🔙", command=lambda:[root4.destroy(), self.setup()]).pack(pady=10)

    def setup(self):
        # Create an instance of tkinter frame or root
        root=tk.Tk()
        root.title("Interest Calculator")
        root.geometry("800x550")
        root.configure(background='#57D0F3')
        # Set the size of the tkinter root
        tk.Button(root, text="Simple Interest", font=("Rockwell 15"), command=lambda:[root.destroy(), self.si()], background='#19B3E0').pack(side=TOP, expand=YES)
        tk.Button(root, text="Non-Continual Compound Interest", font=("Rockwell 15"), command=lambda:[root.destroy(), self.nc()], background='#19B3E0').pack(side=TOP, expand=YES)
        tk.Button(root, text="Continual Compound Interest", font=("Rockwell 15"), command=lambda:[root.destroy(), self.cc()], background='#19B3E0').pack(side=TOP, expand=YES)
        root.mainloop()


setupint = IntrestCalculator()
# create instance
# setup.setup()
# referencing InterestCalulator.setup()

#the above code can be written like this: setup = IntrestCalculator().setup() ; it has the reference and the function call

class LogCalculator:
    def __init__(self) -> None:
        pass

    def log(self):
        root2 = tk.Tk()
        root2.title("Logarithm Calcuator")
        root2.geometry("800x550")
        root2.configure(background="#E7E058")
        def cal_log():
            b = int(b2.get())
            y = int(y2.get())
            log_with_base = math.log(y, b)
            label.config(text=log_with_base)
        tk.Label(root2, text="What is the log base?", font=('Rockwell 10'), padx= 20, pady= 20, background="#E7E058").pack()
        b2=tk.Entry(root2, width=35,)
        b2.pack()
        # Create an tk.Entry widget and label for r
        tk.Label(root2, text="What is the y value of the log?", font=('Rockwell 10'), padx= 20, pady= 20, background="#E7E058").pack()
        y2=tk.Entry(root2, width=35)
        y2.pack()
        label=tk.Label(root2, text="X =  ", font=('Rockwell 15'), background="#E7E058")
        label.pack(pady=20)
        ttk.Button(root2, text="Calculate Logarithm", command=cal_log).pack()
        ttk.Button(root2, text="Back 🔙", command=lambda:[root2.destroy(), self.setup()]).pack(pady=10)
        root2.mainloop()

    def ln(self):
        root3 = tk.Tk()
        root3.title("Natural Log Calculator")
        root3.geometry("800x550")
        root3.configure(background="#F36A4B")
        def cal_ln():
            b = math.e
            y = int(y2.get())
            ln_e_base = math.log(y, b)
            label.config(text=ln_e_base)
        tk.Label(root3, text="What is the y value of the log?", font=('Rockwell 10'), padx= 20, pady= 20, background="#F36A4B").pack()
        y2=tk.Entry(root3, width=35)
        y2.pack()
        label = tk.Label(root3, text="X =  ", font=('Rockwell 15'), background="#F36A4B")
        label.pack(pady=20)
        ttk.Button(root3, text="Calculate Natural Log", command=cal_ln).pack()
        ttk.Button(root3, text="Back 🔙", command=lambda:[root3.destroy(), self.setup()]).pack(pady=10)
        root3.mainloop()
        
    def setup(self):
        # Create an instance of tkinter frame or root
        root=tk.Tk()
        root.title("Logarithm Calculator")
        root.geometry("800x550")
        root.configure(background='#57D0F3')
        # Set the size of the tkinter root
        Button(root, text="Log with Base", font=("Rockwell 12"), command=lambda:[root.destroy(), self.log()], background='#19B3E0').pack(side=TOP, expand=YES)
        Button(root, text="Natural Log", font=("Rockwell 12"), command=lambda:[root.destroy(), self.ln()], background='#19B3E0').pack(side=TOP, expand=YES)
        root.mainloop()

setuplog = LogCalculator()

class Unit6Calculator:
    def __init__(self) -> None:
        pass

    def rootthing(self):
        root = tk.Tk()
        root.title("Logarithm Calcuator")
        root.geometry("800x550")
        root.configure(background="#E7E058")
        ttk.Button(root, text="Interest Calulator", command=setupint.setup()).pack()
        ttk.Button(root, text="Logarithm Calulator", command=setuplog.setup()).pack(pady=10)
        ttk.Button(root, text="Close 🔙", command=root.destroy()).pack(pady=10)
        root.mainloop()

run = Unit6Calculator().rootthing()

# Added basic class methods and self parameter for the function for better grouping

# What tkinter functions have I learned here? ^^^
# Button
# Label
# Entry
# Basic Options (side, expand, text, (rootname), command, pack)
# get() partially understood
# There is a way to have everything in one root, but that involves classes. (need more experience)
# classes

# Need to better understand lambda function