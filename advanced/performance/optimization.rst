Performance Optimization
========================


PyPy
----
* http://pypy.org
* No GIL
* Can speedup couple order of magnitude


Seven strategies
----------------
* https://www.youtube.com/watch?v=zQeYx87mfyw
* https://www.youtube.com/watch?v=EEUXKG97YRw


Line Profiling
--------------
* ``pip install line_profiler``


Numpy vectorization
-------------------
Scipy Ecosystem:

.. figure:: img/scipy-ecosystem.png


Specialized data structures
---------------------------
* ``scipy.spatial`` - for spatial queries like distances, nearest neighbours, etc.
* ``pandas`` - for SQL-like grouping and aggregation
* ``xarray`` - for grouping across multiple dimensions
* ``scipy.sparse`` - sparse metrics for 2-dimensional structured data
* ``sparse`` (package) - for N-dimensional structured data
* ``scipy.sparse.csgraph`` - for graph-like problems (e.g. finding shortest paths)

Cython
------
* https://en.wikipedia.org/wiki/Cython
* https://youtu.be/zQeYx87mfyw?t=747
* types
* Cython files have a ``.pyx`` extension

.. code-block:: text

    def primes(int kmax):   # The argument will be converted to int or raise a TypeError.
        cdef int n, k, i    # These variables are declared with C types.
        cdef int p[1000]    # Another C type
        result = []         # A Python type

        if kmax > 1000:
            kmax = 1000

        k = 0
        n = 2

        while k < kmax:
            i = 0

            while i < k and n % p[i] != 0:
                i = i + 1

            if i == k:
                p[k] = n
                k = k + 1
                result.append(n)

            n = n + 1
        return result

.. code-block:: text

    In [1]: %load_ext Cython

    In [2]: %%cython
       ...: def f(n):
       ...:     a = 0
       ...:     for i in range(n):
       ...:         a += i
       ...:     return a
       ...:
       ...: cpdef g(int n):
       ...:     cdef int a = 0, i
       ...:     for i in range(n):
       ...:         a += i
       ...:     return a
       ...:

    In [3]: %timeit f(1000000)
    42.7 ms ± 783 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

    In [4]: %timeit g(1000000)
    74 µs ± 16.6 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

    # which gives a 585 times improvement over the pure-python version

Cython compiling:

.. figure:: img/performance-cython.png


Numba
-----
Numba gives you the power to speed up your applications with high performance functions written directly in Python. With a few annotations, array-oriented and math-heavy Python code can be just-in-time compiled to native machine instructions, similar in performance to C, C++ and Fortran, without having to switch languages or Python interpreters.

.. code-block:: python

    from numba import jit, int32


    @jit(nogil=True)
    def do_something():
        pass


    @jit(int32(int32, int32))
    def add(x, y):
        return x + y


Dask
----
Dask natively scales Python. Dask provides advanced parallelism for analytics, enabling performance at scale for the tools you love



Find existing implementation
----------------------------
* https://pypi.org


Contains
--------
* Use ``set`` instead of ``list``
* Jeżeli masz listę w której sprawdzasz czy element występuje, to zamień listę na ``set``, dzięki temu będzie lepsza złożoność

.. code-block:: python

    NAMES = ['José', 'Иван', 'Max']

    if 'Max' in NAMES:
        pass

.. code-block:: python

    NAMES = {'José', 'Иван', 'Max'}

    if 'Max' in NAMES:
        pass


String Concatenation
--------------------
How many string are there in a memory?:

.. code-block:: python

    firstname = 'Jan'
    lastname = 'Twardowski'

    firstname + ' ' + lastname
    # Jan Twardowski

How many string are there in a memory?:

.. code-block:: python

    firstname = 'Jan'
    lastname = 'Twardowski'

    f'{firstname} {lastname}'
    # Jan Twardowski

How many string are there in a memory?:

.. code-block:: python

    firstname = 'Jan'
    lastname = 'Twardowski'
    age = 42

    'Hello ' + firstname + ' ' + lastname + ' ' + str(age) + '!'
    # 'Hello Jan Twardowski 42!'

How many string are there in a memory?:

.. code-block:: python

    firstname = 'Jan'
    lastname = 'Twardowski'
    age = 42

    f'Hello {firstname} {lastname} {age}!'
    # 'Hello Jan Twardowski 42!'


Use ``list.append()`` instead of ``str + str``:

.. code-block:: python

    # Performance - Method concatenates strings using + in a loop
    html = '<table>'

    for element in lista:
        html += f'<tr><td>{element}</td></tr>'

    html += '</table>'
    print(html)

.. code-block:: python

    # Problem solved
    html = ['<table>']

    for element in lista:
        html.append(f'<tr><td>{element}</td></tr>')

    html.append('</table>')
    print(''.join(html))


Range between two ``float``
---------------------------
* Uwaga na set zawierający floaty, bo pomiędzy dwoma wartościami jest nieskończona ilość wyrażeń

.. code-block:: python

    range(0, 2)
    # 0
    # 1

    range(0.0, 2.0)
    # ...

Inne
----
* Jeżeli coś ``collections.deque`` - Double ended Queue
* Serializowanie kolejki przy wielowątkowości


Further Reading
---------------
* https://wiki.python.org/moin/TimeComplexity
* https://visualgo.net/bn/sorting
* http://sorting.at/
* https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
* https://www.youtube.com/watch?v=fOdCxum-qLA


Assignments
-----------
.. literalinclude:: assignments/optimization_memoize.py
    :caption: :download:`Solution <assignments/optimization_memoize.py>`
    :end-before: # Solution
