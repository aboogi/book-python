Loop Comprehension
==================

Recap
-----
>>> result = []
>>>
>>> for x in range(0,5):
...     result.append(x)
>>>
>>> print(result)
[0, 1, 2, 3, 4]


Syntax
------
.. code-block:: python

    result = [<RETURN> for <VARIABLE> in <ITERABLE>]


Example
-------
>>> result = [x for x in range(0,5)]
>>>
>>> print(result)
[0, 1, 2, 3, 4]


Convention
----------
* Use shorter variable names
* ``x`` is common name


Comprehensions and Generator Expression
---------------------------------------
* Comprehensions executes instantly
* Generator expression executes lazily

List Comprehension:

>>> list(x for x in range(0,5))
[0, 1, 2, 3, 4]
>>>
>>> [x for x in range(0,5)]
[0, 1, 2, 3, 4]

Set Comprehension:

>>> set(x for x in range(0,5))
{0, 1, 2, 3, 4}
>>>
>>> {x for x in range(0,5)}
{0, 1, 2, 3, 4}

Dict Comprehension:

>>> dict((x,x) for x in range(0,5))
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
>>>
>>> {x:x for x in range(0,5)}
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

Tuple Comprehension:

>>> tuple(x for x in range(0,5))
(0, 1, 2, 3, 4)

Generator Expression:

>>> (x for x in range(0,5))  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>


>>> _ = list(x for x in range(0,5))      # list comprehension
>>> _ = tuple(x for x in range(0,5))     # tuple comprehension
>>> _ = set(x for x in range(0,5))       # set comprehension
>>> _ = dict((x,x) for x in range(0,5))  # dict comprehension
>>>
>>> _ = [x for x in range(0,5)]          # list comprehension
>>> _ = (x for x in range(0,5))          # generator expression
>>> _ = {x for x in range(0,5)}          # set comprehension
>>> _ = {x:x for x in range(0,5)}        # dict comprehension



Comprehensions or Generator Expression
--------------------------------------
Comprehensions vs Generator Expression:

>>> data = [x for x in range(0,10)]
>>> print(data)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> data = (x for x in range(0,10))
>>> print(data)  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>

Comprehension:

>>> data = [x for x in range(0,10)]
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 3:
...         break
0 1 2 3
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 6:
...         break
0 1 2 3 4 5 6
>>>
>>> print(list(data))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> print(list(data))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Generator Expressions:

>>> data = (x for x in range(0,10))
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 3:
...         break
0 1 2 3
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 6:
...         break
4 5 6
>>>
>>> print(list(data))
[7, 8, 9]
>>>
>>> print(list(data))
[]


List Comprehension
------------------
>>> [x+1 for x in range(0,5)]
[1, 2, 3, 4, 5]
>>>
>>> [x-1 for x in range(0,5)]
[-1, 0, 1, 2, 3]
>>>
>>> [x**2 for x in range(0,5)]
[0, 1, 4, 9, 16]
>>>
>>> [2**x for x in range(0,5)]
[1, 2, 4, 8, 16]

>>> list(x+1 for x in range(0,5))
[1, 2, 3, 4, 5]
>>>
>>> list(x-1 for x in range(0,5))
[-1, 0, 1, 2, 3]
>>>
>>> list(x**2 for x in range(0,5))
[0, 1, 4, 9, 16]
>>>
>>> list(2**x for x in range(0,5))
[1, 2, 4, 8, 16]


Set Comprehension
-----------------
``set`` comprehension approach to applying function to elements:

>>> {x+10 for x in range(0, 5)}
{10, 11, 12, 13, 14}

>>> set(x+10 for x in range(0, 5))
{10, 11, 12, 13, 14}


Dict Comprehension
------------------
``dict`` comprehension approach to applying function to elements:

>>> {x+10:x for x in range(0,5)}
{10: 0, 11: 1, 12: 2, 13: 3, 14: 4}

>>> dict((x+10,x) for x in range(0,5))
{10: 0, 11: 1, 12: 2, 13: 3, 14: 4}

``dict`` comprehension approach to applying function to elements:

>>> {x:x+10 for x in range(0,5)}
{0: 10, 1: 11, 2: 12, 3: 13, 4: 14}

>>> dict((x,x+10) for x in range(0,5))
{0: 10, 1: 11, 2: 12, 3: 13, 4: 14}

