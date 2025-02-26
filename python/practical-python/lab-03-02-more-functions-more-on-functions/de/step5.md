# Rückgabe von Werten

Die `return`-Anweisung gibt einen Wert zurück

```python
def square(x):
    return x * x
```

Wenn kein Rückgabewert angegeben wird oder `return` fehlt, wird `None` zurückgegeben.

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# ODER
def foo(x):
    statements  # Keine `return`

b = foo(4)      # b = None
```
