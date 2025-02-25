# Daten generieren

In diesem Schritt werden wir die Daten für das Liniendiagramm generieren. Wir werden die NumPy-Funktion `arange()` verwenden, um ein Array von Werten für die x-Achse zu generieren, und die `sin()`-Funktion, um ein Array von y-Achsenwerten für eine Sinuswelle zu generieren.

```python
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
```
