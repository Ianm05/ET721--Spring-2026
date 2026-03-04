"""
Ian Martinez
March 3, 2026
Lab 10, unit testing using pytest
"""

import pytest
from calculator import *
@pytest.mark.parametrize(
    "password, expected",
    [
        ("Peter$Pan", True),   # valid password
        ("pan", False),        # too short
        ("peterpan", False),   # no special character
        ("Spider$Man", True),  # another valid password
    ],
)
def test_validate_password(password, expected):
    assert validate_password(password) == expected

def test_add():
    assert add(2, 3) == 5
    assert add(-8, 5) == -3


def test_subtract():
    assert subtract(-7, -5) == -2


def divide(a,b):
    if b == 0:
        raise ValueError("Can't divide by zero")
    return a/b


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(3, 0)


# lab exercise 2
def test_valid_password():
    assert validate_password("Peter$Pan") == True


def test_short_password():
    assert validate_password("pan") == False


def test_no_special_character():
    assert validate_password("peterpan") == False


# lab exercise 3
@pytest.mark.parametrize(
    "n, expected",
    [
        (8, True),
        (-5, False),
        (0, False),
        (-12, True),
        (11, False),
    ],
)
def test_is_even(n, expected):
    assert is_even(n) == expected