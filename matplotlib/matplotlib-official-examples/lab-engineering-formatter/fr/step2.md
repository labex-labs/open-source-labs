# Création de données artificielles

Nous devons créer quelques données artificielles pour tracer. Dans ce laboratoire, nous tracerons le logarithme de la fréquence (en Hz) en fonction du logarithme de la puissance (en Watts). Nous utiliserons la bibliothèque `numpy` pour générer les données.

```python
# Fixing random state for reproducibility
prng = np.random.RandomState(19680801)

# Create artificial data to plot.
# The x data span over several decades to demonstrate several SI prefixes.
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2
```
