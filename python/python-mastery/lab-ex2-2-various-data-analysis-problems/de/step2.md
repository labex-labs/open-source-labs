# Comprehensions

Listen-, Mengen- und Wörterbuch-Comprehensions können ein nützliches Werkzeug zur Datenmanipulation sein. Beispielsweise versuchen Sie diese Operationen:

```python
>>> # Finden Sie alle Positionen mit mehr als 100 Anteilen
>>> [s for s in portfolio if s['shares'] > 100]
[{'name': 'CAT','shares': 150, 'price': 83.44},
 {'name': 'MSFT','shares': 200, 'price': 51.23}]

>>> # Berechnen Sie die Gesamtkosten (Anteile * Preis)
>>> sum([s['shares']*s['price'] for s in portfolio])
44671.15
>>>

>>> # Finden Sie alle eindeutigen Aktiennamen (Menge)
>>> { s['name'] for s in portfolio }
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
>>>

>>> # Zählen Sie die Gesamtzahl der Anteile jeder Aktie
>>> totals = { s['name']: 0 for s in portfolio }
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
>>>
```
