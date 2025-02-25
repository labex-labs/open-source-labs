# Generieren von Zufallsdaten

Wir generieren Zufallsdaten mit der `np.random.uniform`-Methode von NumPy. Wir generieren `npts = 200` Datenpunkte mit x- und y-Werten zwischen -2 und 2. Wir berechnen auch die z-Werte mit der Funktion `z = x * np.exp(-x**2 - y**2)`.

```python
np.random.seed(19680801)
npts = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x * np.exp(-x**2 - y**2)
```
