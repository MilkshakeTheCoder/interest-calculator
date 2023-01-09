import numbers
import decimal
import random
import math

def nc():
    p = int(input("What is your depoist/initial amount? "))
    r = float(input("What is your interest rate as a decimal? "))
    n = int(input("How many times is your money being compounded per year (1, 2, 4, 12, 52, 365)? "))
    t = int(input("How long (in years) has this been compounding? "))
    final = (p*((1+(r/n))**(n*t)))
    print(f"Your balance after {t} years, with an interest rate of {r*100}% and a compounding rate of {n} times a year, is ${round(final, 2)}")

def cc():
    p = int(input("What is your depoist/initial amount? "))
    r = float(input("What is your interest rate as a decimal? "))
    e = math.e
    t = int(input("How long (in years) has this been compounding? "))
    final = (p*(e**(r*t)))
    print(final)

def bcicsetup():
    bcicsetupvar = input("Are you compounding continuously? y/n: ")
    if bcicsetupvar == "y":
        cc()
    elif bcicsetupvar == "n":
        nc()
    else:
        print("Is that a y or n? Doesn't look like it.")

bcicsetup()