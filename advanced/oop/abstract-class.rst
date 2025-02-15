OOP Abstract Class
==================


Rationale
---------
* Since Python 3.0: :pep:`3119` -- Introducing Abstract Base Classes
* Cannot instantiate
* Possible to indicate which method must be implemented by child
* Inheriting class must implement all methods
* Some methods can have implementation
* Python Abstract Base Classes [#pydocabc]_

.. glossary::

    abstract class
        Class which can only be inherited, not instantiated

    abstract method
        Method must be implemented in a subclass

    abstract static method
        Static method which must be implemented in a subclass


Syntax
------
* New class ``ABC`` has ``ABCMeta`` as its meta class.
* Using ``ABC`` as a base class has essentially the same effect as specifying ``metaclass=abc.ABCMeta``, but is simpler to type and easier to read.
* ``abc.ABC`` basically just an extra layer over ``metaclass=abc.ABCMeta``
* ``abc.ABC`` implicitly defines the metaclass for you

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class MyClass(ABC):
...
...     @abstractmethod
...     def mymethod(self):
...         pass


Abstract Method
---------------
>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Astronaut(ABC):
...     @abstractmethod
...     def say_hello(self):
...         pass
>>>
>>>
>>> astro = Astronaut()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Astronaut with abstract method say_hello

>>> from abc import ABCMeta, abstractmethod
>>>
>>>
>>> class Astronaut(metaclass=ABCMeta):
...     @abstractmethod
...     def say_hello(self):
...         pass
>>>
>>>
>>> astro = Astronaut()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Astronaut with abstract method say_hello


Abstract Property
-----------------
* ``abc.abstractproperty`` is deprecated since Python 3.3
* Use ``property`` with ``abc.abstractmethod`` instead

>>> from abc import ABC, abstractproperty
>>>
>>>
>>> class Monster(ABC):
...     @abstractproperty
...     def DAMAGE(self) -> int:
...         pass
>>>
>>>
>>> class Dragon(Monster):
...     DAMAGE: int = 10

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Monster(ABC):
...     @property
...     @abstractmethod
...     def DAMAGE(self) -> int:
...         pass
>>>
>>>
>>> class Dragon(Monster):
...     DAMAGE: int = 10

>>> from abc import ABC, abstractproperty
>>>
>>>
>>> class Monster(ABC):
...     @abstractproperty
...     def DAMAGE_MIN(self):
...         pass
...
...     @abstractproperty
...     def DAMAGE_MAX(self):
...         pass
>>>
>>>
>>> class Dragon(Monster):
...     DAMAGE_MIN: int = 10
...     DAMAGE_MAX: int = 20


Common Problems
---------------
In order to use Abstract Base Class you must create abstract method. Otherwise it won't prevent from instantiating:

>>> from abc import ABC
>>>
>>>
>>> class Astronaut(ABC):
...     pass
>>>
>>>
>>> astro = Astronaut()   # It will not raise an error, because there are no abstractmethods
>>>
>>> print('no errors')
no errors

The ``Human`` class does not inherits from ``ABC`` or has ``metaclass=ABCMeta``:

>>> from abc import abstractmethod
>>>
>>>
>>> class Human:
...     @abstractmethod
...     def get_name(self):
...         pass
>>>
>>>
>>> class Astronaut(Human):
...     pass
>>>
>>>
>>> astro = Astronaut()  # None abstractmethod is implemented in child class
>>>
>>> print('no errors')
no errors

Must implement all abstract methods:

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Human(ABC):
...     @abstractmethod
...     def get_name(self):
...         pass
...
...     @abstractmethod
...     def set_name(self):
...         pass
>>>
>>>
>>> class Astronaut(Human):
...     pass
>>>
>>>
>>> astro = Astronaut()  # None abstractmethod is implemented in child class
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Astronaut with abstract methods get_name, set_name

All abstract methods must be implemented in child class:

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Human(ABC):
...     @abstractmethod
...     def get_name(self):
...         pass
...
...     @abstractmethod
...     def set_name(self):
...         pass
>>>
>>>
>>> class Astronaut(Human):
...     def get_name(self):
...         return 'Mark Watney'
>>>
>>>
>>> astro = Astronaut()  # There are abstractmethods without implementation
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Astronaut with abstract method set_name

Problem - Child class has no abstract attribute (using ``abstractproperty``):

>>> from abc import ABC, abstractproperty
>>>
>>>
>>> class Monster(ABC):
...     @abstractproperty
...     def DAMAGE(self) -> int:
...         pass
>>>
>>> class Dragon(Monster):
...     pass
>>>
>>>
>>> d = Dragon()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Dragon with abstract method DAMAGE

Problem - Child class has no abstract attribute (using ``property`` and ``abstractmethod``):

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Monster(ABC):
...     @property
...     @abstractmethod
...     def DAMAGE(self) -> int:
...         pass
>>>
>>> class Dragon(Monster):
...     pass
>>>
>>>
>>> d = Dragon()
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Dragon with abstract method DAMAGE

Problem - Despite having defined property, the order of decorators (``abstractmethod`` and ``property`` is invalid). Should be reversed: first ``@property`` then ``@abstractmethod``:

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Monster(ABC):
...     @property
...     @abstractmethod
...     def DAMAGE(self) -> int:
...         pass
>>>
>>>
>>> class Dragon(Monster):
...     DAMAGE: int = 10
>>>
>>>
>>> d = Dragon()

``abc`` is common name and it is very easy to create file, variable lub module with the same name as the library, hence overwrite it. In case of error. Check all entries in ``sys.path`` or ``sys.modules['abc']`` to find what is overwriting it:

>>> from pprint import pprint
>>> import sys
>>>
>>>
>>> sys.modules['abc']  # doctest: +ELLIPSIS
<module 'abc' from '...'>
>>>
>>> pprint(sys.path)  # doctest: +SKIP
['/Applications/PyCharm 2021.1 EAP.app/Contents/plugins/python/helpers/pydev',
 '/Users/watney/book-python',
 '/Applications/PyCharm 2021.3 EAP.app/Contents/plugins/python/helpers/pycharm_display',
 '/Applications/PyCharm 2021.3 EAP.app/Contents/plugins/python/helpers/third_party/thriftpy',
 '/Applications/PyCharm 2021.3 EAP.app/Contents/plugins/python/helpers/pydev',
 '/usr/local/Cellar/python@3.10/3.10.0/Frameworks/Python.framework/Versions/3.10/lib/python310.zip',
 '/usr/local/Cellar/python@3.10/3.10.0/Frameworks/Python.framework/Versions/3.10/lib/python3.10',
 '/usr/local/Cellar/python@3.10/3.10.0/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload',
 '/Users/watney/.virtualenvs/python-3.10/lib/python3.10/site-packages',
 '/Applications/PyCharm 2021.3 EAP.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend',
 '/Users/watney/book-python',
 '/Users/watney/book-python/_tmp']


Use Case - 0x01
---------------
Abstract Class:

>>> from abc import ABC, abstractmethod
>>>
>>>
>>> class Document(ABC):
...     def __init__(self, filename):
...         self.filename = filename
...         # with open(filename, mode='rb') as file:
...         #     self.content = file.read()
...
...     @abstractmethod
...     def display(self):
...         pass
>>>
>>>
>>> class PDFDocument(Document):
...     def display(self):
...         """display self.content as PDF Document"""
>>>
>>> class WordDocument(Document):
...     def display(self):
...         """display self.content as Word Document"""
>>>
>>>
>>> file1 = PDFDocument('myfile.pdf')
>>> file1.display()
>>>
>>> file2 = Document('myfile.txt')
Traceback (most recent call last):
TypeError: Can't instantiate abstract class Document with abstract method display


Use Case - 0x02
---------------
>>> from abc import ABCMeta, abstractmethod
>>>
>>>
>>> class UIElement(metaclass=ABCMeta):
...     def __init__(self, name):
...         self.name = name
...
...     @abstractmethod
...     def render(self):
...         pass
>>>
>>>
>>> class TextInput(UIElement):
...     def render(self):
...         print(f'Rendering {self.name} TextInput')
>>>
>>>
>>> class Button(UIElement):
...     def render(self):
...         print(f'Rendering {self.name} Button')
>>>
>>>
>>> def render(component: list[UIElement]):
...     for element in component:
...         element.render()
>>>
>>>
>>> login_window = [
...     TextInput(name='Username'),
...     TextInput(name='Password'),
...     Button(name='Submit'),
... ]
>>>
>>> render(login_window)
Rendering Username TextInput
Rendering Password TextInput
Rendering Submit Button


Further Reading
---------------
* https://docs.python.org/dev/library/collections.abc.html#collections-abstract-base-classes
* https://www.youtube.com/watch?v=S_ipdVNSFlo


References
----------
.. [#pydocabc] https://docs.python.org/3/library/collections.abc.html


Assignments
-----------
.. literalinclude:: assignments/oop_abstract_a.py
    :caption: :download:`Solution <assignments/oop_abstract_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_b.py
    :caption: :download:`Solution <assignments/oop_abstract_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_c.py
    :caption: :download:`Solution <assignments/oop_abstract_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_d.py
    :caption: :download:`Solution <assignments/oop_abstract_d.py>`
    :end-before: # Solution
