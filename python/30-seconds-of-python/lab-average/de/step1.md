# Durchschnitt

Schreiben Sie eine Funktion namens `average`, die zwei oder mehr Zahlen entgegennimmt und deren Durchschnitt zurückgibt. Ihre Funktion sollte den folgenden Richtlinien folgen:

- Verwenden Sie `sum()`, um alle bereitgestellten `args` zu summieren, und dividieren Sie durch `len()`.
- Die Funktion sollte beliebig viele Argumente verarbeiten können.
- Die Funktion sollte einen Float zurückgeben.

```python
def average(*args):
  return sum(args, 0.0) / len(args)
```

```python
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```
