"""
Ian Martinez
Feb 5, 2025
Lab5, function
"""

def area_rectangle(width, length):
    """Calculate the area of a rectangle"""
    return width * length


def print_area_result(width, length, area):
    """Print the rectangle area result"""
    print(f"Rectangle with width {width} and length {length} has area: {area}")


def collectnum(prompt):
    """Collect a number from user input"""
    while True:
        try:
            value = float(input(f"Enter {prompt}: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_distance(x1, x2, y1, y2):
    """Calculate the Euclidean distance between two points"""
    import math
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


print('\n-----Example 1: user-defined function')
w = 8
length = 3
a = area_rectangle(w, length)
print_area_result(w, length, a)
    
print('\n------Example 2: calculate ')
x1 = collectnum('x1')
x2 = collectnum('x2')
y1 = collectnum('y1')
y2 = collectnum('y2')

# testing
print(f"x1: {x1}, x2: {x2}, y1: {y1}, y2: {y2}")

# testing
print(f"Distance: {calculate_distance(x1, x2, y1, y2)}")

print('\nEXCERCISE: A function that compares a guess number with a random number')
import random

# Function to generate a random number
def generate_random_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

# Function to compare guess with random number
def compare_guess(random_number, guess_number):
    if random_number < guess_number:
        print("The number is smaller than the guess number")
    elif random_number > guess_number:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")

# Example usage
GUESS_NUMBER = 50  # Constant guess number

# Generate random number and compare
random_num = generate_random_number(1, 100)
print(f"Random number generated: {random_num}")
print(f"Guess number: {GUESS_NUMBER}")

compare_guess(random_num, GUESS_NUMBER)
