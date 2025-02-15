OOP Access Modifiers
====================


Rationale
---------
* Attributes and methods are always public
* No protected and private keywords
* Protecting is only by convention [#pydocprivatevar]_

Attributes:

    * ``name`` - public attribute
    * ``_name`` - protected attribute (non-public by convention)
    * ``__name`` - private attribute (name mangling)
    * ``__name__`` - system attribute
    * ``name_`` - avoid name collision

Methods:

    * ``name(self)`` - public method
    * ``_name(self)`` - protected method (non-public by convention)
    * ``__name(self)`` - private method (name mangling)
    * ``__name__(self)`` - system method
    * ``name_(self)`` - avoid name collision


Example
-------
>>> class Public:
...     firstname: str
...     lastname: str
>>>
>>> class Protected:
...     _firstname: str
...     _lastname: str
>>>
>>> class Private:
...     __firstname: str
...     __lastname: str


DataClasses
-----------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Public:
...     firstname: str
...     lastname: str
>>>
>>>
>>> @dataclass
... class Protected:
...     _firstname: str
...     _lastname: str
>>>
>>>
>>> @dataclass
... class Private:
...     __firstname: str
...     __lastname: str


Public Attribute
----------------
* ``name`` - public attribute

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> vars(astro)
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> print(astro.firstname)
Mark
>>>
>>> print(astro.lastname)
Watney


Protected Attribute
-------------------
* ``_name`` - protected attribute (non-public by convention)

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     _firstname: str
...     _lastname: str
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')

To list all the attributes once again we can use `vars()`:

>>> vars(astro)
{'_firstname': 'Mark', '_lastname': 'Watney'}

Python will allow the following statement, however your IDE should warn you
"Access to a protected member _firstname of a class":

>>> print(astro._firstname)
Mark
>>>
>>> print(astro._lastname)
Watney


Private Attribute
-----------------
* ``__name`` - private attribute (name mangling)

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     __firstname: str
...     __lastname: str
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> vars(astro)
{'_Astronaut__firstname': 'Mark', '_Astronaut__lastname': 'Watney'}
>>>
>>> print(astro._Astronaut__firstname)
Mark
>>>
>>> print(astro._Astronaut__lastname)
Watney
>>>
>>> print(astro.__firstname)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__firstname'
>>>
>>> print(astro.__lastname)
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__lastname'



Name Mangling
-------------
>>> class Person:
...     def hello(self):
...         return 'hello Person'
>>>
>>>
>>> class Astronaut(Person):
...     def hello(self):
...         return 'hello Astronaut'
>>>
>>>
>>> astro = Astronaut()
>>> astro.hello()
'hello Astronaut'

>>> class Person:
...     def __hello(self):
...         return 'hello Person'
>>>
>>>
>>> class Astronaut(Person):
...     def __hello(self):
...         return 'hello Astronaut'
>>>
>>>
>>> astro = Astronaut()
>>> astro._Astronaut__hello()
'hello Astronaut'
>>> astro._Person__hello()
'hello Person'

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Person:
...     __firstname: str
...     __lastname: str
>>>
>>> @dataclass
... class Astronaut(Person):
...     __firstname: str
...     __lastname: str
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>> TypeError: Astronaut.__init__() missing 2 required positional arguments: '_Astronaut__firstname' and '_Astronaut__lastname'
>>>
>>> astro = Astronaut('Mark', 'Watney', 'Melissa', 'Lewis')
>>>
>>> vars(astro)
{'_Person__firstname': 'Mark',
 '_Person__lastname': 'Watney',
 '_Astronaut__firstname': 'Melissa',
 '_Astronaut__lastname': 'Lewis'}


Show Attributes
---------------
* ``vars()`` display ``obj.__dict__``

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self._firstname = firstname
...         self._lastname = lastname
...         self.publicname = f'{firstname} {lastname[0]}.'
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> vars(astro)
{'_firstname': 'Mark', '_lastname': 'Watney', 'publicname': 'Mark W.'}
>>>
>>> public_attributes = {attribute: value
...                      for attribute, value in vars(astro).items()
...                      if not attribute.startswith('_')}
>>>
>>> protected_attributes = {attribute: value
...                         for attribute, value in vars(astro).items()
...                         if attribute.startswith('_')}
>>>
>>>
>>> print(public_attributes)
{'publicname': 'Mark W.'}
>>>
>>> print(protected_attributes)
{'_firstname': 'Mark', '_lastname': 'Watney'}


System Attributes
-----------------
* ``__name__`` - Current module
* ``obj.__class__``
* ``obj.__dict__`` - Getting dynamic fields and values
* ``obj.__doc__`` - Docstring
* ``obj.__annotations__`` - Type annotations of an object
* ``obj.__module__``

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> vars(astro)
{'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> print(astro.__dict__)
{'firstname': 'Mark', 'lastname': 'Watney'}


Protected Method
----------------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     _firstname: str
...     _lastname: str
...
...     def _get_fullname(self):
...         return f'{self._firstname} {self._lastname}'
...
...     def get_publicname(self):
...         return f'{self._firstname} {self._lastname[0]}.'
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>> astro._get_fullname()  # IDE should warn: "Access to a protected member _get_fullname of a class"
'Mark Watney'


Private Method
--------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self._firstname = firstname
...         self._lastname = lastname
...
...     def __get_fullname(self):
...         return f'{self._firstname} {self._lastname}'
...
...     def get_publicname(self):
...         return f'{self._firstname} {self._lastname[0]}.'
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> astro.__get_fullname()
Traceback (most recent call last):
AttributeError: 'Astronaut' object has no attribute '__get_fullname'
>>>
>>> astro._Astronaut__get_fullname()  # IDE should warn: "Access to a protected member _Astronaut__get_fullname of a class"
'Mark Watney'


System Method
-------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self._firstname = firstname
...         self._lastname = lastname
...
...     def __str__(self):
...         return 'stringification'
...
...     def __repr__(self):
...         return 'representation'
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> print(str(astro))
stringification
>>>
>>> print(repr(astro))
representation


Show Methods
------------
* ``dir()``

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self._firstname = firstname
...         self._lastname = lastname
...
...     def __get_fullname(self):
...         return f'{self._firstname} {self._lastname}'
...
...     def get_publicname(self):
...         return f'{self._firstname} {self._lastname[0]}.'
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> print(dir(astro))  # doctest: +NORMALIZE_WHITESPACE
['_Astronaut__get_fullname', '__class__', '__delattr__', '__dict__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 '__weakref__', '_firstname', '_lastname', 'get_publicname']
>>>
>>> [method for method in dir(astro) if callable(getattr(astro, method))]  # doctest: +NORMALIZE_WHITESPACE
['_Astronaut__get_fullname', '__class__', '__delattr__', '__dir__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', 'get_publicname']
>>>
>>> public_methods = [method
...                   for method in dir(astro)
...                   if callable(getattr(astro, method))
...                   and not method.startswith('_')]
>>>
>>> protected_methods = [method
...                      for method in dir(astro)
...                      if callable(getattr(astro, method))
...                      and method.startswith('_')]
>>>
>>> private_methods = [method
...                    for method in dir(astro)
...                    if callable(getattr(astro, method))
...                    and method.startswith(f'_{astro.__class__.__name__}')]



References
----------
.. [#pydocprivatevar] https://docs.python.org/3/tutorial/classes.html#private-variables


Assignments
-----------
.. literalinclude:: assignments/oop_accessmodifiers_a.py
    :caption: :download:`Solution <assignments/oop_accessmodifiers_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_accessmodifiers_b.py
    :caption: :download:`Solution <assignments/oop_accessmodifiers_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_accessmodifiers_c.py
    :caption: :download:`Solution <assignments/oop_accessmodifiers_c.py>`
    :end-before: # Solution
