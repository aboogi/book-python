Linear Algebra
==============



Linear Algebra
--------------
* ``np.sign()``
* ``np.abs()``
* ``np.sqrt()``
* ``np.power()``

Logarithms
----------
* ``np.log()``
* ``np.log10()``
* ``np.exp()``


Vector and matrix mathematics
-----------------------------


Determinant of a square matrix
------------------------------
.. code-block:: python

    import numpy as np


    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    # array([[ 4., 2., 0.],
    #        [ 9., 3., 7.],
    #        [ 1., 2., 1.]])

    np.linalg.det(a)
    # -53.999999999999993

Inner product
-------------
* Compute inner product of two vectors
* ``np.inner()``
* Ordinary inner product of vectors for 1-D arrays (without complex conjugation)
* In higher dimensions a sum product over the last axes

Ordinary inner product for vectors:

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([0, 1, 0])

    np.inner(a, b)
    # 2

Multidimensional example:

.. code-block:: python

    import numpy as np


    a = np.arange(24).reshape((2,3,4))
    b = np.arange(4)

    np.inner(a, b)
    # array([[ 14,  38,  62],
    #        [ 86, 110, 134]])

Outer product
-------------
* Compute the outer product of two vectors
* ``np.outer()``

.. code-block:: python

    import numpy as np


    a = np.array([1, 4, 0], float)
    b = np.array([2, 2, 1], float)

    np.outer(a, b)
    # array([[ 2., 2., 1.],
    #        [ 8., 8., 4.],
    #        [ 0., 0., 0.]])

An example using a "vector" of letters:

.. code-block:: python

    import numpy as np


    a = np.array(['a', 'b', 'c'], dtype=object)

    np.outer(a, [1, 2, 3])
    # array([['a', 'aa', 'aaa'],
    #        ['b', 'bb', 'bbb'],
    #        ['c', 'cc', 'ccc']], dtype=object)

Cross product
-------------
* The cross product of a and b in R^3 is a vector perpendicular to both a and b
* ``np.cross()``

Vector cross-product:

.. code-block:: python

    import numpy as np


    x = [1, 2, 3]
    y = [4, 5, 6]

    np.cross(x, y)
    # array([-3,  6, -3])

One vector with dimension 2:

.. code-block:: python

    import numpy as np


    x = [1, 2]
    y = [4, 5, 6]

    np.cross(x, y)
    # array([12, -6, -3])


Eigenvalues and vectors of a square matrix
------------------------------------------
* Each of a set of values of a parameter for which a differential equation has a nonzero solution (an eigenfunction) under given conditions
* Any number such that a given matrix minus that number times the identity matrix has a zero determinant

.. code-block:: python

    import numpy as np


    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    # array([[ 4., 2., 0.],
    #        [ 9., 3., 7.],
    #        [ 1., 2., 1.]])

    vals, vecs = np.linalg.eig(a)

    vals
    # array([ 9. , 2.44948974, -2.44948974])

    vecs
    # array([[-0.3538921 , -0.56786837, 0.27843404],
    #        [-0.88473024, 0.44024287, -0.89787873],
    #        [-0.30333608, 0.69549388, 0.34101066]])


Inverse of a square matrix
--------------------------
.. code-block:: python

    import numpy as np


    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    # array([[ 4., 2., 0.],
    #        [ 9., 3., 7.],
    #        [ 1., 2., 1.]])

    np.linalg.inv(a)
    # array([[ 0.14814815, 0.07407407, -0.25925926],
    #        [ 0.2037037 , -0.14814815, 0.51851852],
    #        [-0.27777778, 0.11111111, 0.11111111]])

.. code-block:: python

    import numpy as np


    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    b = np.linalg.inv(a)

    np.dot(a, b)
    # array([[ 1.00000000e+00, 5.55111512e-17, 2.22044605e-16],
    #        [ 0.00000000e+00, 1.00000000e+00, 5.55111512e-16],
    #        [ 1.11022302e-16, 0.00000000e+00, 1.00000000e+00]])


Singular value decomposition of a matrix
----------------------------------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 3, 4], [5, 2, 3]], float)

    U, s, Vh = np.linalg.svd(a)

    U
    # array([[-0.6113829 , -0.79133492],
    #        [-0.79133492, 0.6113829 ]])

    s
    # array([ 7.46791327, 2.86884495])

    Vh
    # array([[-0.61169129, -0.45753324, -0.64536587],
    #        [ 0.78971838, -0.40129005, -0.46401635],
    #        [-0.046676 , -0.79349205, 0.60678804]])


Linear Algebra
--------------
.. csv-table:: Linear algebra basics
    :header-rows: 1

    "Function", "Description"
    "norm", "Vector or matrix norm"
    "inv", "Inverse of a square matrix"
    "solve", "Solve a linear system of equations"
    "det", "Determinant of a square matrix"
    "slogdet", "Logarithm of the determinant of a square matrix"
    "lstsq", "Solve linear least-squares problem"
    "pinv", "Pseudo-inverse (Moore-Penrose) calculated using a singular value decomposition"
    "matrix_power", "Integer power of a square matrix"
    "matrix_rank", "Calculate matrix rank using an SVD-based method"

.. csv-table:: Eigenvalues and decompositions
    :header-rows: 1

    "Function", "Description"
    "eig", "Eigenvalues and vectors of a square matrix"
    "eigh", "Eigenvalues and eigenvectors of a Hermitian matrix"
    "eigvals", "Eigenvalues of a square matrix"
    "eigvalsh", "Eigenvalues of a Hermitian matrix"
    "qr", "QR decomposition of a matrix"
    "svd", "Singular value decomposition of a matrix"
    "cholesky", "Cholesky decomposition of a matrix"

.. csv-table:: Tensor operations
    :header-rows: 1

    "Function", "Description"
    "tensorsolve", "Solve a linear tensor equation"
    "tensorinv", "Calculate an inverse of a tensor"

.. csv-table:: Exceptions
    :header-rows: 1

    "Function", "Description"
    "LinAlgError", "Indicates a failed linear algebra operation"


Assignments
-----------
.. figure:: img/algebra-euclidean-distance.png

    Calculate Euclidean distance in Cartesian coordinate system

* :math:`distance(a, b) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}`
* :math:`distance(a, b) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + ... + (n_2 - n_1)^2}`

.. literalinclude:: assignments/numpy_algebra_euclidean_2d.py
    :caption: :download:`Solution <assignments/numpy_algebra_euclidean_2d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_algebra_euclidean_ndim.py
    :caption: :download:`Solution <assignments/numpy_algebra_euclidean_ndim.py>`
    :end-before: # Solution
