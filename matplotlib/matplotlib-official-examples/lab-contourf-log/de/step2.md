# Generieren des Datensatzes

Wir werden einen Datensatz mit positiven und negativen Werten mit `numpy` generieren:

```python
N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-2.0, 2.0, N)

X, Y = np.meshgrid(x, y)

# Ein niedriger Buckel mit einem Ausläufer.
# Braucht eine logarithmische Skala auf der z-/Farbenachse, damit wir sowohl den Buckel als auch den Ausläufer sehen.
# Eine lineare Skala zeigt nur den Ausläufer.
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
z = Z1 + 50 * Z2

# Setze einige negative Werte (untere linke Ecke) ein, um Probleme mit den Logarithmen zu verursachen:
z[:5, :5] = -1

# Folgender Teil ist nicht streng erforderlich, aber es wird eine Warnung eliminieren.
# Kommentiere es aus, um die Warnung zu sehen.
z = ma.masked_where(z <= 0, z)
```
