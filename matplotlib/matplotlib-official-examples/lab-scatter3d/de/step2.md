# Daten vorbereiten

Wir werden mit der NumPy-Bibliothek zwei Datensätze mit zufälligen Werten generieren. Ein Datensatz wird die x- und y-Koordinaten repräsentieren, und der andere Datensatz wird die z-Koordinate repräsentieren.

```python
def randrange(n, vmin, vmax):
    """
    Hilfsfunktion, um ein Array von Zufallszahlen mit der Form (n, ) zu erstellen,
    wobei jede Zahl gleichmäßig im Intervall (vmin, vmax) verteilt ist.
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

n = 100

for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
```
