# Übung 2.17: Umkehren eines Wörterbuchs

Ein Wörterbuch bildet Schlüssel auf Werte ab. Beispielsweise ein Wörterbuch mit Aktienpreisen.

```python
>>> prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }
>>>
```

Wenn Sie die `items()`-Methode verwenden, können Sie `(Schlüssel,Wert)`-Paare erhalten:

```python
>>> prices.items()
dict_items([('GOOG', 490.1), ('AA', 23.45), ('IBM', 91.1), ('MSFT', 34.23)])
>>>
```

Was passiert aber, wenn Sie stattdessen eine Liste von `(Wert,Schlüssel)`-Paaren erhalten möchten? _Hinweis: Verwenden Sie `zip()`._

```python
>>> pricelist = list(zip(prices.values(),prices.keys()))
>>> pricelist
[(490.1, 'GOOG'), (23.45, 'AA'), (91.1, 'IBM'), (34.23, 'MSFT')]
>>>
```

Warum würden Sie das tun? Einerseits ermöglicht es Ihnen, bestimmte Arten von Datenverarbeitung auf den Wörterbuchdaten durchzuführen.

```python
>>> min(pricelist)
(23.45, 'AA')
>>> max(pricelist)
(490.1, 'GOOG')
>>> sorted(pricelist)
[(23.45, 'AA'), (34.23, 'MSFT'), (91.1, 'IBM'), (490.1, 'GOOG')]
>>>
```

Dies veranschaulicht auch eine wichtige Eigenschaft von Tupeln. Wenn sie in Vergleichen verwendet werden, werden Tupel elementweise beginnend mit dem ersten Element verglichen. Ähnlich wie Strings zeichenweise verglichen werden.

`zip()` wird oft in Situationen wie dieser verwendet, in denen Sie Daten aus verschiedenen Quellen paarweise zusammenbringen müssen. Beispielsweise die Spaltennamen mit den Spaltenwerten zu einem Wörterbuch von benanntem Werten zusammenbringen.

Beachten Sie, dass `zip()` nicht auf Paare beschränkt ist. Beispielsweise können Sie es mit beliebig vielen Eingabelisten verwenden:

```python
>>> a = [1, 2, 3, 4]
>>> b = ['w', 'x', 'y', 'z']
>>> c = [0.2, 0.4, 0.6, 0.8]
>>> list(zip(a, b, c))
[(1, 'w', 0.2), (2, 'x', 0.4), (3, 'y', 0.6), (4, 'z', 0.8))]
>>>
```

Außerdem sollten Sie wissen, dass `zip()` sofort stoppt, wenn die kürzeste Eingabesequenz erschöpft ist.

```python
>>> a = [1, 2, 3, 4, 5, 6]
>>> b = ['x', 'y', 'z']
>>> list(zip(a,b))
[(1, 'x'), (2, 'y'), (3, 'z')]
>>>
```
