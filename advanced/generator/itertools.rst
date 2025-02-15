Generator Itertools
===================


Itertools
---------
* Learn more at https://docs.python.org/library/itertools.html
* More information in `Itertools`
* ``from itertools import *``
* ``count(start=0, step=1)``
* ``cycle(iterable)``
* ``repeat(object[, times])``
* ``accumulate(iterable[, func, *, initial=None])``
* ``chain(*iterables)``
* ``compress(data, selectors)``
* ``islice(iterable, start, stop[, step])``
* ``starmap(function, iterable)``
* ``product(*iterables, repeat=1)``
* ``permutations(iterable, r=None)``
* ``combinations(iterable, r)``
* ``combinations_with_replacement(iterable, r)``
* ``groupby(iterable, key=None)``


Itertools Count
---------------
* ``itertools.count(start=0, step=1)``

>>> from itertools import count
>>>
>>>
>>> data = count(3, 2)
>>>
>>> next(data)
3
>>> next(data)
5
>>> next(data)
7


Itertools Cycle
---------------
* ``itertools.cycle(iterable)``

>>> from itertools import cycle
>>>
>>>
>>> data = cycle(['white', 'gray'])
>>>
>>> next(data)
'white'
>>> next(data)
'gray'
>>> next(data)
'white'
>>> next(data)
'gray'

>>> from itertools import cycle
>>>
>>>
>>> for i, status in enumerate(cycle(['even', 'odd'])):  # doctest + SKIP
...     print(i, status)
...     if i == 3:
...         break
0 even
1 odd
2 even
3 odd

Itertools Repeat
----------------
* ``itertools.repeat(object[, times])``

>>> from itertools import repeat
>>>
>>>
>>> data = repeat('Beetlejuice', 3)
>>>
>>> next(data)
'Beetlejuice'
>>> next(data)
'Beetlejuice'
>>> next(data)
'Beetlejuice'
>>> next(data)
Traceback (most recent call last):
StopIteration


Itertools Accumulate
--------------------
* ``itertools.accumulate(iterable[, func, *, initial=None])``

>>> from itertools import accumulate
>>>
>>>
>>> data = accumulate([1, 2, 3, 4])
>>>
>>> next(data)
1
>>> next(data)
3
>>> next(data)
6
>>> next(data)
10
>>> next(data)
Traceback (most recent call last):
StopIteration


Itertools Chain
---------------
``itertools.chain(*iterables)``:

>>> from itertools import chain
>>>
>>>
>>> keys = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>>
>>> for x in chain(keys, values):
...     print(x)
a
b
c
1
2
3

>>> from itertools import chain
>>>
>>>
>>> class Iterator:
...     def __iter__(self):
...         self._current = 0
...         return self
...
...     def __next__(self):
...         if self._current >= len(self.values):
...             raise StopIteration
...         element = self.values[self._current]
...         self._current += 1
...         return element
>>>
>>>
>>> class Character(Iterator):
...     def __init__(self, *values):
...         self.values = values
>>>
>>>
>>> class Number(Iterator):
...     def __init__(self, *values):
...         self.values = values
>>>
>>>
>>> chars = Character('a', 'b', 'c')
>>> nums = Number(1, 2, 3)
>>> data = chain(chars, nums)
>>> next(data)
'a'
>>> next(data)
'b'
>>> next(data)
'c'
>>> next(data)
1
>>> next(data)
2
>>> next(data)
3


Itertools Compress
------------------
``itertools.compress(data, selectors)``:

>>> from itertools import compress
>>>
>>>
>>> # data = compress('ABCDEF', [1,0,1,0,1,1])
>>> data = compress('ABCDEF', [True, False, True, False, True, True])
>>>
>>> next(data)
'A'
>>> next(data)
'C'
>>> next(data)
'E'
>>> next(data)
'F'
>>> next(data)
Traceback (most recent call last):
StopIteration


Itertools ISlice
----------------
* ``itertools.islice(iterable, start, stop[, step])``

