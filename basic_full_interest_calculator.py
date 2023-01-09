import math


# CURRENT: --V
# Solves for balance (A) with given rate, principal, time, (optionally: compound rate).
# Complex full interest calc will have ability to solve for variables other than A.

# TO-DO: --V
# Add a monthly/yearly report feature
# Reuse variables via function
# Use PyPlot to graph per year and rate all that

def si():
    # Asks user just confirming that they wanted simple interest not compounded.
    siback = input("Do you want to compute simple interest? y/n: ")
    if siback == "y":
        print("Ok, continuing... ")
    elif siback == "n":
        print("Ok, sending you back...")
        setup()
    elif siback == "exit":
        exit()
    else:
        print("I'm taking that as a yes and continuing...")
    # Gathering values...
    p = int(input("What is your depoist/initial amount? "))
    r = float(input("What is your interest rate as a percentage? "))
    rr=float(r/100)
    t = int(input("How long has this interest been applied (in years)? "))
    # Interest eqaution.
    final = (p*(1+(rr*t)))
    # Checking if the values inputted are correct --V
    def si_check():
        finalq = input(f"You had a principal amount of ${p}, an interest rate of {rr*100}%, and this rate has been applied for {t} years. Is this correct? y/n: ")
        if finalq == "y":
            print(f"\n--------------------> Your new balance would be ${round(final, 2)}\n")
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
    p = int(input("What is your depoist/initial amount? "))
    r = float(input("What is your interest rate as a percentage? "))
    rr = float(r/100)
    n = int(input("How many times is your money being compounded per year (1, 2, 4, 12, 52, 365)? "))
    ct = int(input("How long (in years) has this been compounding? "))
    # i changed t to ct because if I am to reuse this varible via a function in the future, it should not be confused with t, which is for simple, not compounded interest. it has been changed for nc and cc.
    final = (p*((1+(rr/n))**(n*ct)))
    print(f"Your balance after {ct} years, with an interest rate of {rr*100}% and a compounding rate of {n} times a year, is ${round(final, 2)}")

def cc():
    p = int(input("What is your depoist/initial amount? "))
    r = float(input("What is your interest rate as a percentage? "))
    rr = float(r/100)
    e = math.e
    ct = int(input("How long (in years) has this been compounding? "))
    final = (p*(e**(rr*ct)))
    print(f"Your balance after {ct} years, with an interest rate of {rr*100}% and continuous compounding, is ${round(final, 2)}")

def compoundfunc():
    setupvar2 = input("Are you compounding continuously? y/n: ")
    if setupvar2 == "y":
        cc()
    elif setupvar2 == "n":
        nc()
    elif setupvar2 == "reset":
        setup()
    elif setupvar2 == "exit" or "Exit":
        exit()
    else:
        print("Is that a y or n? Doesn't look like it.")
        compoundfunc()

def setup():
    setupvar=input("What interest are you calculating today? Simple or Compounded? (s or c) ")
    if setupvar == "s":
        si()
    elif setupvar == "c":
        compoundfunc()
    else:
        print(f"I don't think {setupvar} is a interest type.")
        setup()

setup()