# Mathematische Operatoren

Wenn du für ein Objekt die passenden Methoden implementierst, kannst du es mit verschiedenen mathematischen Operatoren verwenden. Allerdings ist es deine Verantwortung, andere Datentypen zu erkennen und den passenden Konversionscode zu implementieren. Ändere die `MutInt`-Klasse, indem du ihr eine `__add__()`-Methode wie folgt gibst:

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented
```

Mit dieser Änderung solltest du feststellen, dass du sowohl Ganzzahlen als auch veränderbare Ganzzahlen addieren kannst. Das Ergebnis ist eine `MutInt`-Instanz. Andere Arten von Zahlen zu addieren führt zu einem Fehler:

```python
>>> a = MutInt(3)
>>> b = a + 10
>>> b
MutInt(13)
>>> b.value = 23
>>> c = a + b
>>> c
MutInt(26)
>>> a + 3.5
Fehler (letzte Aufrufzeile):
  Datei "<stdin>", Zeile 1, in <modul>
TypeError: nicht unterstützte Operandentypen für +: 'MutInt' und 'float'
>>>
```

Ein Problem mit dem Code ist, dass es nicht funktioniert, wenn die Reihenfolge der Operanden umgedreht wird. Betrachte:

```python
>>> a + 10
MutInt(13)
>>> 10 + a
Fehler (letzte Aufrufzeile):
  Datei "<stdin>", Zeile 1, in <modul>
TypeError: nicht unterstützte Operandentypen für +: 'int' und 'MutInt'
>>>
```

Dies geschieht, weil der `int`-Typ keine Kenntnis von `MutInt` hat und verwirrt ist. Dies kann behoben werden, indem du eine `__radd__()`-Methode hinzufügst. Diese Methode wird aufgerufen, wenn der erste Versuch, `__add__()` aufzurufen, mit dem bereitgestellten Objekt nicht funktioniert hat.

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    __radd__ = __add__    # Umgekehrte Operanden
```

Mit dieser Änderung wirst du feststellen, dass die Addition funktioniert:

```python
>>> a = MutInt(3)
>>> a + 10
MutInt(13)
>>> 10 + a
MutInt(13)
>>>
```

Da unsere Ganzzahl veränderbar ist, kannst du auch die in-place-Additions-Update-Operator `+=` erkennen, indem du die `__iadd__()`-Methode implementierst:

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

Dies ermöglicht interessante Anwendungen wie diese:

```python
>>> a = MutInt(3)
>>> b = a
>>> a += 10
>>> a
MutInt(13)
>>> b                 # Beachte, dass b auch geändert wird
MutInt(13)
>>>
```

Es mag ein bisschen merkwürdig erscheinen, dass `b` auch geändert wird, aber es gibt subtile Eigenschaften wie diese bei eingebauten Python-Objekten. Beispielsweise:

```python
>>> a = [1,2,3]
>>> b = a
>>> a += [4,5]
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]

>>> c = (1,2,3)
>>> d = c
>>> c += (4,5)
>>> c
(1, 2, 3, 4, 5)
>>> d                  # Erkläre den Unterschied zu Listen
(1, 2, 3)
>>>
```
