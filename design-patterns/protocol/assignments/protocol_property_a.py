"""
* Assignment: Protocol Property Getter
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `Point` with `x`, `y`, `z` attributes
    3. Define property `position` in class `Point`
    4. Accessing `position` returns `(x, y, z)`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę `Point` z atrybutami `x`, `y`, `z`
    3. Zdefiniuj property `position` w klasie `Point`
    4. Dostęp do `position` zwraca `(x, y, z)`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> pt = Point(x=1, y=2, z=3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)
    >>> pt.position
    (1, 2, 3)
"""


# Given
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    z: int


# Solution
@dataclass
class Point:
    x: int
    y: int
    z: int

    @property
    def position(self):
        return self.x, self.y, self.z
