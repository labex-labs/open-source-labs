# Generieren von Zufallsdaten

Wir werden mit NumPy Zufallsdaten für das Streudiagramm generieren. Wir werden 150 Datenpunkte mit zufälligen Radius- und Winkelwerten erstellen und die Fläche und Farbe jedes Punktes berechnen.

```python
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
```