>>> from itertools import islice
>>>
>>>
>>> data = islice('ABCDEFG', 2, 6, 2 )
>>>
>>> next(data)
'C'
>>> next(data)
'E'
>>> next(data)
Traceback (most recent call last):
StopIteration


Itertools Starmap
-----------------
* ``itertools.starmap(function, iterable)``

>>> from itertools import starmap
>>>
>>>
>>> data = starmap(pow, [(2,5), (3,2), (10,3)])
>>>
>>> next(data)
32
>>> next(data)
9
>>> next(data)
1000
>>> next(data)
Traceback (most recent call last):
StopIteration


Itertools Product
-----------------
* ``itertools.product(*iterables, repeat=1)``

>>> from itertools import product
>>>
>>>
>>> data = product(['a', 'b', 'c'], [1,2])
>>>
>>> next(data)
('a', 1)
>>> next(data)
('a', 2)
>>> next(data)
('b', 1)
>>> next(data)
('b', 2)
>>> next(data)
('c', 1)
>>> next(data)
('c', 2)
>>> next(data)
Traceback (most recent call last):
StopIteration


Itertools Permutations
----------------------
* ``itertools.permutations(iterable, r=None)``

>>> from itertools import permutations
>>>
>>>
>>> data = permutations([1,2,3])
>>>
>>> next(data)
(1, 2, 3)
>>> next(data)
(1, 3, 2)
>>> next(data)
(2, 1, 3)
>>> next(data)
(2, 3, 1)
>>> next(data)
(3, 1, 2)
>>> next(data)
(3, 2, 1)
>>> next(data)
Traceback (most recent call last):
StopIteration


Itertools Combinations
----------------------
* ``itertools.combinations(iterable, r)``

>>> from itertools import combinations
>>>
>>>
>>> data = combinations([1, 2, 3, 4], 2)
>>>
>>> next(data)
(1, 2)
>>> next(data)
(1, 3)
>>> next(data)
(1, 4)
>>> next(data)
(2, 3)
>>> next(data)
(2, 4)
>>> next(data)
(3, 4)
>>> next(data)
Traceback (most recent call last):
StopIteration


Itertools Combinations With Replacement
---------------------------------------
* ``itertools.combinations_with_replacement(iterable, r)``

>>> from itertools import combinations_with_replacement
>>>
>>>
>>> data = combinations_with_replacement([1,2,3], 2)
>>>
>>> next(data)
(1, 1)
>>> next(data)
(1, 2)
>>> next(data)
(1, 3)
>>> next(data)
(2, 2)
>>> next(data)
(2, 3)
>>> next(data)
(3, 3)
>>> next(data)
Traceback (most recent call last):
StopIteration


Itertools GroupBy
-----------------
* ``itertools.groupby(iterable, key=None)``
* Make an iterator that returns consecutive keys and groups from the
  iterable. Generally, the iterable needs to already be sorted on the same
  key function. The operation of groupby() is similar to the uniq filter
  in Unix. It generates a break or new group every time the value of the
  key function changes. That behavior differs from SQL's GROUP BY which
  aggregates common elements regardless of their input order:

>>> from itertools import groupby
>>>
>>>
>>> data = groupby('AAAABBBCCDAABBB')
>>>
>>> next(data)  # doctest: +ELLIPSIS
('A', <itertools._grouper object at 0x...>)
>>> next(data)  # doctest: +ELLIPSIS
('B', <itertools._grouper object at 0x...>)
>>> next(data)  # doctest: +ELLIPSIS
('C', <itertools._grouper object at 0x...>)
>>> next(data)  # doctest: +ELLIPSIS
('D', <itertools._grouper object at 0x...>)
>>> next(data)  # doctest: +ELLIPSIS
('A', <itertools._grouper object at 0x...>)
>>> next(data)  # doctest: +ELLIPSIS
('B', <itertools._grouper object at 0x...>)
>>> next(data)
Traceback (most recent call last):
StopIteration
>>> [k for k, g in groupby('AAAABBBCCDAABBB')]
['A', 'B', 'C', 'D', 'A', 'B']
>>> [list(g) for k, g in groupby('AAAABBBCCD')]
[['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
