# Wende Funktion an, wenn wahr

## Problem

Schreiben Sie eine Funktion namens `when`, die zwei Argumente akzeptiert: eine Prädikatfunktion `predicate` und eine Funktion, die angewendet werden soll, wenn das Prädikat wahr ist (`when_true`). Die `when`-Funktion sollte eine neue Funktion zurückgeben, die ein einzelnes Argument `x` akzeptiert. Die neue Funktion sollte überprüfen, ob der Wert von `predicate(x)` `True` ist. Wenn ja, sollte die neue Funktion `when_true(x)` aufrufen und das Ergebnis zurückgeben. Andernfalls sollte die neue Funktion `x` zurückgeben.

## Beispiel

```python
def double(x):
    return x * 2

def is_even(x):
    return x % 2 == 0

double_even_numbers = when(is_even, double)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```
