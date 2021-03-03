Function Recurrence
===================


.. epigraph::

    Aby zrozumieć rekurencję – musisz najpierw zrozumieć rekurencję.


Rationale
---------
* Also known as recursion
* Python isn't a functional language
* CPython implementation doesn't optimize tail recursion
* Tail recursion is not a particularly efficient technique in Python
* Uncontrolled recursion causes stack overflows!
* Rewriting the algorithm iteratively, is generally a better idea


Example
-------
Recap information about factorial (``n!``):

.. code-block:: text

    5! = 5 * 4!
    4! = 4 * 3!
    3! = 3 * 2!
    2! = 2 * 1!
    1! = 1 * 0!
    0! = 1

>>> def factorial(n):
...     if n == 0:
...         return 1
...     else:
...         return n * factorial(n-1)

.. code-block:: python

    factorial(5)                                    # = 120
        return 5 * factorial(4)                     # 5 * 24 = 120
            return 4 * factorial(3)                 # 4 * 6 = 24
                return 3 * factorial(2)             # 3 * 2 = 6
                    return 2 * factorial(1)         # 2 * 1 = 2
                        return 1 * factorial(0)     # 1 * 1 = 1
                            return 1                # 1


Use Case
--------
.. figure:: img/function-recurrence-hanoi.jpg

    Hanoi Tower as a standard example of a recurrence. Source: [#hanoi]_


Recursion Depth Limit
---------------------
* Default recursion depth limit is 1000
* Warning: Anaconda sets default recursion depth limit to 2000

>>> import sys
>>>
>>> sys.setrecursionlimit(3000)


Assignments
-----------
.. literalinclude:: assignments/function_recurrence_a.py
    :caption: :download:`Solution <assignments/function_recurrence_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_recurrence_b.py
    :caption: :download:`Solution <assignments/function_recurrence_b.py>`
    :end-before: # Solution


References
----------
.. [#hanoi] https://dyermath.files.wordpress.com/2015/06/hanoi-13.jpg