``dict`` Comprehension approach to applying function to elements:

>>> {x+10:x+10 for x in range(0,5)}
{10: 10, 11: 11, 12: 12, 13: 13, 14: 14}

>>> dict((x+10,x+10) for x in range(0,5))
{10: 10, 11: 11, 12: 12, 13: 13, 14: 14}


Tuple Comprehension?!
---------------------
* Tuple Comprehension vs. Generator Expression
* More information in `Generators`

Tuple Comprehension:

>>> tuple(x+10 for x in range(0,5))
(10, 11, 12, 13, 14)

Generator Expression:

>>> (x+10 for x in range(0,5))  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>


Filter
------
Example 1:

>>> result = []
...
>>> for x in range(0,5):
...     if x % 2 == 0:
...         result.append(x)
>>>
>>> print(result)
[0, 2, 4]

>>> result = [x for x in range(0,5) if x%2==0]
>>> print(result)
[0, 2, 4]

Example 2:

>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa'),
...         (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>> [features for *features,label in DATA if label == 'setosa']  # doctest: +NORMALIZE_WHITESPACE
[[5.1, 3.5, 1.4, 0.2],
 [4.7, 3.2, 1.3, 0.2]]
>>>
>>> [X for *X,y in DATA if y=='setosa']  # doctest: +NORMALIZE_WHITESPACE
[[5.1, 3.5, 1.4, 0.2],
 [4.7, 3.2, 1.3, 0.2]]


Map
---
Applying function to each output element:

>>> [float(x) for x in range(0,5)]
[0.0, 1.0, 2.0, 3.0, 4.0]

>>> [float(x) for x in range(0,5) if x%2==0]
[0.0, 2.0, 4.0]

Applying function to each output element:

>>> [pow(2,x) for x in range(0,5)]
[1, 2, 4, 8, 16]

>>> [pow(2,x) for x in range(0,5) if x%2==0]
[1, 4, 16]

Using ``list`` comprehension for filtering:

>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa'),
...         (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>> [tuple(features) for *features,label in DATA if label == 'setosa']  # doctest: +NORMALIZE_WHITESPACE
[(5.1, 3.5, 1.4, 0.2),
 (4.7, 3.2, 1.3, 0.2)]
>>>
>>> [tuple(X) for *X,y in DATA if y=='setosa']  # doctest: +NORMALIZE_WHITESPACE
[(5.1, 3.5, 1.4, 0.2),
 (4.7, 3.2, 1.3, 0.2)]


Indent and Whitespaces
----------------------
>>> result = [pow(x,2) for x in range(0,5)]
>>>
>>> result = [pow(x,2)
...           for x in range(0,5)]

>>> result = [pow(x, 2) for x in range(0, 5) if x % 2 == 0]
>>>
>>> result = [pow(x,2) for x in range(0,5) if x%2==0]

>>> result = [pow(x,2)
...           for x in range(0,5)
...               if x % 2 == 0]
>>>
>>> result = [pow(x,2)
...           for x in range(0,5)
...           if x % 2 == 0]

>>> DATA = [{'a':1, 'b':2, 'c': 3},
...         {'a':1, 'b':2, 'c': 3},
...         {'a':1, 'b':2, 'c': 3}]
>>>
>>> result = [value
...           for row in DATA
...             for key, value in row.items()]
>>>
>>> result = [value
...           for row in DATA
...           for key, value in row.items()]
>>>

>>> # doctest: +SKIP
... result = [astronaut | dict(addresses)
...           for astronaut in json.loads(DATA)
...             for i, address in enumerate(astronaut.pop('addresses'), start=1)
...                 if (columns := [f'{key}{i}' for key in address.keys()])
...                     and (addresses := zip(columns, address.values()))]
>>>
>>> # doctest: +SKIP
... result = [astronaut | dict(addresses)
...           for astronaut in json.loads(DATA)
...           for i, address in enumerate(astronaut.pop('addresses'), start=1)
...           if (columns := [f'{key}{i}' for key in address.keys()])
...           and (addresses := zip(columns, address.values()))]


Nested
------
>>> DATA = {
...     6: ['Doctorate', 'Prof-school'],
...     5: ['Masters', 'Bachelor', 'Engineer'],
...     4: ['HS-grad'],
...     3: ['Junior High'],
...     2: ['Primary School'],
...     1: ['Kindergarten']}
>>>
>>> result = {}
>>> for i, titles in DATA.items():
...     for title in titles:
...         result[title] = str(i)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'Doctorate': '6',
 'Prof-school': '6',
 'Masters': '5',
 'Bachelor': '5',
 'Engineer': '5',
 'HS-grad': '4',
 'Junior High': '3',
 'Primary School': '2',
 'Kindergarten': '1'}
>>>
>>> print(i)
1
>>>
>>> print(title)
Kindergarten
>>>
>>> print(titles)
['Kindergarten']

>>> DATA = {
...     6: ['Doctorate', 'Prof-school'],
...     5: ['Masters', 'Bachelor', 'Engineer'],
...     4: ['HS-grad'],
...     3: ['Junior High'],
...     2: ['Primary School'],
...     1: ['Kindergarten']}
>>>
>>> result = {title: str(i)
...           for i, titles in DATA.items()
...           for title in titles}
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'Doctorate': '6',
 'Prof-school': '6',
 'Masters': '5',
 'Bachelor': '5',
 'Engineer': '5',
 'HS-grad': '4',
 'Junior High': '3',
 'Primary School': '2',
 'Kindergarten': '1'}
