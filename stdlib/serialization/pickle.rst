Serialization Pickle
====================


What is ``pickle``?
-------------------------------------------------------------------------------
* Python object serialization format
* ``pickle`` vs. ``cPickle``


Serialize data types
-------------------------------------------------------------------------------

Dump to string
--------------
.. code-block:: python

    import pickle


    pickle.dumps('Jan Twardowski')
    # b'\x80\x03X\x0e\x00\x00\x00Jan Twardowskiq\x00.'

    pickle.dumps(1)
    # b'\x80\x03K\x01.'

    pickle.dumps(1.0)
    # b'\x80\x03G?\xf0\x00\x00\x00\x00\x00\x00.'

    pickle.dumps(1.2)
    # b'\x80\x03G?\xf3333333.'

    pickle.dumps(1.5)
    # b'\x80\x03G?\xf8\x00\x00\x00\x00\x00\x00.'

Load from string
----------------
.. code-block:: python

    import pickle


    pickle.loads(b'\x80\x03X\x0e\x00\x00\x00Jan Twardowskiq\x00.')
    # 'Jan Twardowski'

    pickle.loads(b'\x80\x03K\x01.')
    # 1

    pickle.loads(b'\x80\x03G?\xf0\x00\x00\x00\x00\x00\x00.')
    # 1.0

    pickle.loads(b'\x80\x03G?\xf3333333.')
    # 1.2

    pickle.loads(b'\x80\x03G?\xf8\x00\x00\x00\x00\x00\x00.')
    # 1.5


Serialize sequences
-------------------------------------------------------------------------------

Dump to string
--------------
.. code-block:: python

    import pickle


    pickle.dumps([1, 2, 3])
    # b'\x80\x03]q\x00(K\x01K\x02K\x03e.

    pickle.dumps((1, 2, 3))
    # b'\x80\x03K\x01K\x02K\x03\x87q\x00.'

    pickle.dumps({1, 2, 3})
    # b'\x80\x03cbuiltins\nset\nq\x00]q\x01(K\x01K\x02K\x03e\x85q\x02Rq\x03.'

    pickle.dumps({'a': 1, 'b': 2, 'c': 3})
    # b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02X\x01\x00\x00\x00cq\x03K\x03u.'

