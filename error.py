from cfic import setup

def errorHandler():
    try:
        setup()
    except ValueError:
        print("Wrong value buddy.")
    except TypeError:
        print("Wrong type buddy.")