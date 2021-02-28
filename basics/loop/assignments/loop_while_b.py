"""
* Assignment: Loop While to Str
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create `result: str`
    3. Use `while` to iterate over `DATA`
    4. Add current element of `DATA` to `result`
    5. Do not use `str.join()`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `result: str`
    3. Użyj `while` do iterowania po `DATA`
    4. Dodaj obecny element z `DATA` do `result`
    5. Nie używaj `str.join()`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop

Tests:
    >>> type(result)
    <class 'str'>
    >>> result
    'hello'
"""


# Given
DATA = ['h', 'e', 'l', 'l', 'o']
result: str = ''


# Solution
i = 0

while i < len(DATA):
    result += DATA[i]
    i += 1
