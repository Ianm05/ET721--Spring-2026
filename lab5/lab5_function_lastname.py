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


def generate_random_int(minimum, maximum):
    """
    Generate and return a random integer between minimum and maximum (inclusive)
    
    Args:
        minimum: The minimum value (inclusive)
        maximum: The maximum value (inclusive)
    
    Returns:
        A random integer between minimum and maximum
    """
    import random
    return random.randint(minimum, maximum)


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

print('\nEXCERCISE')

# Example: Generate random integer between min and max
min_val = 1
max_val = 100
random_num = generate_random_int(min_val, max_val)
print(f"Random integer between {min_val} and {max_val}: {random_num}")

# Another example
random_dice = generate_random_int(1, 6)

print(f"Random dice roll (1-6): {random_dice}")