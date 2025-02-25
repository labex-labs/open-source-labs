# Daten erstellen

Als nächstes müssen wir die Daten erstellen, die wir verwenden werden, um die Linien zu zeichnen. Wir werden `numpy` verwenden, um ein 2D-Array von `x`- und `y`-Werten zu erstellen.

```python
x = np.arange(100)
ys = x[:50, np.newaxis] + x[np.newaxis, :]
```
