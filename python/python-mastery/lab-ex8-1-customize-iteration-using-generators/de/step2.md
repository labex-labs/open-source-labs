# Iteration hinzufügen zu Objekten

Wenn Sie eine benutzerdefinierte Klasse erstellt haben, können Sie es so gestalten, dass es die Iteration unterstützt, indem Sie eine spezielle Methode `__iter__()` definieren. `__iter__()` liefert als Ergebnis einen Iterator zurück. Wie im vorherigen Beispiel gezeigt, ist eine einfache Möglichkeit dazu, `__iter__()` als Generator zu definieren.

In früheren Übungen haben Sie eine Basisklasse `Structure` definiert. Fügen Sie dieser Klasse eine Methode `__iter__()` hinzu, die die Attributwerte in der Reihenfolge liefert. Beispielsweise:

```python
class Structure(metaclass=StructureMeta):
  ...
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
  ...
```

Wenn Sie dies getan haben, sollten Sie in der Lage sein, über die Instanzattribute wie folgt zu iterieren:

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> for val in s:
        print(val)
GOOG
100
490.1
>>>
```
