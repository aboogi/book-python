"""
* Assignment: ControlFlow Exception Except
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. Ask user to input temperature in Kelvins
    2. Try converting temperature to `float`
    3. If unsuccessful, then print 'Invalid temperature' and exit with status code 1

Polish:
    1. Poproś użytkownika o wprowadzenie temperatury w Kelwinach
    2. Spróbuj skonwertować temperaturę do `float`
    3. Jeżeli się nie uda to wypisz 'Invalid temperature' i wyjdź z kodem błędu 1

Tests:
    TODO: Doctests
    TODO: Input Stub
"""


# Given
temperature = input('Type temperature: ')


# Solution
try:
    float(temperature)
except ValueError:
    print('Invalid temperature')
    exit(1)
