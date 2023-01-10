import math

# Simple interest inputs and formula...
def prt():
    p = int(input("What is your depoist/initial amount? "))
    r = float(input("What is your interest rate as a percentage? "))
    r=float(r/100)
    t = int(input("How long has this interest been applied (in years)? "))
    return p, r, t

# Non-continual compound interest inputs and formula...
def prnt():
    p = int(input("What is your depoist/initial amount? "))
    r = float(input("What is your interest rate as a percentage? "))
    r=float(r/100)
    n = int(input("How many times is your money being compounded per year (1, 2, 4, 12, 52, 365)? "))
    t = int(input("How long has this interest been applied (in years)? "))
    return p, r, n, t

# Continual Compound interest inputs and formula...
def pert():
    p = int(input("What is your depoist/initial amount? "))
    e = math.e
    r = float(input("What is your interest rate as a percentage? "))
    r=float(r/100)
    t = int(input("How long has this interest been applied (in years)? "))
    return p, e, r, t