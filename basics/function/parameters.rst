Function Parameters
===================


Rationale
---------
* Parameter - Receiving variable used within the function
* Required parameter:

    * Necessary to call that function
    * Specified at leftmost side

* Default parameter:

    * Optional to call that function
    * Has default value
    * Default value will be overridden if specified at a call time
    * Specified at rightmost side

.. glossary::

    parameter
        Receiving variable used within the function/block

    required parameter
        Parameter which is necessary to call function

    default parameter
        Parameter which is optional and has default value (if not specified at call time)

Syntax
------
Function definition with parameters:

.. code-block:: python

    def myfunction(<parameters>):
        <do something>

>>> def add(a, b):
...     print(a + b)


Required Parameters
-------------------
* Parameters without default values are required

>>> def add(a, b):
...     print(a + b)
>>>
>>>
>>> add()
Traceback (most recent call last):
TypeError: add() missing 2 required positional arguments: 'a' and 'b'
>>> add(1)
Traceback (most recent call last):
TypeError: add() missing 1 required positional argument: 'b'
>>> add(1, 2)
3
>>> add(1, 2, 3)
Traceback (most recent call last):
TypeError: add() takes 2 positional arguments but 3 were given


Default Parameters
------------------
* Default parameters has default value
* Function will use default value if not overwritten by user
* Parameters with default values can be omitted while executing

>>> def add(a=10, b=20):
...     print(a + b)
>>>
>>>
>>> add()
30
>>> add(1)
21
>>> add(1, 2)
3
>>> add(1, 2, 3)
Traceback (most recent call last):
TypeError: add() takes from 0 to 2 positional arguments but 3 were given


Required and Default Parameters
-------------------------------
* Required parameters must be at the left side
* Default parameters must be at the right side
* There cannot be required parameter after optional

>>> def add(a, b=20):
...     print(a + b)
>>>
>>>
>>> add()
Traceback (most recent call last):
TypeError: add() missing 1 required positional argument: 'a'
>>> add(1)
21
>>> add(1, 2)
3
>>> add(1, 2, 3)
Traceback (most recent call last):
TypeError: add() takes from 1 to 2 positional arguments but 3 were given

>>> def add(a=1, b):
...     print(a + b)
Traceback (most recent call last):
SyntaxError: non-default argument follows default argument

>>> def add(a, b=1, c):
...     print(a + b + c)
Traceback (most recent call last):
SyntaxError: non-default argument follows default argument


Examples
--------
Example 1:

>>> def add(a, b):
...     print(a + b)
>>>
>>>
>>> add(1, 2)
3
>>> add(1.5, 2.5)
4.0
>>> add('a', 'b')
ab

Example 2:

>>> def echo(text):
...     print(text)
>>>
>>>
>>> echo('hello')
hello

Example 3:

>>> def connect(username, password, host='127.0.0.1', port=22,
...             ssl=True, keep_alive=1, persistent=False):
...
...     print('Connecting...')

Example 4. Definition of pandas.read_csv() function. Source:  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html:

>>> def read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer',
...              names=None, index_col=None, usecols=None, squeeze=False, prefix=None,
...              mangle_dupe_cols=True, dtype=None, engine=None, converters=None,
...              true_values=None, false_values=None, skipinitialspace=False,
...              skiprows=None, nrows=None, na_values=None, keep_default_na=True,
...              na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False,
...              infer_datetime_format=False, keep_date_col=False, date_parser=None,
...              dayfirst=False, iterator=False, chunksize=None, compression='infer',
...              thousands=None, decimal=b'.', lineterminator=None, quotechar='"',
...              quoting=0, escapechar=None, comment=None, encoding=None, dialect=None,
...              tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True,
...              skipfooter=0, doublequote=True, delim_whitespace=False, low_memory=True,
...              memory_map=False, float_precision=None):
...
...     print('Reading CSV...')


Assignments
-----------
.. literalinclude:: assignments/function_parameters_a.py
    :caption: :download:`Solution <assignments/function_parameters_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_parameters_b.py
    :caption: :download:`Solution <assignments/function_parameters_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_parameters_c.py
    :caption: :download:`Solution <assignments/function_parameters_c.py>`
    :end-before: # Solution
