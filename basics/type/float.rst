Type Float
==========


Definition
----------
>>> data = 1.337
>>> data = +1.337
>>> data = -1.337


Notation
--------
* Without leading or trailing zero
* Used by ``numpy``

>>> data = 69.
>>> print(data)
69.0
>>> data = .44
>>> print(data)
0.44

Scientific and engineering notation

>>> million = 1e6
>>> print(million)
1000000.0
>>> million = 1E6
>>> print(million)
1000000.0

>>> 1e6
1000000.0
>>> +1e6
1000000.0
>>> -1e6
-1000000.0
>>> 1e-3
0.001
>>> 1e-4
0.0001
>>> 1e-5
1e-05
>>> 1e-6
1e-06

>>> -1e-3
-0.001
>>> -1e-4
-0.0001

>>> 1.337 * 1e3
1337.0
>>> 1.337 * 1e-3
0.001337


Type Casting
------------
Builtin function ``float()`` converts argument to ``float``

>>> float(1)
1.0
>>> float(+1)
1.0
>>> float(-1)
-1.0

>>> float(1.337)
1.337
>>> float(+1.337)
1.337
>>> float(-1.337)
-1.337

>>> float('1.337')
1.337
>>> float('+1.337')
1.337
>>> float('-1.337')
-1.337

>>> float('1,337')
Traceback (most recent call last):
ValueError: could not convert string to float: '1,337'

>>> float('+1,337')
Traceback (most recent call last):
ValueError: could not convert string to float: '+1,337'

>>> float('-1,337')
Traceback (most recent call last):
ValueError: could not convert string to float: '-1,337'


Round Number
------------
Rounding a number

>>> pi = 3.14159265359
>>>
>>> round(pi, 4)
3.1416
>>> round(pi, 2)
3.14
>>> round(pi)
3

Rounding a number in string formatting

>>> pi = 3.14159265359
>>>
>>> print(f'Pi number is {pi}')
Pi number is 3.14159265359
>>> print(f'Pi number is {pi:f}')
Pi number is 3.141593
>>> print(f'Pi number is {pi:.4f}')
Pi number is 3.1416
>>> print(f'Pi number is {pi:.2f}')
Pi number is 3.14
>>> print(f'Pi number is {pi:.0f}')
Pi number is 3

>>> round(10.5)
10
>>> round(10.51)
11


Built-in Functions
------------------
Builtin function ``pow()`` raises number to the ``n-th`` power.
Note, that arithmetic operator ``**`` also raises number to the power:

>>> pow(10, 2)
100
>>> pow(2, -1)
0.5

>>> pow(1.337, 3)
2.389979753
>>> pow(4, 0.5)
2.0
>>> pow(2, 0.5)
1.4142135623730951

Builtin function ``pow()`` can be used to calculate roots of a number:

>>> pow(4, 1/2)
2.0
>>> pow(2, 1/2)
1.4142135623730951
>>> pow(27, 1/3)
3.0

>>> pow(4, -1/2)
0.5
>>> pow(2, -1/2)
0.7071067811865476
>>> pow(27, -1/3)
0.33333333333333337

>>> pow(-2, -1)
-0.5
>>> pow(-4, -1)
-0.25

Builtin function ``pow()`` can return ``complex`` numbers.
Note that Python has special ``complex()`` numeric type.

>>> pow(-2, -1/2)
(4.329780281177467e-17-0.7071067811865476j)
>>> pow(-2, 1/2)
(8.659560562354934e-17+1.4142135623730951j)
>>> pow(-4, -1/2)
(3.061616997868383e-17-0.5j)
>>> pow(-4, 1/2)
(1.2246467991473532e-16+2j)

Absolute value

>>> abs(1)
1
>>> abs(1.337)
1.337

>>> abs(-1)
1
>>> abs(-1.337)
1.337


Assignments
-----------
.. literalinclude:: assignments/type_float_a.py
    :caption: :download:`Solution <assignments/type_float_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_b.py
    :caption: :download:`Solution <assignments/type_float_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_c.py
    :caption: :download:`Solution <assignments/type_float_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_d.py
    :caption: :download:`Solution <assignments/type_float_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_e.py
    :caption: :download:`Solution <assignments/type_float_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_f.py
    :caption: :download:`Solution <assignments/type_float_f.py>`
    :end-before: # Solution

.. figure:: img/spacesuits.png

    EMU and Orlan

.. literalinclude:: assignments/type_float_g.py
    :caption: :download:`Solution <assignments/type_float_g.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_float_h.py
    :caption: :download:`Solution <assignments/type_float_h.py>`
    :end-before: # Solution
