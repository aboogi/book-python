"""
* Assignment: Sequence Slice Substr
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Use `str.find()` and slicing
    3. Print `TEXT` without text in `REMOVE`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj `str.find()` oraz wycinania
    3. Wypisz `TEXT` bez tekstu z `REMOVE`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'str'>
    >>> result
    'We choose the Moon!'
"""


# Given
TEXT = 'We choose to go to the Moon!'
REMOVE = 'to go to '


# Solution
a = TEXT.find(REMOVE)   # 10
b = a + len(REMOVE)     # 19
result = TEXT[:a] + TEXT[b:]
