"""
Ian Martinez
March 3, 2026
Lab 10, unite testing using pytest
"""
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b
"""
# testing
print(add(2,3)) # should print 5
print(add(-8, 5 )) # should print -3
print(subtract(7, 5)) # should print 2
print(subtract(-7, 5)) # should print -2
print(subtract(-7, -5)) # should print 12
"""

# lab exercise 1: basic testing
def divide(a,b):
    if b == 0:
        raise ValueError("Can't divide by zero")
        return a/b
    
    # local testing
    print(divide(5/2)) # should print 2.5
    print(divide(3/0)) # should raise ValueError
    
# local testing
# print(divide(5,2)) # 2.5
# print(divide(3,0)) # should raise ValueError

# lab exercise 2: password validation: 8+ characters, at least one uppercase letter, at least one lowercase letter, at least one digit, and at least one special character
import string

def validate_password(password):
    if len(password) < 8:
        return False
    special_characters = string.punctuation
    
    for char in password:
        if char in special_characters:
            return True
    
    return False
    
    # local testing
    print(validate_password("peterpan")) # true   
    print(validate_password("Peter pan"))   # false
    print(validate_password("Peter#pan")) # false
    print(validate_password("Peter%pan"))
    print(validate_password("Peter"))
    
# lab exercise 3: test if a number is even
def is_even(n):
    return (n%2 ==0 and n !=0)

    # local testing
    print(is_even(8)) # true
    print(is_even(-5)) # false
    print(is_even(0)) # false
    print(is_even(-12)) # true
    print(is_even(11)) # false