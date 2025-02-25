# Zahl ist Primzahl

## Problem

Schreiben Sie eine Python-Funktion namens `is_prime(n)`, die eine ganze Zahl `n` als Eingabe nimmt und `True` zurückgibt, wenn die Zahl eine Primzahl ist, und `False` sonst. Um dieses Problem zu lösen, müssen Sie die folgenden Regeln befolgen:

- Geben Sie `False` zurück, wenn die Zahl `0`, `1`, eine negative Zahl oder ein Vielfaches von `2` ist.
- Verwenden Sie `all()` und `range()` zum Überprüfen von Zahlen von `3` bis zur Quadratwurzel der gegebenen Zahl.
- Geben Sie `True` zurück, wenn keine Zahl die gegebene Zahl teilt, `False` sonst.

## Beispiel

```python
is_prime(11) # True
```
