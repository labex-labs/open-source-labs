# Übung 2.2: Dictionaries als Datenstruktur

Eine Alternative zu einem Tupel ist die Erstellung eines Dictionaries.

```python
>>> d = {
        'name' : row[0],
      'shares' : int(row[1]),
        'price'  : float(row[2])
    }
>>> d
{'name': 'AA','shares': 100, 'price': 32.2 }
>>>
```

Berechnen Sie die Gesamtkosten dieses Portfolios:

```python
>>> cost = d['shares'] * d['price']
>>> cost
3220.0000000000005
>>>
```

Vergleichen Sie dieses Beispiel mit der gleichen Berechnung mit Tupeln oben. Ändern Sie die Anzahl der Anteile auf 75.

```python
>>> d['shares'] = 75
>>> d
{'name': 'AA','shares': 75, 'price': 32.2 }
>>>
```

Im Gegensatz zu Tupeln können Dictionaries frei geändert werden. Fügen Sie einige Attribute hinzu:

```python
>>> d['date'] = (6, 11, 2007)
>>> d['account'] = 12345
>>> d
{'name': 'AA','shares': 75, 'price':32.2, 'date': (6, 11, 2007), 'account': 12345}
>>>
```
