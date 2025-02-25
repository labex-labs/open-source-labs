# Erstellen des Kreises

Wir werden den Kreis mit der `make_circle()`-Funktion erstellen. Die Funktion nimmt den Radius des Kreises als Eingabe und gibt die x- und y-Koordinaten des Kreises zurück.

```python
def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
```
