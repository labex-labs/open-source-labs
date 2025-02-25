# Ein diagonale Linie zeichnen

Zunächst werden wir eine diagonale Linie im 45-Grad-Winkel mit der `plot()`-Funktion von Matplotlib zeichnen.

```python
fig, ax = plt.subplots()

# Zeichne diagonale Linie (45 Grad)
h = ax.plot(range(0, 10), range(0, 10))
```
