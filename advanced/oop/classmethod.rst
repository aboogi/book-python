OOP Classmethod
===============


Rationale
---------
* Using class as namespace
* Will pass class as a first argument
* ``self`` is not required


Syntax
------
Dynamic methods:

>>> class MyClass:
...     def mymethod(self):
...         pass

Static methods:

>>> class MyClass:
...     @staticmethod
...     def mymethod():
...         pass

Class methods:

>>> class MyClass:
...     @classmethod
...     def mymethod(cls):
...         pass


Manifestation
-------------
>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class User:
...     firstname: str
...     lastname: str
...
...     @staticmethod
...     def from_json(data):
...         data = json.loads(data)
...         return User(**data)
>>>
>>>
>>> User.from_json('{"firstname": "Jan", "lastname": "Twardowski"}')
User(firstname='Jan', lastname='Twardowski')

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     @staticmethod
...     def from_json(data):
...         data = json.loads(data)
...         return User(**data)
>>>
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>>
>>> data = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>> result = User.from_json(data)
>>>
>>> print(result)
User(firstname='Jan', lastname='Twardowski')

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     @classmethod
...     def from_json(cls, data):
...         data = json.loads(data)
...         return cls(**data)
>>>
>>> @dataclass
... class User(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>>
>>> data = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>> result = User.from_json(data)
>>>
>>> print(result)
User(firstname='Jan', lastname='Twardowski')


Use Cases - 0x01
----------------
* Singleton

>>> class Singleton:
...     _instance: object
...
...     @classmethod
...     def get_instance(cls):
...         if not hasattr(cls, '_instance'):
...             cls._instance = object.__new__(cls)
...         return cls._instance
>>>
>>>
>>> class Astronaut(Singleton):
...     pass
>>>
>>> class Cosmonaut(Singleton):
...     pass
>>>
>>>
>>> astro = Astronaut.get_instance()
>>> cosmo = Cosmonaut.get_instance()
>>>
>>>
>>> print(astro)  # doctest: +SKIP
<__main__.Astronaut object at 0x102453ee0>
>>>
>>> print(cosmo)  # doctest: +SKIP
<__main__.Cosmonaut object at 0x102453ee0>


Use Cases - 0x02
----------------
* JSONMixin

>>> import json
>>> from dataclasses import dataclass
>>>
>>>
>>> class JSONMixin:
...     @classmethod
...     def from_json(cls, data):
...         data = json.loads(data)
...         return cls(**data)
>>>
>>> @dataclass
... class Guest(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>> @dataclass
... class Admin(JSONMixin):
...     firstname: str
...     lastname: str
>>>
>>>
>>> DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'
>>>
>>> Guest.from_json(DATA)
Guest(firstname='Jan', lastname='Twardowski')
>>>
>>> Admin.from_json(DATA)
Admin(firstname='Jan', lastname='Twardowski')


Use Case - 0x03
---------------
* Interplanetary time

>>> # myapp/time.py
>>> class AbstractTime:
...     tzname: str
...     tzcode: str
...
...     def __init__(self, date, time):
...         ...
...
...     @classmethod
...     def parse(cls, text):
...         result = {'date': ..., 'time': ...}
...         return cls(**result)
>>>
>>> class MartianTime(AbstractTime):
...     tzname = 'Coordinated Mars Time'
...     tzcode = 'MTC'
>>>
>>> class LunarTime(AbstractTime):
...     tzname = 'Lunar Standard Time'
...     tzcode = 'LST'
>>>
>>> class EarthTime(AbstractTime):
...     tzname = 'Universal Time Coordinated'
...     tzcode = 'UTC'

>>> # myapp/settings.py
>>> from myapp.time import *  # doctest: +SKIP
>>>
>>> time = MartianTime

>>> # myapp/usage.py
>>> from myapp.settings import time  # doctest: +SKIP
>>>
>>> UTC = '1969-07-21T02:53:07Z'
>>>
>>> dt = time.parse(UTC)
>>> print(dt.tzname)
Coordinated Mars Time


Use Case - 0x04
---------------
* Interplanetary time

>>> # myapp/time.py
>>> class AbstractTime:
...     tzname: str
...     tzcode: str
...
...     def __init__(self, date, time):
...         ...
...
...     @classmethod
...     def parse(cls, text):
...         result = {'date': ..., 'time': ...}
...         return cls(**result)
>>>
>>> class MartianTime(AbstractTime):
...     tzname = 'Coordinated Mars Time'
...     tzcode = 'MTC'
>>>
>>> class LunarTime(AbstractTime):
...     tzname = 'Lunar Standard Time'
...     tzcode = 'LST'
>>>
>>> class EarthTime(AbstractTime):
...     tzname = 'Universal Time Coordinated'
...     tzcode = 'UTC'

>>> # myapp/settings.py
>>> # doctest: +SKIP
... import myapp.time
... from myapp.time import *
... from os import getenv
...
... time = getattr(myapp.time, getenv('MISSION_TIME'))  # doctest: +SKIP

>>> # myapp/usage.py
>>> # doctest: +SKIP
... from myapp.settings import time
...
... UTC = '1969-07-21T02:53:07Z'
...
... dt = time.parse(UTC)
... print(dt.tzname)
Coordinated Mars Time


Assignments
-----------
.. literalinclude:: assignments/oop_classmethod_a.py
    :caption: :download:`Solution <assignments/oop_classmethod_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_classmethod_b.py
    :caption: :download:`Solution <assignments/oop_classmethod_b.py>`
    :end-before: # Solution
