"""
* Assignment: File Write Non-Str
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Write `DATA` to file `FILE`
    3. Check in your operating system if data was written correctly
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz `DATA` do pliku `FILE`
    3. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `[str(x) for x in ...]`
    * `','.join(...)`
    * Add newline `\n` at the end of line and file

Tests:
    >>> open(FILE).read()
    '5.1,3.5,1.4,0.2,setosa\\n'
    >>> from os import remove
    >>> remove(FILE)
"""


# Given
FILE = r'_temporary.txt'
DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')


# Solution
data = ','.join(str(x) for x in DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(data)