>>>
>>> # doctest: +SKIP
... print(i)
Traceback (most recent call last):
NameError: name 'i' is not defined
>>>
>>> # doctest: +SKIP
... print(title)
Traceback (most recent call last):
NameError: name 'title' is not defined
>>>
>>> # doctest: +SKIP
... print(titles)
Traceback (most recent call last):
NameError: name 'titles' is not defined


Examples
--------
Increment and decrement:

>>> [x+1 for x in range(0,5)]
[1, 2, 3, 4, 5]

>>> [x-1 for x in range(0,5)]
[-1, 0, 1, 2, 3]

Sum:

>>> sum(x for x in range(0,5))
10

>>> sum(x for x in range(0,5) if x%2==0)
6

Power:

>>> [pow(x,2) for x in range(0,5)]
[0, 1, 4, 9, 16]

>>> [x**2 for x in range(0,5)]
[0, 1, 4, 9, 16]

>>> [pow(2,x) for x in range(0,5)]
[1, 2, 4, 8, 16]

>>> [2**x for x in range(0,5)]
[1, 2, 4, 8, 16]

Even or Odd:

>>> [x for x in range(0,5)]
[0, 1, 2, 3, 4]

>>> [x%2==0 for x in range(0,5)]
[True, False, True, False, True]

Even or Odd:

>>> result = {}
>>>
>>> for x in range(0,5):
...     is_even = (x % 2 == 0)
...     result.update({x: is_even})
>>>
>>> print(result)
{0: True, 1: False, 2: True, 3: False, 4: True}

>>> {x: (x%2==0) for x in range(0,5)}
{0: True, 1: False, 2: True, 3: False, 4: True}

Filtering:

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [person
...               for person in DATA
...               if person['is_astronaut']]
>>>
>>> print(astronauts)  # doctest: +NORMALIZE_WHITESPACE
[{'is_astronaut': True, 'name': 'Jan Twardowski'},
 {'is_astronaut': True, 'name': 'Mark Watney'},
 {'is_astronaut': True, 'name': 'Melissa Lewis'}]

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [person['name']
...               for person in DATA
...               if person['is_astronaut']]
>>>
>>> print(astronauts)
['Jan Twardowski', 'Mark Watney', 'Melissa Lewis']

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [{'firstname': person['name'].split()[0],
...                'lastname': person['name'].split()[1]}
...                for person in DATA
...                if person['is_astronaut']]
>>>
>>> print(astronauts)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'Twardowski'},
 {'firstname': 'Mark', 'lastname': 'Watney'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'}]

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [{'firstname': person['name'].split()[0].capitalize(),
...                'lastname': person['name'].split()[1][0]+'.'}
...                for person in DATA
...                if person['is_astronaut']]
>>>
>>> print(astronauts)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'T.'},
 {'firstname': 'Mark', 'lastname': 'W.'},
 {'firstname': 'Melissa', 'lastname': 'L.'}]


