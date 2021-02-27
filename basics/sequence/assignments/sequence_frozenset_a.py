"""
* Assignment: Sequence Frozenset Create
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create frozenset `result` with elements:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz frozenset `result` z elementami:
        a. `'a'`
        b. `1`
        c. `2.2`
    2. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'frozenset'>
    >>> len(result)
    3
    >>> 'a' in result
    True
    >>> 1 in result
    True
    >>> 2.2 in result
    True
"""

# Solution
result = frozenset({'a', 1, 2.2})
