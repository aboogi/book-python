Generator Inspect
=================


Is Generator
------------
>>> from inspect import isgenerator
>>>
>>>
>>> a = [x for x in range(0,5)]
>>> b = (x for x in range(0,5))
>>>
>>> isgenerator(a)
False
>>> isgenerator(b)
True

>>> from inspect import isgenerator
>>>
>>>
>>> data = range(0, 10)
>>>
>>> isgenerator(data)
False


Introspection
-------------
>>> data = (x for x in range(0,10))
>>>
>>>
>>> next(data)
0
>>>
>>> data.gi_code  # doctest: +ELLIPSIS
<code object <genexpr> at 0x..., file "<...>", line 1>
>>>
>>> data.gi_running
False
>>>
>>> data.gi_frame  # doctest: +ELLIPSIS
<frame at 0x..., file '<...>', line 1, code <genexpr>>
>>>
>>> data.gi_frame.f_locals  # doctest: +ELLIPSIS
{'.0': <range_iterator object at 0x...>, 'x': 0}
>>>
>>> data.gi_frame.f_code  # doctest: +ELLIPSIS
<code object <genexpr> at 0x...0, file "<...>", line 1>
>>>
>>> data.gi_frame.f_lineno
1
>>>
>>> data.gi_frame.f_lasti
10
>>>
>>> data.gi_yieldfrom


Memory Footprint
----------------
* ``sys.getsizeof(obj)`` returns the size of an ``obj`` in bytes
* ``sys.getsizeof(obj)`` calls ``obj.__sizeof__()`` method
* ``sys.getsizeof(obj)`` adds an additional garbage collector overhead if the ``obj`` is managed by the garbage collector

* 104 bytes for generator in Python 3.10
* 112 bytes for generator in Python 3.9
* 112 bytes for generator in Python 3.8
* 120 bytes for generator in Python 3.7

>>> from sys import getsizeof
>>>
>>>
>>> gen1 = (x for x in range(0,1))
>>> gen10 = (x for x in range(0,10))
>>> gen100 = (x for x in range(0,100))
>>> gen1000 = (x for x in range(0,1000))
>>>
>>> getsizeof(gen1)
104
>>>
>>> getsizeof(gen10)
104
>>>
>>> getsizeof(gen100)
104
>>>
>>> getsizeof(gen1000)
104

>>> from sys import getsizeof
>>>
>>>
>>> com1 = [x for x in range(0,1)]
>>> com10 = [x for x in range(0,10)]
>>> com100 = [x for x in range(0,100)]
>>> com1000 = [x for x in range(0,1000)]
>>>
>>>
>>> getsizeof(com1)
88
>>>
>>> getsizeof(com10)
184
>>>
>>> getsizeof(com100)
920
>>>
>>> getsizeof(com1000)
8856

.. figure:: img/generator-function-performance.png

    Source: https://www.askpython.com/python/python-yield-examples


Assignments
-----------
.. literalinclude:: assignments/generator_inspect_a.py
    :caption: :download:`Solution <assignments/generator_inspect_a.py>`
    :end-before: # Solution
