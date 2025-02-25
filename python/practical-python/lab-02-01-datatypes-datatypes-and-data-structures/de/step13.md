# Übung 2.3: Weitere Dictionary-Operationen

Wenn Sie ein Dictionary in eine Liste umwandeln, erhalten Sie alle seine Schlüssel:

```python
>>> list(d)
['name','shares', 'price', 'date', 'account']
>>>
```

Ähnlich können Sie die `for`-Anweisung verwenden, um über ein Dictionary zu iterieren, und erhalten Sie dann die Schlüssel:

```python
>>> for k in d:
        print('k =', k)

k = name
k = shares
k = price
k = date
k = account
>>>
```

Versuchen Sie diese Variante, die gleichzeitig eine Suche ausführt:

```python
>>> for k in d:
        print(k, '=', d[k])

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
account = 12345
>>>
```

Sie können auch alle Schlüssel mit der `keys()`-Methode erhalten:

```python
>>> keys = d.keys()
>>> keys
dict_keys(['name','shares', 'price', 'date', 'account'])
>>>
```

`keys()` ist etwas ungewöhnlich, da sie ein spezielles `dict_keys`-Objekt zurückgibt.

Dies ist eine Überlagerung des ursprünglichen Dictionaries, die Ihnen immer die aktuellen Schlüssel gibt - auch wenn das Dictionary sich ändert. Beispielsweise versuchen Sie dies:

```python
>>> del d['account']
>>> keys
dict_keys(['name','shares', 'price', 'date'])
>>>
```

Befinden Sie sich aufmerksam darauf, dass das `'account'` aus `keys` verschwunden ist, obwohl Sie `d.keys()` nicht erneut aufgerufen haben.

Eine elegantere Möglichkeit, um Schlüssel und Werte zusammen zu verwenden, ist die `items()`-Methode. Dies gibt Ihnen `(Schlüssel, Wert)`-Tupel:

```python
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> for k, v in d.items():
        print(k, '=', v)

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
>>>
```

Wenn Sie Tupel wie `items` haben, können Sie ein Dictionary mit der `dict()`-Funktion erstellen. Versuchen Sie es:

```python
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA','shares': 75, 'price':32.2, 'date': (6, 11, 2007)}
>>>
```
