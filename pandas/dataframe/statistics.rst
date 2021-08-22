DataFrame Statistics
====================

.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    df = pd.DataFrame(
        columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
        index = pd.date_range('1999-12-30', periods=7),
        data = np.random.randn(7, 4))

    df
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Count
-----
Number of non-null observations:

.. code-block:: python

    df.count()
    # Morning     7
    # Noon        7
    # Evening     7
    # Midnight    7
    # dtype: int64

.. code-block:: python

    df.value_counts()

.. code-block:: python

    df.nunique()


Sum
---
Sum of values:

.. code-block:: python

    df.sum()
    # Morning     5.500273
    # Noon       -1.050752
    # Evening     3.739996
    # Midnight    2.094039
    # dtype: float64

Cumulative sum:

.. code-block:: python

    df.cumsum()
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  3.631610 -0.577121  1.928826  2.089536
    # 2000-01-01  3.528391 -0.166522  2.072870  3.543809
    # 2000-01-02  4.289429 -0.044847  2.516733  3.877484
    # 2000-01-03  5.783508 -0.250005  2.829801  3.023388
    # 2000-01-04  3.230518  0.403613  3.694237  2.281223
    # 2000-01-05  5.500273 -1.050752  3.739996  2.094039


Product
-------
Product of values:

.. code-block:: python

    df.prod()
    # Morning     2.240538
    # Noon       -0.003810
    # Evening     0.000736
    # Midnight    0.019528
    # dtype: float64

Cumulative product:

.. code-block:: python

    df.cumprod()
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  3.294470 -0.391065  0.929888 -0.339175
    # 2000-01-01 -0.340051 -0.160571  0.133944 -0.493254
    # 2000-01-02 -0.258792 -0.019537  0.059453 -0.164586
    # 2000-01-03 -0.386656  0.004008  0.018613  0.140572
    # 2000-01-04  0.987128  0.002620  0.016090 -0.104328
    # 2000-01-05  2.240538 -0.003810  0.000736  0.019528


Extremes
--------
Minimum, index of minimum and cumulative minimum:

.. code-block:: python

    df.min()
    # Morning    -2.552990
    # Noon       -1.454366
    # Evening     0.045759
    # Midnight   -0.854096
    # dtype: float64

    df.idxmin()
    # Morning    2000-01-04
    # Noon       2000-01-05
    # Evening    2000-01-05
    # Midnight   2000-01-03
    # dtype: datetime64[ns]

    df.cummin()

Maximum, index of maximum and cumulative maximum:

.. code-block:: python

    df.max()
    # Morning     2.269755
    # Noon        0.653619
    # Evening     0.978738
    # Midnight    2.240893
    # dtype: float64

.. code-block:: python

    df.idxmax()
    # Morning    2000-01-05
    # Noon       2000-01-04
    # Evening    1999-12-30
    # Midnight   1999-12-30
    # dtype: datetime64[ns]

    df.cummax()


Average
-------
Arithmetic mean of values:

.. code-block:: python

    df.mean()
    # Morning     0.785753
    # Noon       -0.150107
    # Evening     0.534285
    # Midnight    0.299148
    # dtype: float64

Arithmetic median of values:

.. code-block:: python

    df.median()
    # Morning     1.494079
    # Noon        0.121675
    # Evening     0.443863
    # Midnight   -0.151357
    # dtype: float64

Mode:

.. code-block:: python

    df.mode()

Rolling Average:

.. code-block:: python

    df.rolling(window=30)

.. figure:: img/pandas-dataframe-stats-rolling.png

    Rolling Average

Distribution
------------
Absolute value:

.. code-block:: python

    df.abs()

Standard deviation:

.. code-block:: python

    df.std()
    # Morning     1.671798
    # Noon        0.787967
    # Evening     0.393169
    # Midnight    1.151785
    # dtype: float64

.. figure:: img/pandas-dataframe-stats-stdev.png

    Standard Deviation

Mean absolute deviation:

.. code-block:: python

    df.mad()

Standard Error of the Mean (SEM):

.. code-block:: python

    df.sem()

.. figure:: img/pandas-dataframe-stats-sem.png

    Standard Error of the Mean (SEM)

Skewness (3rd moment):

.. code-block:: python

    df.skew()

.. figure:: img/pandas-dataframe-stats-skew.png

    Skewness

Kurtosis (4th moment):

.. code-block:: python

    df.kurt()

.. figure:: img/pandas-dataframe-stats-kurt.png

    Kurtosis

Sample quantile (value at %). Quantile also known as Percentile:

.. code-block:: python

    df.quantile(.33)
    # Morning     0.743753
    # Noon       -0.220601
    # Evening     0.309687
    # Midnight   -0.198283
    # Name: 0.33, dtype: float64

    df.quantile([.25, .5, .75])
    #        Morning      Noon   Evening  Midnight
    # 0.25  0.328909 -0.591218  0.228556 -0.464674
    # 0.50  1.494079  0.121675  0.443863 -0.151357
    # 0.75  1.815805  0.405378  0.907262  0.893974

Variance:

.. code-block:: python

    df.var()
    # Morning     2.794907
    # Noon        0.620892
    # Evening     0.154582
    # Midnight    1.326610
    # dtype: float64

Correlation Coefficient:

.. code-block:: python

    df.corr()
    #            Morning      Noon   Evening  Midnight
    # Morning   1.000000 -0.698340 -0.190219  0.201034
    # Noon     -0.698340  1.000000  0.307686  0.359761
    # Evening  -0.190219  0.307686  1.000000  0.136436
    # Midnight  0.201034  0.359761  0.136436  1.000000

.. figure:: img/pandas-dataframe-stats-corr.png

    Correlation Coefficient


Describe
--------
.. code-block:: python

    df.describe()
    #         Morning      Noon   Evening  Midnight
    # count  7.000000  7.000000  7.000000  7.000000
    # mean   0.785753 -0.150107  0.534285  0.299148
    # std    1.671798  0.787967  0.393169  1.151785
    # min   -2.552990 -1.454366  0.045759 -0.854096
    # 25%    0.328909 -0.591218  0.228556 -0.464674
    # 50%    1.494079  0.121675  0.443863 -0.151357
    # 75%    1.815805  0.405378  0.907262  0.893974
    # max    2.269755  0.653619  0.978738  2.240893


Examples
--------
.. code-block:: python

    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/phones-en.csv'

    df = pd.read_csv(DATA, parse_dates=['date'])
    df.drop(columns='index', inplace=True)

.. csv-table:: Data
    :header: Column, Description
    :widths: 10, 90

    "date", "The date and time of the entry"
    "duration", "The duration (in seconds) for each call, the amount of data (in MB) for each data entry, and the number of texts sent (usually 1) for each sms entry"
    "item", "A description of the event occurring – can be one of call, sms, or data"
    "month", "The billing month that each entry belongs to – of form ``YYYY-MM``"
    "network", "The mobile network that was called/texted for each entry"
    "network_type", "Whether the number being called was a mobile, international ('world'), voicemail, landline, or other ('special') number."

How many rows the dataset:

.. code-block:: python

    df['item'].count()
    # 830

What was the longest phone call / data entry?:

.. code-block:: python

    df['duration'].max()
    # 10528.0

How many seconds of phone calls are recorded in total?:

.. code-block:: python

    df.loc[ df['item'] == 'call' ]['duration'].sum()
    # 92321.0

How many entries are there for each month?:

.. code-block:: python

    df['month'].value_counts()
    # 2014-11  230
    # 2015-01  205
    # 2014-12  157
    # 2015-02  137
    # 2015-03  101
    # dtype: int64

Number of non-null unique network entries:

.. code-block:: python

    df['network'].nunique()
    # 9


Assignments
-----------
.. literalinclude:: assignments/pandas_df_statistics_a.py
    :caption: :download:`Solution <assignments/pandas_df_statistics_a.py>`
    :end-before: # Solution
