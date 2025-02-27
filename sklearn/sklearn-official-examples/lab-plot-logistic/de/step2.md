# Erzeugen eines einfachen Datensatzes

Als nächster Schritt erzeugen wir einen einfachen Datensatz, der eine Gerade mit etwas Gauß'scher Störung ist. Wir werden `numpy` verwenden, um diesen Datensatz zu erzeugen.

```python
# Generate a toy dataset, it's just a straight line with some Gaussian noise:
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(float)
X[X > 0] *= 4
X += 0.3 * np.random.normal(size=n_samples)

X = X[:, np.newaxis]
```
