# Mehrere Rückgabewerte

Funktionen können nur einen Wert zurückgeben. Ein Funktionsaufruf kann jedoch mehrere Werte in einem Tupel zurückgeben.

```python
def divide(a,b):
    q = a // b      # Quotient
    r = a % b       # Rest
    return q, r     # Gebe ein Tupel zurück
```

Verwendungsbeispiel:

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```
