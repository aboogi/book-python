Functional Paradigm
===================


Rationale
---------
* Programming paradigm
* Programs are constructed by applying and composing functions
* Functions are treated as first-class citizens
* Functions can be bound to names (including local identifiers), passed as arguments, and returned from other functions, just as any other data type can [#WikipediaFunc]_
* Functional programming avoids side effects, which are used in imperative programming to implement state and I/O
* Pure functional programming completely prevents side-effects and provides referential transparency
* Higher-order functions are rarely used in older imperative programming.
* Imperative program will use a loop to traverse and modify a list, while a functional program, would prefer using a higher-order ``map`` function that takes a function and a list, generating and returning a new list by applying the function to each list item [#Spiewak2008]_
* Restricting side effects, can decrease number of bugs, be easier to debug and test, and be more suited to formal verification [#Hughes1984]_ [#Hudak1989]_
* Functional programming languages are typically less efficient in their use of CPU and memory than imperative languages such as C, Java, Python [#Paulson1996]_
* This is due that some mutable data structures like arrays have a very straightforward implementation using present hardware

.. code-block:: python

    def hello():
        print('My name... José Jiménez')


    type(hello)
    # <class 'function'>

    callable(hello)
    # True


Higher-Order Function
---------------------
* Function can take other function as arguments
* Function can return function

.. code-block:: python

    def lower():
        ...


    def higher():
        return lower

.. code-block:: python

    def http_request(url, on_success, on_error):
        try:
            result = ...
        except Exception as error:
            return on_error(error)
        else:
            return on_success(result)


    http_request(
        url = 'https://python.astrotech.io',
        on_success = lambda result: print(result),
        on_error = lambda error: print(error))


Pure Functions
--------------
* Pure functions have no side effects (i.e. memory, state, I/O)
* If the result of a pure expression is not used, it can be removed without affecting other expressions
* Calling the pure function again with the same arguments returns the same result (this can enable caching optimizations such as memoization)
* If there is no data dependency between two pure expressions, their order can be reversed, or they can be performed in parallel and they cannot interfere with one another (the evaluation of any pure expression is thread-safe)
* Source: [#WikipediaFunc]_

Definition:
    .. code-block:: python

        def add(a, b):
            return a + b


        add(1, 2)
        # 3
        add(1, 2)
        # 3
        add(1, 2)
        # 3

Impure Function:

    .. code-block:: python

        def add(a, b):
            return a + b + c


        c = 3

        add(1, 2)
        # 6
        add(1, 2)
        # 6
        add(1, 2)
        # 6

        c = 4

        add(1, 2)
        # 7
        add(1, 2)
        # 7
        add(1, 2)
        # 7

Pure Function:

    .. code-block:: python

        def add(a, b, c):
            return a + b


        c = 3

        add(1, 2, c)
        # 6
        add(1, 2, c)
        # 6
        add(1, 2, c)
        # 6

        c = 4

        add(1, 2, c)
        # 7
        add(1, 2, c)
        # 7
        add(1, 2, c)
        # 7

Example:

    .. code-block:: python

        def add(a, b):
            return a + b

    .. code-block:: python

        def odd(x):
            return x % 2

    .. code-block:: python

        def cube(x):
            return x ** 3

Use Case [pure]:

    .. code-block:: python

        DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
                (5.1, 3.5, 1.4, 0.2, 'setosa'),
                (5.7, 2.8, 4.1, 1.3, 'versicolor'),
                (6.3, 2.9, 5.6, 1.8, 'virginica'),
                (6.4, 3.2, 4.5, 1.5, 'versicolor'),
                (4.7, 3.2, 1.3, 0.2, 'setosa')]


        def function(data, species):
            result = []
            for *features, label in data:
                if label == species:
                    result.append(features)
            return result

Use Case [impure]:

    .. code-block:: python

        DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
                (5.1, 3.5, 1.4, 0.2, 'setosa'),
                (5.7, 2.8, 4.1, 1.3, 'versicolor'),
                (6.3, 2.9, 5.6, 1.8, 'virginica'),
                (6.4, 3.2, 4.5, 1.5, 'versicolor'),
                (4.7, 3.2, 1.3, 0.2, 'setosa')]


        def function(species):
            result = []
            for *features, label in DATA:
                if label == species:
                    result.append(features)
            return result


Recursion
---------
.. epigraph::

    Aby zrozumieć rekurencję – musisz najpierw zrozumieć rekurencję.

* Also known as recurrence
* Recursive functions invoke themselves, operation is repeated until it reaches the base case
* Iteration (looping) in functional languages is usually accomplished via recursion
* In general, recursion requires maintaining a stack, which consumes space in a linear amount to the depth of recursion. This could make recursion prohibitively expensive to use instead of imperative loops. However, a special form of recursion known as tail recursion can be recognized and optimized by a compiler into the same code used to implement iteration in imperative languages. Tail recursion optimization can be implemented by transforming the program into continuation passing style during compiling, among other approaches. [#WikipediaFunc]_
* CPython doesn't optimize tail recursion
* Tail recursion is not efficient technique in Python
* Rewriting the algorithm iteratively, is generally a better idea
* Unconstrained recursion causes stack overflows!

Recap information about factorial (``n!``):

    5! = 5 * 4!
    4! = 4 * 3!
    3! = 3 * 2!
    2! = 2 * 1!
    1! = 1 * 0!
    0! = 1

Cache with global scope:

.. code-block:: python

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

.. code-block:: python

    factorial(5)                                    # = 120
        return 5 * factorial(4)                     # 5 * 24 = 120
            return 4 * factorial(3)                 # 4 * 6 = 24
                return 3 * factorial(2)             # 3 * 2 = 6
                    return 2 * factorial(1)         # 2 * 1 = 2
                        return 1 * factorial(0)     # 1 * 1 = 1
                            return 1                # 1


Data Structures
---------------
* Purely functional data structures have persistence (keeps previous versions of the data structure unmodified)
* The array with constant access and update times is a basic component of most imperative languages, and many imperative data-structures, such as the hash table and binary heap, are based on arrays
* Arrays can be replaced by maps or random access lists, which admit purely functional implementation, but have logarithmic access and update times
* Source: [#WikipediaFunc]_


Referential Transparency
------------------------
* Functional programs do not have assignment statements
* Value of a variable in a functional program never changes once defined
* This eliminates any chances of side effects
* Any variable can be replaced with its actual value at any point of execution [#Hughes1984]_


First-class Function
--------------------
* Function can be returned
* Function can be user as a parameter
* Function can be assigned to variable
* Function can be stored in data structures such as hash tables, lists, ...

Function can be returned:

.. code-block:: python

    def lower():
        return 'My name... José Jiménez'


    def higher():
        return lower


    result = higher()     # <function __main__.lower()>
    result()              # 'My name... José Jiménez'

.. code-block:: python

    def lower():
        return 'My name... José Jiménez'

    def higher():
        return lower


    a = higher
    b = higher()

    a
    # <function higher at 0x10a999040>

    a()
    # <function lower at 0x10a802a60>

    a()()
    # 'My name... José Jiménez'

    b
    # <function lower at 0x10a802a60>

    b()
    # 'My name... José Jiménez'

Function can be user as a parameter:

.. code-block:: python

    def http_request(url, on_success, on_error):
        try:
            result = ...
        except Exception as error:
            return on_error(error)
        else:
            return on_success(result)


    http_request(
        url = 'https://python.astrotech.io',
        on_success = lambda result: print(result),
        on_error = lambda error: print(error))

Function can be assigned to variable:

.. code-block:: python

    from datetime import datetime
    from time import sleep


    now = datetime.now

    print(now())          # 1969-07-21 02:56:15
    sleep(10)
    print(now())          # 1969-07-21 02:56:25

Function can be stored in data structures such as hash tables, lists, ...:

.. code-block:: python

    def square(x):
        return x ** 2


    def cube(x):
        return x ** 3


    myfunctions = {
        'cube': cube,
        'square': square,
    }


Assignments
-----------
.. literalinclude:: assignments/function_recurrence_a.py
    :caption: :download:`Solution <assignments/function_recurrence_a.py>`
    :end-before: # Solution


References
----------
.. [#WikipediaFunc] Functional programming. URL: https://en.wikipedia.org/wiki/Functional_programming Retrieved: 2020-10-09
.. [#Hudak1989] Hudak, Paul. "Conception, evolution, and application of functional programming languages". ACM Computing Surveys. 21 (3): 359–411. doi:10.1145/72551.72554. S2CID 207637854. 1989.
.. [#Hughes1984] Hughes, John. "Why Functional Programming Matters". Chalmers University of Technology. 1984.
.. [#Spiewak2008] Spiewak, Daniel. "Implementing Persistent Vectors in Scala". Code Commit. 2008.
.. [#Paulson1996] Paulson, Larry C. "ML for the Working Programmer". Cambridge University Press. ISBN: 978-0-521-56543-1. Retrieved: 2013-02-10. 1996.
