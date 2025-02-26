# Verwendung der zip()-Funktion

Die `zip()`-Funktion wird am häufigsten verwendet, um Daten zu verknüpfen. Beispielsweise erinnern Sie sich daran, dass Sie eine `headers`-Variable erstellt haben:

```python
>>> headers
['name','shares', 'price']
>>>
```

Dies könnte nützlich sein, um es mit den anderen Zeilendaten zu kombinieren:

```python
>>> row = rows[0]
>>> row
['AA', '100', '32.20']
>>> for col, val in zip(headers, row):
        print(col, val)

name AA
shares 100
price 32.20
>>>
```

Oder Sie können es vielleicht verwenden, um ein Dictionary zu erstellen:

```python
>>> dict(zip(headers, row))
{'name': 'AA','shares': '100', 'price': '32.20'}
>>>
```

Oder vielleicht eine Sequenz von Dictionaries:

```python
>>> for row in rows:
        record = dict(zip(headers, row))
        print(record)

{'name': 'AA','shares': '100', 'price': '32.20'}
{'name': 'IBM','shares': '50', 'price': '91.10'}
{'name': 'CAT','shares': '150', 'price': '83.44'}
{'name': 'MSFT','shares': '200', 'price': '51.23'}
{'name': 'GE','shares': '95', 'price': '40.37'}
{'name': 'MSFT','shares': '50', 'price': '65.10'}
{'name': 'IBM','shares': '100', 'price': '70.44'}
>>>
```
