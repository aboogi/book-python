Logic Bool
==========


Definition
----------
* ``True`` - Positive value
* ``False`` - Negative value
* First letter capitalized, other are lower cased

>>> data = True
>>> data = False


Type Casting
------------
* Builtin function ``bool()`` converts argument to ``bool``

>>> bool(True)
True
>>> bool(False)
False
>>> bool(1)
True
>>> bool(0)
False

>>> bool(1)
True
>>> bool(2)
True
>>> bool(3)
True
>>> bool(-1)
True
>>> bool(-2)
True
>>> bool(-3)
True
>>> bool(1.0)
True
>>> bool('Jan Twardowski')
True

Negative values

>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(0+0j)
False
>>> bool(0.0+0.0j)
False
>>> bool(False)
False
>>> bool(None)
False
>>> bool('')
False
>>> bool(())
False
>>> bool([])
False
>>> bool({})
False

>>> bool(int())
False
>>> bool(float())
False
>>> bool(complex())
False
>>> bool(bool())
False
>>> bool(str())
False
>>> bool(tuple())
False
>>> bool(list())
False
>>> bool(dict())
False
>>> bool(set())
False
>>> bool(frozenset())
False


Comparison
----------
* ``x < y`` - Less than
* ``x <= y`` - Less or equal
* ``x > y`` - Greater than
* ``x >= y`` - Greater or equal
* ``==`` - Equals
* ``!=`` - Not Equals

>>> 10 < 2
False
>>> 10 <= 2
False
>>> 10 > 2
True
>>> 10 >= 2
True
>>> 10 == 2
False
>>> 10 != 2
True

>>> x = 1
>>> y = 2
>>>
>>> x == 1
True
>>> y == 2
True
>>> x == y
False
>>> x != y
True


Conjunction
-----------
Definition:

.. code-block:: text

    1 & 1 -> 1
    1 & 0 -> 0
    0 & 1 -> 0
    0 & 0 -> 0

Example:

>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False

Use Cases:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> firstname == 'Mark' and lastname == 'Watney'
True

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> firstname == 'Mark' and lastname == 'Twardowski'
False

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> firstname == 'Mark'
True
>>> lastname == 'Watney'
True
>>> lastname == 'Twardowski'
False
>>> True and True
True
>>> True and False
False


Disjunction
-----------
Definition:

.. code-block:: text

    1 | 1 -> 1
    1 | 0 -> 1
    0 | 1 -> 1
    0 | 0 -> 0

Example:

>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False

Use Case:

>>> name = 'Mark Watney'
>>>
>>> name == 'Mark Watney' or name == 'Melissa Lewis'
True

>>> name = 'Mark Watney'
>>>
>>> name == 'Mark Watney'
True
>>> name == 'Melissa Lewis'
False
>>> True or False
False


Boolean Algebra
---------------
Example:

>>> True and True or False
True
>>> False and False or True
True

>>> (True and True) or False
True
>>> True and (True or False)
True

>>> True and False or False
False
>>> True and (False or False)
False

Use Case:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> (firstname == 'Mark' and lastname == 'Watney') \
...     or (firstname == 'Jan' and lastname == 'Twardowski') \
...     or (firstname == 'Melissa' and lastname == 'Lewis')
True

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> firstname == 'Mark' and lastname == 'Watney'
True
>>> firstname == 'Jan' and lastname == 'Twardowski'
False
>>> firstname == 'Melissa' and lastname == 'Lewis'
False
>>> True or False or False
True


Built-in Functions
------------------
* ``type()`` - Checks type of an object
* ``isinstance(a, x)`` - If ``a`` is instance of ``x``
* ``isinstance(a, (x,y))`` - If ``a`` is instance of ``x`` or ``y``

>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>

>>> isinstance(1, bool)
False
>>> isinstance(1, int)
True
>>> isinstance(1, float)
False

>>> isinstance(1.23, bool)
False
>>> isinstance(1.23, int)
False
>>> isinstance(1.23, float)
True

>>> isinstance(True, bool)
True
>>> isinstance(True, int)
True
>>> isinstance(True, float)
False
>>> isinstance(False, bool)
True
>>> isinstance(False, int)
True
>>> isinstance(False, float)
False


Example
-------
* ``&`` - and
* ``|`` - or

>>> import numpy as np
>>>
>>>
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
...
>>> a > 2
array([[False, False,  True],
       [ True,  True,  True],
       [ True,  True,  True]])
>>>
>>> a < 7
array([[ True,  True,  True],
       [ True,  True,  True],
       [False, False, False]])
>>>
>>> a == 9
array([[False, False, False],
       [False, False, False],
       [False, False,  True]])
>>>
>>> (a>2) & (a<7) | (a==9)
array([[False, False,  True],
       [ True,  True,  True],
       [False, False,  True]])
>>>
>>> a[(a>2) & (a<7) | (a==9)]
array([3, 4, 5, 6, 9])


Assignments
-----------
.. literalinclude:: assignments/type_bool_a.py
    :caption: :download:`Solution <assignments/type_bool_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_bool_b.py
    :caption: :download:`Solution <assignments/type_bool_b.py>`
    :end-before: # Solution
