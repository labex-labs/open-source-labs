# Teil 4 : Wörterbücher

In den letzten Teilen haben Sie lediglich mit Aktiensymbolen gearbeitet. Angenommen, Sie möchten jedoch Aktiensymbole auf andere Daten wie den Preis abbilden. Verwenden Sie ein Wörterbuch:

```python
>>> prices = { 'IBM': 91.1, 'GOOG': 490.1, 'AAPL':312.23 }
>>>
```

Ein Wörterbuch bildet Schlüssel auf Werte ab. So können Sie darauf zugreifen:

```python
>>> prices['IBM']
91.1
>>> prices['IBM'] = 123.45
>>> prices['HPQ'] = 26.15
>>> prices
{'GOOG': 490.1, 'AAPL': 312.23, 'IBM': 123.45, 'HPQ': 26.15}
>>>
```

Um eine Liste der Schlüssel zu erhalten, verwenden Sie dies:

```python
>>> list(prices)
['GOOG', 'AAPL', 'IBM', 'HPQ']
>>>
```

Um einen Wert zu löschen, verwenden Sie `del`

```python
>>> del prices['AAPL']
>>> prices
{'GOOG': 490.1, 'IBM': 123.45, 'HPQ': 26.15}
>>>
```
