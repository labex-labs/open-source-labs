# Übung 2.22: Datenextraktion

Zeigen Sie, wie Sie eine Liste von Tupeln `(name, shares)` erstellen könnten, wobei `name` und `shares` aus `portfolio` entnommen werden.

```python
>>> name_shares =[ (s['name'], s['shares']) for s in portfolio ]
>>> name_shares
[('AA', 100), ('IBM', 50), ('CAT', 150), ('MSFT', 200), ('GE', 95), ('MSFT', 50), ('IBM', 100)]
>>>
```

Wenn Sie die eckigen Klammern (`[`, `]`) durch geschweifte Klammern (`{`, `}`) ersetzen, erhalten Sie etwas, das als Mengenverständnis bekannt ist. Dies liefert Ihnen einzigartige oder unterschiedliche Werte.

Zum Beispiel bestimmt dies die Menge der einzigartigen Aktiennamen, die in `portfolio` auftauchen:

```python
>>> names = { s['name'] for s in portfolio }
>>> names
{ 'AA', 'GE', 'IBM', 'MSFT', 'CAT' }
>>>
```

Wenn Sie `Schlüssel:Wert`-Paare angeben, können Sie ein Wörterbuch erstellen. Beispielsweise erstellen Sie ein Wörterbuch, das den Namen einer Aktie auf die Gesamtzahl der gehaltenen Aktien abbildet.

```python
>>> holdings = { name: 0 for name in names }
>>> holdings
{'AA': 0, 'GE': 0, 'IBM': 0, 'MSFT': 0, 'CAT': 0}
>>>
```

Dieses letzte Feature ist als **Wörterbuchverständnis** bekannt. Tabellieren wir:

```python
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
{ 'AA': 100, 'GE': 95, 'IBM': 150, 'MSFT':250, 'CAT': 150 }
>>>
```

Versuchen Sie dieses Beispiel, das das `prices`-Wörterbuch auf nur die Namen reduziert, die in `portfolio` auftauchen:

```python
>>> portfolio_prices = { name: prices[name] for name in names }
>>> portfolio_prices
{'AA': 9.22, 'GE': 13.48, 'IBM': 106.28, 'MSFT': 20.89, 'CAT': 35.46}
>>>
```
