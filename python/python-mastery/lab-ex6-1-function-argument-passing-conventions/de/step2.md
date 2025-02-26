# Vereinfachte Datenstrukturen

In früheren Übungen haben Sie eine Klasse definiert, die einen Aktienkurs wie folgt darstellt:

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Konzentrieren Sie sich auf die `__init__()`-Methode - ist das nicht eine Menge Code, den Sie jedes Mal tippen müssen, wenn Sie eine Struktur befüllen möchten? Was wäre, wenn Sie in Ihrem Programm dozens von solchen Strukturen definieren müssten?

In einer Datei `structure.py` definieren Sie eine Basisklasse `Structure`, die es dem Benutzer ermöglicht, einfache Datenstrukturen wie folgt zu definieren:

```python
class Stock(Structure):
    _fields = ('name','shares','price')

class Date(Structure):
    _fields = ('year','month', 'day')
```

Die `Structure`-Klasse sollte eine `__init__()`-Methode definieren, die beliebig viele Argumente annimmt und nach dem Vorhandensein einer `_fields`-Klassenvariable sucht. Lassen Sie die Methode die Instanz aus den Attributnamen in `_fields` und den an `__init__()` übergebenen Werten befüllen.

Hier ist ein Beispielcode, um Ihre Implementierung zu testen:

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s = Stock('AA',50)
Traceback (most recent call last):
...
TypeError: Expected 3 arguments
>>>
```
