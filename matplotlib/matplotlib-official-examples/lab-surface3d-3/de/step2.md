# Daten für den Oberflächenplot erstellen

In diesem Schritt werden wir Daten für den Oberflächenplot erstellen. Wir werden ein Gitternetz von X- und Y-Werten erstellen, die radiale Entfernung R berechnen und den Z-Wert basierend auf dem R-Wert mit `np.sin()` berechnen.

```python
# Create data for the surface plot
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
