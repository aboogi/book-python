"""
* Assignment: OOP Interface Implement
* Complexity: easy
* Lines of code: 12 lines
* Time: 8 min

English:
    1. Define class `Setosa` implementing `IrisInterface`
    2. Implement interface
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Setosa` implementującą `IrisInterface`
    2. Zaimplementuj interfejs
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(self).values()`
    * `mean = sum() / len()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert issubclass(Setosa, IrisInterface)

    >>> assert hasattr(Setosa, '__annotations__'), \
    'Setosa has no field type annotations'

    >>> assert hasattr(Setosa, 'mean'), \
    'Setosa has no method .mean()'

    >>> assert hasattr(Setosa, 'sum'), \
    'Setosa has no method .sum()'

    >>> assert hasattr(Setosa, 'len'), \
    'Setosa has no method .len()'

    >>> assert isfunction(Setosa.mean), \
    'Setosa.mean() is not a method'

    >>> assert isfunction(Setosa.sum), \
    'Setosa.sum() is not a method'

    >>> assert isfunction(Setosa.len), \
    'Setosa.len() is not a method'

    >>> Setosa.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>,
     'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>,
     'petal_width': <class 'float'>}

    >>> setosa = Setosa(5.1, 3.5, 1.4, 0.2)
    >>> setosa.len()
    4
    >>> setosa.sum()
    10.2
    >>> setosa.mean()
    2.55
"""

class IrisInterface:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:
        raise NotImplementedError

    def mean(self) -> float:
        raise NotImplementedError

    def sum(self) -> float:
        raise NotImplementedError

    def len(self) -> int:
        raise NotImplementedError


# Solution
class Setosa(IrisInterface):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def mean(self) -> float:
        return self.sum() / self.len()

    def sum(self) -> float:
        return sum(vars(self).values())

    def len(self) -> int:
        return len(vars(self))
