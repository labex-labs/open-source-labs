# Daten erstellen

Als nächstes werden wir einige Beispiel-Daten erstellen, um sie zu plotten. In diesem Beispiel werden wir ein 2D-Gitter von x- und y-Werten erstellen und diese verwenden, um die z-Werte zu berechnen.

```python
# invent some numbers, turning the x and y arrays into simple
# 2d arrays, which make combining them together easier.
x = np.linspace(-3, 5, 150).reshape(1, -1)
y = np.linspace(-3, 5, 120).reshape(-1, 1)
z = np.cos(x) + np.sin(y)
```
