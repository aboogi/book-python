OOP Inheritance Patterns
========================


Rationale
---------
.. glossary::

    single inheritance
        One class inherits from one other class. Has one parent.

    multilevel inheritance
        One class inherits from other class, and yet another class inherits
        from it. This creates hierarchical structure.

    multiple inheritance
    mixin classes
        One class derives from several other classes at once.


No Inheritance
--------------
>>> class Parent:
...     pass
>>>
>>>
>>> class Child:
...     pass


Single Inheritance
------------------
>>> class Parent:
...     pass
>>>
>>>
>>> class Child(Parent):
...     pass


Multilevel Inheritance
----------------------
>>> class Person:
...     pass
>>>
>>>
>>> class Parent(Person):
...     pass
>>>
>>>
>>> class Child(Parent):
...     pass


Multiple Inheritance
--------------------
>>> class Mother:
...     pass
>>>
>>>
>>> class Father:
...     pass
>>>
>>>
>>> class Child(Mother, Father):
...     pass


Assignments
-----------
.. literalinclude:: assignments/oop_inheritance_patterns_a.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_inheritance_patterns_b.py
    :caption: :download:`Solution <assignments/oop_inheritance_patterns_b.py>`
    :end-before: # Solution
