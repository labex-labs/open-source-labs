# Übung 2.21: Datenabfragen

Versuchen Sie die folgenden Beispiele verschiedener Datenabfragen.

Zunächst eine Liste aller Portfolio-Holdings mit mehr als 100 Aktien.

```python
>>> more100 = [ s for s in portfolio if s['shares'] > 100 ]
>>> more100
[{'price': 83.44, 'name': 'CAT','shares': 150}, {'price': 51.23, 'name': 'MSFT','shares': 200}]
>>>
```

Alle Portfolio-Holdings für MSFT- und IBM-Aktien.

```python
>>> msftibm = [ s for s in portfolio if s['name'] in {'MSFT','IBM'} ]
>>> msftibm
[{'price': 91.1, 'name': 'IBM','shares': 50}, {'price': 51.23, 'name': 'MSFT','shares': 200},
  {'price': 65.1, 'name': 'MSFT','shares': 50}, {'price': 70.44, 'name': 'IBM','shares': 100}]
>>>
```

Eine Liste aller Portfolio-Holdings, die mehr als 10000 Dollar kosten.

```python
>>> cost10k = [ s for s in portfolio if s['shares'] * s['price'] > 10000 ]
>>> cost10k
[{'price': 83.44, 'name': 'CAT','shares': 150}, {'price': 51.23, 'name': 'MSFT','shares': 200}]
>>>
```
