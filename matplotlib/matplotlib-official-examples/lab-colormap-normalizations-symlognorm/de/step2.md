# Erstellen von synthetischen Daten

In diesem Schritt erstellen wir einen synthetischen Datensatz, der aus zwei Buckeln besteht, einem negativen und einem positiven, wobei der positive Buckel eine Amplitude von achtmal der Amplitude des negativen Buckels hat. Anschließend wenden wir `SymLogNorm` an, um die Daten zu visualisieren.

```python
def rbf(x, y):
    return 1.0 / (1 + 5 * ((x ** 2) + (y ** 2)))

N = 200
gain = 8
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z1 = rbf(X + 0.5, Y + 0.5)
Z2 = rbf(X - 0.5, Y - 0.5)
Z = gain * Z1 - Z2

shadeopts = {'cmap': 'PRGn','shading': 'gouraud'}
colormap = 'PRGn'
lnrwidth = 0.5
```
