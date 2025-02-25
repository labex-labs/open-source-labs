# Daten erstellen

Wir werden einen numpy-Array `x` erstellen, der 500 gleichmäßig verteilte Werte zwischen 0 und 3π enthält. Wir werden auch einen weiteren numpy-Array `y` erstellen, der die Sinuswerte der Werte in `x` enthält. Schließlich werden wir einen numpy-Array `dydx` erstellen, der die erste Ableitung von `y` enthält.

```python
x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))
```
