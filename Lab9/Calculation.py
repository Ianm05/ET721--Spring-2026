"""
Ian Martinez
Lab 9 - Unit Testing
Feb 26, 2026
"""

def addthreenumbers(n1=0, n2=0, n3=0):
    return n1 + n2 + n3


def subtracttwonumbers(n1=0, n2=0):
    return n1 - n2


def multiplythreenumbers(n1=0, n2=0, n3=0):
    return n1 * n2 * n3


def dividetwonnumbers(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except ValueError:
        print("ERROR! not a numerical value")
        return None
    except:
        print("ERROR! can't divide the numbers")
        return None