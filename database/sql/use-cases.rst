SQL Use Cases
=============


Use Case - 0x01
---------------
.. code-block:: sql

    SELECT category,
           COUNT(category) AS count

    FROM apollo11

    GROUP BY category
    HAVING count > 50

    ORDER BY category DESC
             NULLS FIRST

    LIMIT 0, 5;



Use Case - 0x02
---------------
.. code-block:: sql

    SELECT *
    FROM logs
    WHERE level in (

        SELECT level
        FROM logs
        GROUP BY level
        HAVING COUNT(*) > 5

    );


Use Case - 0x03
---------------
.. code-block:: sql

    SELECT id,
           firstname AS fname,
           lastname AS lname

    FROM astronauts

    WHERE lastname == 'Watney' AND firstname == 'Mark'
       OR lastname == 'Lewis' AND firstname == 'Melissa'
       OR born BETWEEN '1990-01-01' AND '2000-01-01'
       OR lastname IN ('Martinez', 'Vogel')
       OR lastname IN (
          SELECT lastname
          FROM astronauts
          WHERE lastname LIKE 'Wat%'
       )

    ORDER BY lastname DESC,
             firstname ASC
             NULLS FIRST

    LIMIT 0, 3;


Use Case - 0x04
---------------
.. code-block:: sql

    SELECT
        message,
        level,
        COUNT(level) AS count
    FROM logs
    WHERE (datetime <= '1969-07-18' OR datetime >= '1969-07-20')
      AND message LIKE 'Max__%'
      AND level IN (SELECT DISTINCT(level) FROM logs)
    GROUP BY level
    HAVING count > 5
    ORDER BY datetime DESC
    LIMIT 5;
