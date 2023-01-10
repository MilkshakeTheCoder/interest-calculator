# C: Complex
# F: Full
# I: Interest
# C: Calculator

import math
import matplotlib.pyplot as plt
from formulas import *

# CURRENT: --V
# Solves for balance (A) with given rate, principal, time, (optionally: compound rate).
# Complex full interest calc will have ability to solve for variables other than A.
# Back and check functions to cc() and nc(), to ensure the user actually wants to do that, and so they don't have to exit to restart.
# Importing formulas separately.

# TO-DO: --V
# Add a monthly/yearly report feature
# Reuse variables via function
# Use PyPlot to graph per year and rate all that
# Possibly add "modes" for different types of interest, so that the user doesn't have to constantly fill out the y/n answers.
# Add Error Handler

# Values p and r get used a lot, so i made a function call for them.

def si():
    # Asks user just confirming that they wanted simple interest not compounded.
    siback = input("Do you want to compute simple interest? y/n: ")
    if siback == "y":
        print("Ok, continuing... ")
    elif siback == "n":
        print("Ok, sending you back...\n")
        setup()
    elif siback == "exit":
        exit()
    else:
        print("I'm taking that as a yes and continuing...")
    # Gathering values...
    p, r, t = prt()
    # Interest eqaution.
    final = (p*(1+(r*t)))
    # Checking if the values inputted are correct --V
    def si_check():
        finalq = input(f"You had a principal amount of ${p}, an interest rate of {r*100}%, and this rate has been applied for {t} years. Is this correct? y/n: ")
        if finalq == "y":
            print(f"\n--------------------> Your new balance would be ${round(final, 2)}\n")
            print("\n-------------------- Running again. Type exit to end the program. --------------------\n\n")
            setup()
        elif finalq == "n":
            print("\n--------------------> Looks like some of the information was incorrectly typed. Please try again.\n")
            si()
        elif finalq == "exit":
            exit()
        else:
            print("\n--------------------> You didn't quite inform me if this is correct or not.\n")
            si_check()
    si_check()

def nc():
    # Confirmation.
    ncback = input("Do you want to compute non-continual compounded interest? y/n: ")
    if ncback == "y":
        print("Ok, continuing... ")
    elif ncback == "n":
        print("Ok, sending you back...\n")
        setup()
    elif ncback == "exit":
        exit()
    else:
        print("I'm taking that as a yes and continuing...")
    # Gathering Values...
    p, r, n, t = prnt()
    # Non-Continual Compound Equation:
    final = (p*((1+(r/n))**(n*t)))
    # Checking if the values inputted are correct --V
    def nccheck():
        finalq = input(f"You had a principal amount of ${p}, an interest rate of {r*100}%, this rate has been applied for {t} years, and this money has been compounding {n} times per year. Is this correct? y/n: ")
        if finalq == "y":
            print(f"\n--------------------> Your new balance would be ${round(final, 2)}\n")
            print("\n-------------------- Running again. Type exit to end the program. --------------------\n\n")
            setup()
        elif finalq == "n":
            print("\n--------------------> Looks like some of the information was incorrectly typed. Please try again.\n")
            si()
        elif finalq == "exit":
            exit()
        else:
            print("\n--------------------> You didn't quite inform me if this is correct or not.\n")
            nccheck()
    nccheck()

def cc():
    # Asks user just confirming that they wanted simple interest not compounded.
    ccback = input("Do you want to compute continually compounded interest? y/n: ")
    if ccback == "y":
        print("Ok, continuing... ")
    elif ccback == "n":
        print("Ok, sending you back...\n")
        setup()
    elif ccback == "exit":
        exit()
    else:
        print("I'm taking that as a yes and continuing...")
    # Gathering Values...
    p, e, r, t = pert()
    # Continual Compound Interest Equation
    final = (p*(e**(r*t)))
    def cccheck():
        finalq = input(f"You had a principal amount of ${p}, an interest rate of {r*100}%, this rate has been applied for {t} years, and this money has been compounding continually. Is this correct? y/n: ")
        if finalq == "y":
            print(f"\n--------------------> Your new balance would be ${round(final, 2)}\n")
            print("\n-------------------- Running again. Type exit to end the program. --------------------\n\n")
            setup()
        elif finalq == "n":
            print("\n--------------------> Looks like some of the information was incorrectly typed. Please try again.\n")
            si()
        elif finalq == "exit":
            exit()
        else:
            print("\n--------------------> You didn't quite inform me if this is correct or not.\n")
            cccheck()
    cccheck()

def compoundfunc():
    setupvar2 = input("Are you compounding continuously? y/n: ")
    if setupvar2 == "y":
        cc()
    elif setupvar2 == "n":
        nc()
    elif setupvar2 == "reset":
        setup()
    elif setupvar2 == "exit":
        exit()
    else:
        print("Is that a y or n? Doesn't look like it.")
        compoundfunc()

def setup():
    setupvar=input("What interest are you calculating? Simple or Compounded? (s or c) ")
    if setupvar == "s":
        si()
    elif setupvar == "c":
        compoundfunc()
    elif setupvar == "exit":
        exit()
    else:
        print(f"I don't think {setupvar} is a interest type.")
        setup()

setup()