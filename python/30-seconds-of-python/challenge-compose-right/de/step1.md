# Umgekehrte Kompositionsfunktionen

## Problemstellung

Schreiben Sie eine Funktion `compose_right`, die eine oder mehrere Funktionen als Argumente nimmt und eine neue Funktion zurückgibt, die eine links-rechts-Funktionskomposition durchführt. Die erste (am linken Rand befindliche) Funktion kann ein oder mehrere Argumente akzeptieren; die verbleibenden Funktionen müssen einstellige sein.

Ihre Implementierung sollte die `reduce`-Funktion aus dem `functools`-Modul verwenden, um die links-rechts-Funktionskomposition durchzuführen.

```python
from functools import reduce

def compose_right(*fns):
  # Ihr Code hier
```

## Beispiel

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
assert add_and_square(1, 2) == 9
```

Im obigen Beispiel definieren wir zwei Funktionen `add` und `square`. Anschließend verwenden wir die `compose_right`-Funktion, um eine neue Funktion `add_and_square` zu erstellen, die zunächst zwei Zahlen addiert und dann das Ergebnis quadriert. Anschließend rufen wir die `add_and_square`-Funktion mit den Argumenten `1` und `2` auf, was `9` zurückgibt.
