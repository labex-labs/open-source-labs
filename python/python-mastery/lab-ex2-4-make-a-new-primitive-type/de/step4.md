# Vergleiche

Ein Problem ist, dass die Vergleiche immer noch nicht funktionieren. Beispielsweise:

```python
>>> a = MutInt(3)
>>> b = MutInt(3)
>>> a == b
False
>>> a == 3
False
>>>
```

Du kannst dies beheben, indem du eine `__eq__()`-Methode hinzufügst. Weitere Methoden wie `__lt__()`, `__le__()`, `__gt__()`, `__ge__()` können verwendet werden, um andere Vergleiche zu implementieren. Beispielsweise:

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
```

Teste es:

```python
>>> a = MutInt(3)
>>> b = MutInt(3)
>>> a == b
True
>>> c = MutInt(4)
>>> a < c
True
>>> a <= c
Fehler (letzte Aufrufzeile):
  Datei "<stdin>", Zeile 1, in <modul>
TypeError: '<=' wird zwischen Instanzen von 'MutInt' und 'MutInt' nicht unterstützt
>>>
```

Der Grund, warum der `<=`-Operator fehlschlägt, ist, dass keine `__le__()`-Methode bereitgestellt wurde. Du könntest es separat programmieren, aber eine einfachere Möglichkeit, es zu erhalten, ist, den `@total_ordering`-Decorator zu verwenden:

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
```

`@total_ordering` füllt die fehlenden Vergleichsmethoden für dich aus, solange du mindestens einen Gleichheitsoperator und eine der anderen Relationen angeben.
