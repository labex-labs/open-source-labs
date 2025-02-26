# Übung 5.5: Vererbung

Erstellen Sie eine neue Klasse, die von `Stock` erbt.

```python
>>> class NewStock(Stock):
        def yow(self):
            print('Yow!')

>>> n = NewStock('ACME', 50, 123.45)
>>> n.cost()
6172.50
>>> n.yow()
Yow!
>>>
```

Die Vererbung wird durch Erweiterung des Suchprozesses für Attribute implementiert. Das `__bases__`-Attribut hat ein Tupel der unmittelbaren Elternklassen:

```python
>>> NewStock.__bases__
(<class'stock.Stock'>,)
>>>
```

Das `__mro__`-Attribut hat ein Tupel aller Elternklassen in der Reihenfolge, in der nach Attributen gesucht wird.

```python
>>> NewStock.__mro__
(<class '__main__.NewStock'>, <class'stock.Stock'>, <class 'object'>)
>>>
```

So würde die `cost()`-Methode der oben genannten Instanz `n` gefunden werden:

```python
>>> for cls in n.__class__.__mro__:
        if 'cost' in cls.__dict__:
            break

>>> cls
<class '__main__.Stock'>
>>> cls.__dict__['cost']
<function cost at 0x101aed598>
>>>
```
