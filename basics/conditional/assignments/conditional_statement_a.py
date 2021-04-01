"""
* Assignment: Conditional Statement Adult
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Ask user to input age
    2. User will pass only valid `int`
    3. Print whether user is adult

Polish:
    1. Poproś użytkownika o wprowadzenie swojego wieku
    2. Użytkownika poda tylko poprawne `int`
    3. Wypisz czy użytkownik jest pełnoletni

Tests:
    >>> type(result)
    <class 'str'>
    >>> result in ('Adult', 'Young')
    True
"""

# Mock input() built-in function
from unittest.mock import MagicMock
input = MagicMock(return_value='21')


# Given
ADULT = 18
age = input('What is your age?: ')

result = ...  # str: Whether 'Young' or 'Adult'

# Solution
if int(age) >= ADULT:
    result = 'Adult'
else:
    result = 'Young'
