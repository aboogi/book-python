Type Annotation OOP
===================


Rationale
---------
* All classes are types

>>> class Point:
...     x: int
...     y: int
...
...     def set_coordinates(self, x: int, y: int) -> None:
...         self.x = x
...         self.y = y
...
...     def get_coordinates(self) -> tuple[int,int]:
...         return self.x, self.y
>>>
>>>
>>> pt: Point = Point()
>>> pt.set_coordinates(1, 2)
>>> pt.get_coordinates()
(1, 2)


Dynamic Attributes
------------------
>>> class Astronaut:
...     firstname: str
...     lastname: str


Static Attributes
-----------------
* ClassVar indicates that a given attribute is intended to be used as a class variable and should not be set on instances of that class.
* https://docs.python.org/3/library/typing.html#typing.ClassVar

>>> from typing import ClassVar
>>>
>>>
>>> class Astronaut:
...     AGE_MIN: ClassVar[int] = 30
...     AGE_MAX: ClassVar[int] = 50


Method Return Type
------------------
>>> class Astronaut:
...     def say_hello(self) -> str:
...         return 'My name... José Jiménez'


Required Method Arguments
-------------------------
>>> class Astronaut:
...     def say_hello(self, name: str) -> str:
...         return f'My name... {name}'


Optional Method Arguments
-------------------------
>>> class Astronaut:
...     def say_hello(self, name: str = 'Mark Watney') -> str:
...         return f'My name... {name}'


Init Method
-----------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname: str, lastname: str) -> None:
...         self.firstname = firstname
...         self.lastname = lastname


Composition
-----------
>>> class Person:
...     firstname: str
...     lastname: str
>>>
>>>
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     friends: list[Person]


Circular Dependency
-------------------
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     friends: list[Astronaut]
...
Traceback (most recent call last):
NameError: name 'Astronaut' is not defined

>>> class Astronaut:
...     firstname: str
...     lastname: str
...     friends: list['Astronaut']

Since Python 3.7:

>>> from __future__ import annotations
>>>
>>>
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     friends: list[Astronaut]


Instance
--------
>>> class Astronaut:
...     pass
>>>
>>>
>>> mark: Astronaut = Astronaut()
>>> melissa: Astronaut = Astronaut()


Dependency Inversion Principle
------------------------------
* Always depend upon abstraction not an implementation
* More information in `OOP SOLID`

>>> class Person:
...     pass
>>>
>>>
>>> class Astronaut(Person):
...     pass
>>>
>>>
>>> mark: Person = Astronaut()
>>> melissa: Person = Astronaut()


Final Class
-----------
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing
* There is no runtime checking of these properties

The following code demonstrates how to use ``@final`` decorator to mark
class as final:

>>> from typing import final
>>>
>>>
>>> @final
... class Astronaut:
...     pass


Final Method
------------
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing
* There is no runtime checking of these properties

The following code demonstrates how to use ``@final`` decorator to mark
method as final:

>>> from typing import final
>>>
>>>
>>> class Astronaut:
...     @final
...     def say_hello(self) -> None:
...         pass


Final Attribute
---------------
* A special typing construct to indicate to type checkers that a name cannot be re-assigned or overridden in a subclass
* There is no runtime checking of these properties
* https://docs.python.org/3/library/typing.html#typing.Final

The following code demonstrates how to use ``Final`` class to mark
attribute as final:

>>> from typing import Final
>>>
>>>
>>> class Astronaut:
...     firstname: Final[str]
...     lastname: Final[str]
...
...     def __init__(self) -> None:
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'


Errors
------
Error: 'Astronaut' is marked as ``@final`` and should not be subclassed:

>>> from typing import final
>>>
>>>
>>> @final
... class Person:
...     pass
>>>
>>> class Astronaut(Person):
...     pass

The following code will yield with an error: 'Person.say_hello' is marked
as ``@final`` and should not be overridden:

>>> from typing import final
>>>
>>>
>>> class Person:
...     @final
...     def say_hello(self) -> None:
...         pass
>>>
>>> class Astronaut(Person):
...     def say_hello(self) -> None:
...         pass

The following code will yield with an error: final attribute (``y``) without
an initializer:

