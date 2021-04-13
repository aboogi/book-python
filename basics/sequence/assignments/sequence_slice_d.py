"""
* Assignment: Sequence Slice Split
* Complexity: easy
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Separate header from data
    3. Write header (first line) to `header` variable
    4. Write data without header to `data` variable
    5. Calculate pivot point: number records in `data` multiplied by PERCENT
    (division ratio below)
    6. Divide `data` into two lists:
        a. `train`: 60% - training data
        b. `test`: 40% - testing data
    7. From `data` write training data from start to pivot
    8. From `data` write test data from pivot to end
    9. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Odseparuj nagłówek od danych
    3. Zapisz nagłówek (pierwsza linia) do zmiennej `header`
    4. Zapisz dane bez nagłówka do zmiennej `data`
    5. Wylicz punkt podziału: ilość rekordów w `data` razy PROCENT (
    proporcja podziału poniżej)
    6. Podziel `data` na dwie listy:
        a. `train`: 60% - dane do uczenia
        b. `test`: 40% - dane do testów
    7. Z `data` zapisz do uczenia rekordy od początku do punktu podziału
    8. Z `data` zapisz do testów rekordy od punktu podziału do końca
    9. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert header is not Ellipsis, 'Assignment solution must be in `header` instead of ... (Ellipsis)'
    >>> assert data is not Ellipsis, 'Assignment solution must be in `data` instead of ... (Ellipsis)'
    >>> assert train is not Ellipsis, 'Assignment solution must be in `train` instead of ... (Ellipsis)'
    >>> assert test is not Ellipsis, 'Assignment solution must be in `test` instead of ... (Ellipsis)'
    >>> assert type(header) is tuple, 'Variable `header` has invalid type, should be tuple'
    >>> assert type(train) is list, 'Variable `train` has invalid type, should be list'
    >>> assert type(train) is list, 'Variable `train` has invalid type, should be list'
    >>> assert type(test) is list, 'Variable `test` has invalid type, should be list'
    >>> assert all(type(x) is tuple for x in train), 'All elements in `train` should be tuple'
    >>> assert all(type(x) is tuple for x in test), 'All elements in `test` should be tuple'
    >>> assert header not in train, 'Header should not be in `train`'
    >>> assert header not in test, 'Header should not be in `test`'

    >>> header  # doctest: +NORMALIZE_WHITESPACE
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')

    >>> train  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa')]

    >>> test  # doctest: +NORMALIZE_WHITESPACE
    [(7.0, 3.2, 4.7, 1.4, 'versicolor'),
     (7.6, 3.0, 6.6, 2.1, 'virginica'),
     (4.9, 3.0, 1.4, 0.2, 'setosa'),
     (4.9, 2.5, 4.5, 1.7, 'virginica')]
"""

# Given
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (4.9, 2.5, 4.5, 1.7, 'virginica')]

header = ...  # tuple with row at index 0 from DATA
data = ...  # list of tuple with rows at all the other indexes from DATA
train = ...  # first 60% from data
test = ...  # last 40% from data

# Solution
ratio = 0.6  # 60%
header = DATA[0]
data = DATA[1:]

pivot = int(len(data) * ratio)
train = data[:pivot]
test = data[pivot:]
