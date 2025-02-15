"""
* Assignment: Decorator Arguments Syntax
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define decorator `mydecorator`
    2. Decorator should take `a` and `b` as arguments
    2. Define `wrapper` with `*args` and `**kwargs` parameters
    3. Wrapper should call original function with its original parameters,
       and return its value
    4. Decorator should return `wrapper` function
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj dekorator `mydecorator`
    2. Dekorator powinien przyjmować `a` i `b` jako argumenty
    2. Zdefiniuj `wrapper` z parametrami `*args` i `**kwargs`
    3. Wrapper powinien wywoływać oryginalną funkcję z jej oryginalnymi
       parametrami i zwracać jej wartość
    4. Decorator powinien zwracać funckję `wrapper`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(mydecorator), \
    'Create mydecorator() function'

    >>> assert isfunction(mydecorator(1, 2)), \
    'mydecorator() should take two positional arguments'

    >>> assert isfunction(mydecorator(a=1, b=2)), \
    'mydecorator() should take two keyword arguments: a and b'

    >>> assert isfunction(mydecorator(a=1, b=2)(lambda: ...)), \
    'mydecorator() should return decorator which can take a function as arg'

    >>> @mydecorator(a=1, b=2)
    ... def echo(text):
    ...     return text

    >>> echo('hello')
    'hello'
"""


# Solution
def mydecorator(a, b):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator
