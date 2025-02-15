"""
* Assignment: About EntryTest ListDict
* Complexity: hard
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Define `result: list[dict]`, where each dict has keys:
       * address: str
       * hosts: list[str]
    2. Iterate over lines in `DATA` skipping comments (`#`) and empty lines
    3. Extract from each line: `address` and `hosts`
    4. Add `address` and `hosts` to `result` as a dict, example:
       {'address': '127.0.0.1', 'hosts': ['localhost', 'astromatt']}
    5. Each line must be a separate dict
    6. Merge host names with the same IP (important!)
    7. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[dict]`, gdzie każdy dict ma klucze:
       * address: str
       * hosts: list[str]
    2. Iteruje po liniach w `DATA` pomijając komentarze (`#`) i puste linie
    3. Wyciągnij z każdej linii: `address` i `hosts`
    4. Dodaj `address` i `hosts` do `result` jako słownik, przykład:
       {'address': '127.0.0.1', 'hosts': ['localhost', 'astromatt']}
    5. Każda linia ma być osobnym słownikiem
    6. Scal nazwy hostów dla tego samego IP (ważne)
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result` instead of Ellipsis `...`'
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is dict for x in result), \
    'All keys in `result` should be dict'
    >>> assert [x['address'] for x in result].count('127.0.0.1') == 1, \
    'You did not merge hostnames for the same ip (127.0.0.1)'

    >>> pprint(result, width=120)
    [{'address': '127.0.0.1', 'hosts': ['localhost', 'astromatt']},
     {'address': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int', 'roscosmos.ru']},
     {'address': '255.255.255.255', 'hosts': ['broadcasthost']},
     {'address': '::1', 'hosts': ['localhost']}]
"""

DATA = """##
# `/etc/hosts` structure:
#   - IPv4 or IPv6
#   - Hostnames
 ##

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost"""

# list[dict]: keys: address, hosts, protocol; merge hosts for the same ip
#             protocol is 'ipv4' when '.' is in address; use conditional expr.
result = ...


# Solution
result = []
for line in DATA.splitlines():
    line = line.strip()

    if len(line) == 0:
        continue
    elif line.startswith('#'):
        continue

    address, *hosts = line.split()

    for row in result:
        if row['address'] == address:
            row['hosts'] += hosts
            break
    else:
        row = {'address': address, 'hosts': hosts}
        result.append(row)
