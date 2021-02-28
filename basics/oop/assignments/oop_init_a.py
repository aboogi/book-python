"""
* Assignment: OOP Init Print
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create one class `Echo`
    2. Value `text` must be passed at the initialization
    3. At initialization instance print `text`
    4. Do not store values in the instances (only print on instance creation)
    5. Do not use `@dataclass`
    6. Compare result with "Tests" section (see below)

Polish:
    1. Stwórz jedną klasę `Echo`
    2. Wartość `text` maja być podawana przy inicjalizacji
    3. Przy inicjalizacji instancja wypisuje `text`
    4. Nie przechowuj informacji w instancjach (tylko wypisz przy inicjalizacji)
    5. Nie używaj `@dataclass`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> _ = Echo('hello')
    hello
    >>> _ = Echo('world')
    world
    >>> result = Echo('Test')
    Test
    >>> result.__dict__
    {}
"""


# Solution
class Echo:
    def __init__(self, text):
        print(text)


