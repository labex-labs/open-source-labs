# Übung 4.1: Objekte als Datenstrukturen

Im Abschnitt 2 und 3 haben wir mit Daten gearbeitet, die als Tupel und Wörterbücher repräsentiert wurden. Beispielsweise könnte ein Aktienbesitz als Tupel wie folgt repräsentiert werden:

```python
s = ('GOOG',100,490.10)
```

oder als Wörterbuch wie folgt:

```python
s = { 'name'   : 'GOOG',
    'shares' : 100,
     'price'  : 490.10
}
```

Sie können sogar Funktionen zum Manipulieren solcher Daten schreiben. Beispielsweise:

```python
def cost(s):
    return s['shares'] * s['price']
```

Allerdings kann es sein, dass Sie bei einem größeren Programm eine bessere Organisationsstruktur wünschen. Ein anderer Ansatz zur Datenrepräsentation wäre daher, eine Klasse zu definieren. Erstellen Sie eine Datei namens `stock.py` und definieren Sie eine Klasse `Stock`, die einen einzelnen Aktienbesitz repräsentiert. Lassen Sie die Instanzen von `Stock` die Attribute `name`, `shares` und `price` haben. Beispielsweise:

```python
>>> import stock
>>> a = stock.Stock('GOOG',100,490.10)
>>> a.name
'GOOG'
>>> a.shares
100
>>> a.price
490.1
>>>
```

Erstellen Sie einige weitere `Stock`-Objekte und manipulieren Sie sie. Beispielsweise:

```python
>>> b = stock.Stock('AAPL', 50, 122.34)
>>> c = stock.Stock('IBM', 75, 91.75)
>>> b.shares * b.price
6117.0
>>> c.shares * c.price
6881.25
>>> stocks = [a, b, c]
>>> stocks
[<stock.Stock object at 0x37d0b0>, <stock.Stock object at 0x37d110>, <stock.Stock object at 0x37d050>]
>>> for s in stocks:
     print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

... schauen Sie sich die Ausgabe an...
>>>
```

Eines, das hier betont werden muss, ist, dass die Klasse `Stock` wie eine Fabrik für das Erstellen von Objektinstanzen funktioniert. Im Grunde rufen Sie sie wie eine Funktion auf und sie erstellt ein neues Objekt für Sie. Auch muss betont werden, dass jedes Objekt unterschiedlich ist - jedes hat seine eigenen Daten, die von anderen erstellten Objekten getrennt sind.

Ein von einer Klasse definiertes Objekt ähnelt etwas einem Wörterbuch - nur mit etwas unterschiedlicher Syntax. Beispielsweise schreiben Sie statt `s['name']` oder `s['price']` jetzt `s.name` und `s.price`.
