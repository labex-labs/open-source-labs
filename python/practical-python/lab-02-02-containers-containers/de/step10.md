# Übung 2.5: Liste von Dictionaries

Nehmen Sie die Funktion, die Sie in Übung 2.4 geschrieben haben, und ändern Sie sie so, dass jedes Aktie im Portfolio durch ein Dictionary statt eines Tupels dargestellt wird. Verwenden Sie in diesem Dictionary die Feldnamen "name", "shares" und "price", um die verschiedenen Spalten in der Eingabedatei darzustellen.

Experimentieren Sie mit dieser neuen Funktion auf die gleiche Weise wie in Übung 2.4.

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
    {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
    {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
    {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> portfolio[0]
{'name': 'AA','shares': 100, 'price': 32.2}
>>> portfolio[1]
{'name': 'IBM','shares': 50, 'price': 91.1}
>>> portfolio[1]['shares']
50
>>> total = 0.0
>>> for s in portfolio:
        total += s['shares']*s['price']

>>> print(total)
44671.15
>>>
```

Hier werden Sie bemerken, dass die verschiedenen Felder für jede Eingabe über Schlüsselnamen statt numerischer Spaltennummern zugegriffen werden. Dies ist oft bevorzugt, da der resultierende Code später einfacher lesbar ist.

Das Anzeigen großer Dictionaries und Listen kann chaotisch sein. Um die Ausgabe für das Debugging zu bereinigen, können Sie die `pprint`-Funktion verwenden.

```python
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2,'shares': 100},
    {'name': 'IBM', 'price': 91.1,'shares': 50},
    {'name': 'CAT', 'price': 83.44,'shares': 150},
    {'name': 'MSFT', 'price': 51.23,'shares': 200},
    {'name': 'GE', 'price': 40.37,'shares': 95},
    {'name': 'MSFT', 'price': 65.1,'shares': 50},
    {'name': 'IBM', 'price': 70.44,'shares': 100}]
>>>
```
