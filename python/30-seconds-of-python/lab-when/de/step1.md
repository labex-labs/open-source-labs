# Wende Funktion an, wenn wahr

Schreiben Sie eine Funktion namens `when`, die zwei Argumente akzeptiert: eine Prädikatfunktion `predicate` und eine Funktion `when_true`, die angewendet werden soll. Die `when`-Funktion sollte eine neue Funktion zurückgeben, die ein einzelnes Argument `x` akzeptiert. Die neue Funktion sollte überprüfen, ob der Wert von `predicate(x)` `True` ist. Wenn ja, sollte die neue Funktion `when_true(x)` aufrufen und das Ergebnis zurückgeben. Andernfalls sollte die neue Funktion `x` zurückgeben.

```python
def when(predicate, when_true):
  return lambda x: when_true(x) if predicate(x) else x
```

```python
double_even_numbers = when(lambda x: x % 2 == 0, lambda x : x * 2)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```