Load from string
----------------
.. code-block:: python

    import pickle


    pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03e.)
    # [1, 2, 3]

    pickle.loads(b'\x80\x03K\x01K\x02K\x03\x87q\x00.')
    # (1, 2, 3)

    pickle.loads(b'\x80\x03cbuiltins\nset\nq\x00]q\x01(K\x01K\x02K\x03e\x85q\x02Rq\x03.')
    # {1, 2, 3}

    pickle.loads(b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02X\x01\x00\x00\x00cq\x03K\x03u.')
    # {'a': 1, 'b': 2, 'c': 3}


Serialize Dates and Datetimes
-------------------------------------------------------------------------------
.. code-block:: python

    import pickle


    dt = datetime(1969, 7, 21, 2, 56, 15)
    pickle.dumps(dt)
    # b'\x80\x03cdatetime\ndatetime\nq\x00C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00q\x01\x85q\x02Rq\x03.'

.. code-block:: python

    import pickle


    pickle.loads(b'\x80\x03cdatetime\ndatetime\nq\x00C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00q\x01\x85q\x02Rq\x03.')
    # datetime.datetime(1969, 7, 21, 2, 56, 15)


Serialize and deserialize objects
-------------------------------------------------------------------------------
.. code-block:: python

    import pickle


    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

    jan = Astronaut('Jan', 'Twardowski')

    pickle.dumps(jan)
    # b'\x80\x03c__main__\nAstronaut\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00firstnameq\x03X\x03\x00\x00\x00Janq\x04X\t\x00\x00\x00lastnameq\x05X\n\x00\x00\x00Twardowskiq\x06ub.'

    pickle.loads(b'\x80\x03c__main__\nAstronaut\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00firstnameq\x03X\x03\x00\x00\x00Janq\x04X\t\x00\x00\x00lastnameq\x05X\n\x00\x00\x00Twardowskiq\x06ub.')
    # <__main__.Astronaut object at 0x10585f8d0>


Serialize and deserialize to file
-------------------------------------------------------------------------------
* File extension ``pkl``

Dump to file
------------
Dump to file:

.. code-block:: python

    import pickle


    DATA = [1, 2, 3]

    with open('filename.pkl', mode='wb') as file:
        pickle.dump(DATA, file)

Load from file
--------------
Load from file:

.. code-block:: python

    import pickle


    with open('filename.pkl', mode='rb') as file:
        result = pickle.load(file)

    print(result)


Examples
-------------------------------------------------------------------------------
Advanced Example:

.. code-block:: python

    import pickle
    from datetime import datetime, timezone, timedelta


    def month_ago(dt):
        return dt - timedelta(days=30)


    class Astronaut:
        agency = 'NASA'

        def __init__(self, name):
            self.name = name


    jose = Astronaut(name='José Jiménez')
    now = datetime.now(tz=timezone.utc)


    DATA = [
        jose,
        Astronaut,
        month_ago(now),
        str(now),
        now.__str__(),
        '{}'.format(now),
        f'{now}',
        {'imie': 'Иван', 'nazwisko': 'Иванович'},
        {10, 20, 30},
        (1,),
        10,
        10.5,
    ]

    pickle.dumps(DATA)
    # b'\x80\x03]q\x00(c__main__\nAstronaut\nq\x01)\x81q\x02}q\x03X\x04\x00\x00\x00nameq\x04X\x0c\x00\x00\x00Jose Jimenezq\x05sbh\x01cdatetime\ndatetime\nq\x06C\n\x07\xe2\t\x0b\r\n\x05\x04\xa9\xfdq\x07cdatetime\ntimezone\nq\x08cdatetime\ntimedelta\nq\tK\x00K\x00K\x00\x87q\nRq\x0b\x85q\x0cRq\r\x86q\x0eRq\x0fX \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x10X \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x11X \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x12X \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x13}q\x14(X\x04\x00\x00\x00imieq\x15X\x08\x00\x00\x00\xd0\x98\xd0\xb2\xd0\xb0\xd0\xbdq\x16X\x08\x00\x00\x00nazwiskoq\x17X\x10\x00\x00\x00\xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb8\xd1\x87q\x18ucbuiltins\nset\nq\x19]q\x1a(K\nK\x14K\x1ee\x85q\x1bRq\x1cK\x01\x85q\x1dK\nG@%\x00\x00\x00\x00\x00\x00e.'

    pickle.loads(b'\x80\x03]q\x00(c__main__\nAstronaut\nq\x01)\x81q\x02}q\x03X\x04\x00\x00\x00nameq\x04X\x0c\x00\x00\x00Jose Jimenezq\x05sbh\x01cdatetime\ndatetime\nq\x06C\n\x07\xe2\t\x0b\r\n\x05\x04\xa9\xfdq\x07cdatetime\ntimezone\nq\x08cdatetime\ntimedelta\nq\tK\x00K\x00K\x00\x87q\nRq\x0b\x85q\x0cRq\r\x86q\x0eRq\x0fX \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x10X \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x11X \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x12X \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x13}q\x14(X\x04\x00\x00\x00imieq\x15X\x08\x00\x00\x00\xd0\x98\xd0\xb2\xd0\xb0\xd0\xbdq\x16X\x08\x00\x00\x00nazwiskoq\x17X\x10\x00\x00\x00\xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb8\xd1\x87q\x18ucbuiltins\nset\nq\x19]q\x1a(K\nK\x14K\x1ee\x85q\x1bRq\x1cK\x01\x85q\x1dK\nG@%\x00\x00\x00\x00\x00\x00e.')
    # [
    #   <__main__.Astronaut object at 0x10585f850>,
    #   <class '__main__.Astronaut'>,
    #   datetime.datetime(2018, 9, 11, 13, 10, 5, 305661, tzinfo=datetime.timezone.utc),
    #   '2018-10-11 13:10:05.305661+00:00',
    #   '2018-10-11 13:10:05.305661+00:00',
    #   '2018-10-11 13:10:05.305661+00:00',
    #   '2018-10-11 13:10:05.305661+00:00',
    #   {'imie': 'Иван', 'nazwisko': 'Иванович'},
    #   {10, 20, 30},
    #   (1,),
    #   10,
    #   10.5
    # ]


Assignments
-------------------------------------------------------------------------------
.. literalinclude:: assignments/serialization_pickle_a.py
    :caption: :download:`Solution <assignments/serialization_pickle_a.py>`
    :end-before: # Solution
