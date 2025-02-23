# Fiktive Daten erstellen

Im zweiten Schritt werden wir fiktive Daten erstellen, die wir für das Diagramm verwenden.

```python
# fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1
```
