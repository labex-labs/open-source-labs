# Wörterbücher als Container

Wörterbücher sind nützlich, wenn Sie schnelle Zufallsabfragen (nach Schlüsselnamen) durchführen möchten. Beispielsweise ein Wörterbuch mit Aktienkursen:

```python
prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}
```

Hier sind einige einfache Abfragen:

```python
>>> prices['IBM']
93.37
>>> prices['GOOG']
513.25
>>>
```
