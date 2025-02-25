# Daten erstellen

Wir müssen die Daten erstellen, die wir zum Erstellen des Konturplots verwenden werden. In diesem Beispiel werden wir zwei 2D-Gaußfunktionen erstellen.

```python
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
