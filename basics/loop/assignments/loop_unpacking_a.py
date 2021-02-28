"""
* Assignment: Loop Unpacking Months
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Use `enumerate()` to convert `MONTH` into dict:
        a. Keys: month number
        b. Values: month name
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj `enumerate()` do konwersji `MONTH` w słownik:
        a. klucz: numer miesiąca
        b. wartość: nazwa miesiąca
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'dict'>
    >>> assert all(type(x) is int for x in result.keys())
    >>> assert all(type(x) is str for x in result.values())
    >>> assert all(x in result.keys() for x in range(1, 13))
    >>> assert all(x in result.values() for x in MONTHS)
    >>> 13 not in result
    True
    >>> 0 not in result
    True
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {1: 'January',
     2: 'February',
     3: 'March',
     4: 'April',
     5: 'May',
     6: 'June',
     7: 'July',
     8: 'August',
     9: 'September',
     10: 'October',
     11: 'November',
     12: 'December'}
"""


# Given
MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

result: dict = {}


# Solution
for i, month in enumerate(MONTHS, start=1):
    result[i] = month
