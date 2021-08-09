Multiprocessing
===============

.. glossary::

    IPC
        Inter Process Communication

    Process
    Daemon
    Dead Lock
    Race Condition
    Starvation


Problems
--------
* Zakleszczania
* Race Condition


Cykl życia procesów
-------------------
* Tworzenie procesów
* Zamykanie procesów
* Multiprocesowość
* Komunikacja między procesami


Rationale
---------
* IPC - Inter-Process Communication
* Aby ``pickle`` mógł odtworzyć obiekt, musi posiadać jego definicję - klasę.


Define payload
--------------
``iris.py``:

.. code-block:: python

    from dataclasses import dataclass

    @dataclass
    class Iris:
        sepal_length: float
        sepal_width: float
        petal_length: float
        petal_width: float
        species: str

        def sepal_area(self):
            return self.sepal_length * self.sepal_width

        def petal_area(self):
            return self.petal_length * self.petal_width

        def total_area(self):
            return self.sepal_area() + self.petal_area()

Client
------
* Obiekt wysyłający dane ``multiprocessing-client.py``:

.. code-block:: python

    import pickle
    from multiprocessing.connection import Client
    from iris import Iris


    flower = Iris(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2,
        species='setosa'
    )

    payload = pickle.dumps(flower)


    ADDRESS = ('localhost', 6000)
    PASSWORD = b'My voice is my password, verify me.'

    connection = Client(ADDRESS, authkey=PASSWORD)
    connection.send(payload)
    connection.send('close')
    connection.close()


Listener
--------
* Obiekt nasłuchujący na połączenia ``multiprocessing-listener.py``:

.. code-block:: python

    import pickle
    from multiprocessing.connection import Listener
    from iris import Iris


    ADDRESS = ('localhost', 6000)
    PASSWORD = b'My voice is my password, verify me.'

    listener = Listener(ADDRESS, authkey=PASSWORD)
    connection = listener.accept()

    while True:
        payload = connection.recv()

        if payload == 'close':
            connection.close()
            break

        flower = pickle.loads(payload)
        area = flower.total_area()
        print(f'Area: {area}')

    listener.close()


Assignments
-----------
.. literalinclude:: assignments/multiprocessing_client.py
    :caption: :download:`Solution <assignments/multiprocessing_client.py>`
    :end-before: # Solution

.. literalinclude:: assignments/multiprocessing_server.py
    :caption: :download:`Solution <assignments/multiprocessing_server.py>`
    :end-before: # Solution
