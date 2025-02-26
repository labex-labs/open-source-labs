# Übung 2.26: Das große Ganze

Mit den Techniken aus dieser Übung könnten Sie Anweisungen schreiben, die Felder aus fast jedem spaltenorientierten Datenfile leicht in ein Python-Dictionary umwandeln.

Nur zur Veranschaulichung: Nehmen wir an, Sie lesen Daten aus einer anderen Datendatei wie folgt:

```python
>>> f = open('dowstocks.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> headers
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
>>> row
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
>>>
```

Lassen Sie uns die Felder mit einem ähnlichen Trick umwandeln:

```python
>>> types = [str, float, str, str, float, float, float, float, int]
>>> converted = [func(val) for func, val in zip(types, row)]
>>> record = dict(zip(headers, converted))
>>> record
{'volume': 181800, 'name': 'AA', 'price': 39.48, 'high': 39.69,
'low': 39.45, 'time': '9:36am', 'date': '6/11/2007', 'open': 39.67,
'change': -0.18}
>>> record['name']
'AA'
>>> record['price']
39.48
>>>
```

Bonus: Wie würden Sie dieses Beispiel modifizieren, um den `date`-Eintrag zusätzlich in ein Tupel wie `(6, 11, 2007)` zu parsen?

Nehmen Sie sich ein wenig Zeit, um über das Nachdenken, was Sie in dieser Übung gemacht haben. Wir werden diese Ideen ein wenig später noch einmal aufgreifen.
