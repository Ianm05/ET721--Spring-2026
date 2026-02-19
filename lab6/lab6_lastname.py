"""
Ian Martinez
Lab 6: Classes, Objects, and Methods
"""

print("\n---- example 1: classes")

# a class is like a blueprint of something
# using the class, we can create different instances of an object
# data attributes (properties) are values that represent an object
# methods are functions of an object


class Circle(object):
    def __init__(self, radius, color):
        self.r = radius
        self.c = color

    # method to add value to the radius
    def add_radius(self, plusradius):
        self.r += plusradius
        return self.r


class Rectangle(object):
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color

    # method to calculate and return the area of the rectangle
    def area(self):
        return self.h * self.w

    # method to calculate the perimeter of a rectangle
    def perimeter(self):
        return 2 * (self.h + self.w)

    # method to draw the rectangle
    def drawRectangle(self):
        for i in range(self.h):
            print("*" * self.w)


# create instances of objects
circle1 = Circle(5, "yellow")
circle2 = Circle(2, "red")

rectangle1 = Rectangle(2, 3, "green")
rectangle2 = Rectangle(5, 4, "blue")

# accessing data in an object
print(f"color of circle 2 = {circle2.c}")
print(f"The area of rectangle 1 = {rectangle1.w * rectangle1.h}")
print(f"The area of rectangle 2 = {rectangle2.w * rectangle2.h}")

# modify data of an object
circle2.c = "orange"
print(f"color of circle 2 after modification = {circle2.c}")

print(f"radius of circle 2 = {circle2.r}")

# call method add_radius in circle2 and pass 6
circle2.add_radius(6)
print(f"radius of circle 2 after modification = {circle2.r}")

# call methods in class Rectangle
print(f"The area of rectangle 1 = {rectangle1.area()}")
print(f"The perimeter of rectangle 2 = {rectangle2.perimeter()}")

# draw rectangle
rectangle2.drawRectangle()


print("\n---- exercise 1")


class BankAccount:
    def __init__(self, account_number, account_holder):
        # Properties
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 250.50  # Initial balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds. Withdrawal cannot be made.")

    def display_balance(self):
        print(f"Final balance $ {self.balance:.2f}")


# Testing the BankAccount class

# Creating an instance of the BankAccount class
useraccount = BankAccount(123456789, "Ian Martinez")

# Demonstrating deposits and withdrawals
useraccount.withdraw(700)
useraccount.deposit(500)
useraccount.withdraw(200)
useraccount.display_balance()
