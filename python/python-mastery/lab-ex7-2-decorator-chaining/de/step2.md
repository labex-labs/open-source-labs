# Dein erster Dekorator mit Argumenten

Der `@logged`-Dekorator, den du zuvor definiert hast, gibt immer nur eine einfache Nachricht mit dem Funktionsnamen aus. Angenommen, du wolltest, dass der Benutzer eine benutzerdefinierte Nachricht angeben kann.

Definiere einen neuen Dekorator `@logformat(fmt)`, der einen Formatstring als Argument akzeptiert und `fmt.format(func=func)` verwendet, um eine bereitgestellte Funktion in eine Log-Nachricht zu formatieren:

```python
# sample.py
...
from logcall import logformat

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x,y):
    return x*y
```

Dazu musst du einen Dekorator definieren, der ein Argument annimmt. So sollte es aussehen, wenn du es testest:

```python
>>> import sample
Adding logging to add
Adding logging to sub
Adding logging to mul
>>> sample.add(2,3)
Calling add
5
>>> sample.mul(2,3)
sample.py:mul
6
>>>
```

Um den Code weiter zu vereinfachen, zeige, wie du den ursprünglichen `@logged`-Dekorator mithilfe des `@logformat`-Dekorators definieren kannst.