>>> from typing import Final
>>>
>>>
>>> class Astronaut:
...     firstname: Final[str]
...     lastname: Final[str]  # error: not initialized
...
...     def __init__(self) -> None:
...         self.firstname = 'Mark'

The following code will yield with an error: can't override a final
attribute:

>>> from typing import Final
>>>
>>>
>>> class Astronaut:
...     AGE_MIN: Final[int] = 30
...     AGE_MAX: Final[int] = 50
>>>
>>>
>>> Astronaut.AGE_MAX = 65 # error: can't override

The following code will yield with an error: can't override a final
attribute:

>>> from typing import Final
>>>
>>>
>>> class Astronaut:
...     AGE_MIN: Final[int] = 30
...     AGE_MAX: Final[int] = 50
>>>
>>>
>>> class VeteranAstronaut(Astronaut):
...     AGE_MAX = 65  # error: can't override


Use Case - 0x01
---------------
>>> class Astronaut:
...     def get_name(self) -> tuple[str, str]:
...         return 'Mark', 'Watney'


Use Case - 0x02
---------------
* SOLID Dependency Inversion Principle

>>> class Cache:
...     pass
>>>
>>> class DatabaseCache(Cache):
...     pass
>>>
>>> class MemoryCache(Cache):
...     pass
>>>
>>> class FilesystemCache(Cache):
...     pass
>>>
>>>
>>> db: Cache = DatabaseCache()
>>> mem: Cache = MemoryCache()
>>> fs: Cache = FilesystemCache()


Use Case - 0x03
---------------
>>> class Point:
...     x: int
...     y: int
...
...     def set_coordinates(self, x: int, y: int) -> None:
...         self.x = x
...         self.y = y
...
...     def get_coordinates(self) -> tuple[int,int]:
...         return self.x, self.y
>>>
>>>
>>> pt: Point = Point()
>>> pt.set_coordinates(1, 2)
>>> pt.get_coordinates()
(1, 2)


Use Case - 0x04
---------------
>>> class Point:
...     def __init__(self, x: int = 0, y: int = 0) -> None:
...         self.x = x
...         self.y = y
...
...     def __str__(self) -> str:
...         return f'Point(x={self.x}, y={self.y})'
>>>
>>>
>>> class Position:
...     def __init__(self, initial_position: Point = Point()) -> None:
...         self.position = initial_position
...
...     def get_coordinates(self) -> Point:
...         return self.position
>>>
>>>
>>> pos: Position = Position()
>>>
>>> pos.get_coordinates()  # doctest: +ELLIPSIS
<Point object at 0x...>
>>>
>>> print(pos.get_coordinates())
Point(x=0, y=0)


Use Case - 0x05
---------------
>>> class Iris:
...     def __init__(self, features: list[float], label: str) -> None:
...         self.features: list[float] = features
...         self.label: str = label
>>>
>>> data: list[Iris] = [
...     Iris([4.7, 3.2, 1.3, 0.2], 'setosa'),
...     Iris([7.0, 3.2, 4.7, 1.4], 'versicolor'),
...     Iris([7.6, 3.0, 6.6, 2.1], 'virginica')]

>>> class Position:
...     x: Final[int]
...     y: Final[int]
...
...     def __init__(self) -> None:
...         self.x = 1
...         self.y = 2


Use Case - 0x06
---------------
* Immutable attributes (set only on init)

>>> from typing import Final
>>>
>>>
>>> class Position:
...     x: Final[int]
...     y: Final[int]
...
...     def __init__(self, x: int, y: int) -> None:
...         self.x = x
...         self.y = y


Use Case - 0x07
---------------
>>> from typing import Final
>>>
>>>
>>> class Settings:
...     RESOLUTION_X_MIN: Final[int] = 0
...     RESOLUTION_X_MAX: Final[int] = 1024
...     RESOLUTION_Y_MIN: Final[int] = 0
...     RESOLUTION_Y_MAX: Final[int] = 768


Use Case - 0x08
---------------
>>> from typing import Final
>>>
>>>
>>> class Hero:
...     DAMAGE_MIN: Final[int] = 10
...     DAMAGE_MAX: Final[int] = 20


Further Reading
---------------
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`
