# Generieren von Zufallsdaten

Wir werden zwei Sets von Zufallsdaten mit NumPy generieren. Diese Daten werden geplottet, um einen Streudiagramm zu erstellen.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 200)
```
