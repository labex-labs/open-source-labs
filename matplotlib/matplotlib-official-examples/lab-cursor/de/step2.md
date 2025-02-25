# Daten generieren

In diesem Schritt generieren wir zufällige Datenpunkte mit numpy.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data points
x, y = 4*(np.random.rand(2, 100) -.5)
```