>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [{'firstname': fname, 'lastname': lname}
...                for person in DATA
...                if person['is_astronaut']
...                and (name := person['name'].split())
...                and (fname := name[0].capitalize())
...                and (lname := f'{name[1][0]}.')]
>>>
>>> print(astronauts)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'T.'},
 {'firstname': 'Mark', 'lastname': 'W.'},
 {'firstname': 'Melissa', 'lastname': 'L.'}]

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [f'{fname} {lname[0]}.'
...               for person in DATA
...               if person['is_astronaut']
...               and (fullname := person['name'].split())
...               and (fname := fullname[0].capitalize())
...               and (lname := fullname[1].upper())]
>>>
>>> print(astronauts)
['Jan T.', 'Mark W.', 'Melissa L.']

More information in `Assignment Expression`

Using ``list`` comprehension for filtering with more complex expression:

>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa'),
...         (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>>
>>> def is_setosa(species):
...     if species == 'setosa':
...         return True
...     else:
...         return False
>>>
>>>
>>> [tuple(X) for *X,y in DATA if is_setosa(y)]  # doctest: +NORMALIZE_WHITESPACE
[(5.1, 3.5, 1.4, 0.2),
 (4.7, 3.2, 1.3, 0.2)]

Quick parsing lines:

>>> DATA = ['5.8,2.7,5.1,1.9,virginica',
...         '5.1,3.5,1.4,0.2,setosa',
...         '5.7,2.8,4.1,1.3,versicolor']
>>>
>>> result = []
>>>
>>> for row in DATA:
...     row = row.split(',')
...     result.append(row)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[['5.8', '2.7', '5.1', '1.9', 'virginica'],
 ['5.1', '3.5', '1.4', '0.2', 'setosa'],
 ['5.7', '2.8', '4.1', '1.3', 'versicolor']]
>>>
>>> [row.split(',') for row in DATA]  # doctest: +NORMALIZE_WHITESPACE
[['5.8', '2.7', '5.1', '1.9', 'virginica'],
 ['5.1', '3.5', '1.4', '0.2', 'setosa'],
 ['5.7', '2.8', '4.1', '1.3', 'versicolor']]

Reversing ``dict`` keys with values:

>>> DATA = {'a': 1, 'b': 2}
>>>
>>> list(DATA.items())  # doctest: +NORMALIZE_WHITESPACE
[('a', 1),
 ('b', 2)]
>>> [(k,v) for k,v in DATA.items()]  # doctest: +NORMALIZE_WHITESPACE
[('a', 1),
 ('b', 2)]
>>> [(v,k) for k,v in DATA.items()]  # doctest: +NORMALIZE_WHITESPACE
[(1, 'a'),
 (2, 'b')]
>>>
>>> {v:k for k,v in DATA.items()}
{1: 'a', 2: 'b'}

Value collision while reversing ``dict``:

>>> DATA = {'a': 1, 'b': 2, 'c': 2}
>>>
>>> {v:k for k,v in DATA.items()}
{1: 'a', 2: 'c'}


All and Any
-----------
>>> all(x for x in range(0,5))
False
>>> any(x for x in range(0,5))
True

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> if all(person['is_astronaut'] for person in DATA):
...     print('Everyone is astronaut')
... else:
...     print('Not everyone is astronaut')
Not everyone is astronaut

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> if any(person['is_astronaut'] for person in DATA):
...     print('At least one person is astronaut')
... else:
...     print('There are no astronauts')
At least one person is astronaut

>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa'),
...         (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>> all(observation > 1.0
...     for *features, label in DATA[1:]
...     for observation in features
...     if isinstance(observation, float))
False
>>>
>>> all(x > 1.0
...     for *X,y in DATA[1:]
...     for x in X
...     if isinstance(x, float))
False


Conditional Expression
----------------------
>>> result = ['even' if x % 2 == 0 else 'odd'
...           for x in range(0,10)]
>>> result
['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

>>> result = ['even' if x % 2 == 0 else 'odd'
...           for x in range(0,10)
...           if x % 3 == 0]
>>> result
['even', 'odd', 'even', 'odd']


Assignments
-----------
.. literalinclude:: assignments/loop_comprehension_a.py
    :caption: :download:`Solution <assignments/loop_comprehension_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_b.py
    :caption: :download:`Solution <assignments/loop_comprehension_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_c.py
    :caption: :download:`Solution <assignments/loop_comprehension_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_d.py
    :caption: :download:`Solution <assignments/loop_comprehension_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_comprehension_e.py
    :caption: :download:`Solution <assignments/loop_comprehension_e.py>`
    :end-before: # Solution
