# Übung 7.2: Übergabe von Tupeln und Wörterbüchern als Argumente

Nehmen wir an, Sie lesen einige Daten aus einer Datei und erhalten ein Tupel wie dieses:

```python
>>> data = ('GOOG', 100, 490.1)
>>>
```

Nun, nehmen wir an, Sie möchten ein `Stock`-Objekt aus diesen Daten erstellen. Wenn Sie versuchen, `data` direkt zu übergeben, funktioniert das nicht:

```python
>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Stock.__init__() missing 2 required positional arguments:'shares' and 'price'
>>>
```

Dies lässt sich leicht beheben, indem Sie `*data` verwenden. Probieren Sie das:

```python
>>> s = Stock(*data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

Wenn Sie ein Wörterbuch haben, können Sie stattdessen `**` verwenden. Beispielsweise:

```python
>>> data = { 'name': 'GOOG','shares': 100, 'price': 490.1 }
>>> s = Stock(**data)
Stock('GOOG', 100, 490.1)
>>>
```
