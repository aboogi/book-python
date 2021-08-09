Annotation OOP
==============


Rationale
---------
* All classes are types
* Always depend upon abstraction not an implementation (SOLID Dependency Inversion Principle)
* More information in `OOP SOLID`

.. code-block:: python

    class Astronaut:
        pass


    mark: Astronaut = Astronaut()

.. code-block:: python

    class Cache:
        pass

    class DatabaseCache(Cache):
        pass

    class MemoryCache(Cache):
        pass

    class FilesystemCache(Cache):
        pass


    db: Cache = DatabaseCache()
    mem: Cache = MemoryCache()
    fs: Cache = FilesystemCache()


Attributes
----------
.. code-block:: python

    class Point:
        x: int
        y: int

.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str

Warning! - Do not confuse this with static fields:

    .. code-block:: python

        class Astronaut:
            firstname: str = 'Mark'
            lastname: str = 'Watney'


Method Return Types
-------------------
.. code-block:: python

    class Astronaut:
        def say_hello(self) -> str:
            return 'My name... José Jiménez'


    mark: Astronaut = Astronaut()
    mark.say_hello()
    # 'My name... José Jiménez'

.. code-block:: python

    class Point:
        def get_coordinates(self) -> tuple[int, int]:
            return 1, 2


    pt: Point = Point()
    pt.get_coordinates()
    # (1, 2)


Required Method Arguments
-------------------------
.. code-block:: python

    class Point:
        x: int
        y: int

        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str

        def __init__(self, firstname: str, lastname: str) -> None:
            self.firstname: str = firstname
            self.lastname: str = lastname


Optional Method Arguments
-------------------------
.. code-block:: python

    class Point:
        x: int
        y: int

        def __init__(self, x: int = 0, y: int = 0) -> None:
            self.x = x
            self.y = y

        def set_coordinates(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

        def get_coordinates(self) -> tuple[int, int]:
            return self.x, self.y


    pt: Point = Point()
    pt.set_coordinates(1, 2)
    pt.get_coordinates()
    # (1, 2)

.. code-block:: python

    class Point:
        x: int
        y: int

        def __init__(self, x: int = 0, y: int = 0) -> None:
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return f'Point(x={self.x}, y={self.y})'


Classes as Method Arguments
---------------------------
.. code-block:: python

    class Point:
        x: int
        y: int

        def __init__(self, x: int = 0, y: int = 0) -> None:
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return f'Point(x={self.x}, y={self.y})'


    class Position:
        position: Point

        def __init__(self, initial_position: Point = Point()) -> None:
            self.position = initial_position

        def get_coordinates(self) -> Point:
            return self.position


    pos: Position = Position()

    pos.get_coordinates()
    # <__main__.Point object at 0x11c5531c0>

    print(pos.get_coordinates())
    # Point(x=0, y=0)


Aggregation
-----------
.. code-block:: python

    class Mission:
        year: int
        name: str


    class Astronaut:
        firstname: str
        lastname: str
        mission: list[Mission]


Nested
------
.. code-block:: python

    class Iris:
        features: list[float]
        label: str

        def __init__(self, features: list[float], label: str) -> None:
            self.features = features
            self.label = label

    data: list[Iris] = [
        Iris([4.7, 3.2, 1.3, 0.2], 'setosa'),
        Iris([7.0, 3.2, 4.7, 1.4], 'versicolor'),
        Iris([7.6, 3.0, 6.6, 2.1], 'virginica'),
    ]


Final Class
-----------
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing

.. code-block:: python

    from typing import final


    @final
    class Astronaut:
        pass

Error: Cannot inherit from final class "Base":

.. code-block:: python

    from typing import final


    @final
    class Astronaut:
        pass

    class Pilot(Astronaut):
        pass


Final Method
------------
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing

.. code-block:: python

    from typing import final


    class Astronaut:

        @final
        def say_hello(self) -> None:
            pass


Error: Cannot override final attribute "foo" (previously declared in base class "Base"):

.. code-block:: python

    from typing import final


    class Astronaut:
        @final
        def say_hello(self) -> None:
            pass

    class Pilot(Astronaut):
        def say_hello(self) -> None:    # Error: Cannot override final attribute
            pass


Final Attribute
---------------
.. code-block:: python

    from typing import Final


    class Position:
        x: Final[int]
        y: Final[int]

        def __init__(self) -> None:
            self.x = 1
            self.y = 2

Error: final attribute (``y``) without an initializer:

.. code-block:: python

    from typing import Final


    class Position:
        x: Final[int]
        y: Final[int]       # Error: final attribute 'y' without an initializer

        def __init__(self) -> None:
            self.x = 1

Error: can't override a final attribute:

.. code-block:: python

    from typing import Final


    class Settings:
        RESOLUTION_X_MIN: Final[int] = 0
        RESOLUTION_X_MAX: Final[int] = 1024
        RESOLUTION_Y_MIN: Final[int] = 0
        RESOLUTION_Y_MAX: Final[int] = 768


    class Game(Settings):
        RESOLUTION_X_MIN = 3        # Error: can't override a final attribute

Error: can't override a final attribute:

.. code-block:: python

    from typing import Final


    class Hero:
        DAMAGE_MIN: Final[int] = 10
        DAMAGE_MAX: Final[int] = 20


    Hero.DAMAGE_MIN = 1             # Error: can't override a final attribute


Forward References
------------------
.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str
        friends: list[Astronaut]  # Error, cannot reference to class which is still being defined

.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str
        friends: list['Astronaut']

Since Python 3.11: :pep:`563` -- Postponed Evaluation of Annotations

.. code-block:: python

    class Astronaut:
        firstname: str
        lastname: str
        friends: list[Astronaut]   # This code will work only in Python 3.11

In Python 3.7, 3.8, 3.9, 3.10 you can get this behavior by importing it from ``__future__``:

.. code-block:: python

    from __future__ import annotations


    class Astronaut:
        firstname: str
        lastname: str
        friends: list[Astronaut]


Further Reading
---------------
* What’s New In Python 3.10: https://docs.python.org/dev/whatsnew/3.10.html
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`
