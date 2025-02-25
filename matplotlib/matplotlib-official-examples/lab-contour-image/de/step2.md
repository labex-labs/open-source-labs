# Die Daten definieren

In diesem Schritt definierst du die Daten, die geplottet werden sollen. Die Daten sind ein zweidimensionales Array von Werten, das die Fläche repräsentiert.

```python
# Default delta ist groß, weil das die Geschwindigkeit erhöht und die
# richtige Registrierung zwischen Bild und Konturen veranschaulicht.
delta = 0.5

extent = (-3, 4, -4, 3)

x = np.arange(-3.0, 4.001, delta)
y = np.arange(-4.0, 3.001, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
