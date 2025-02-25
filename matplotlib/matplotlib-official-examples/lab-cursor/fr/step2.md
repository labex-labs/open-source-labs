# Générer des données

Dans cette étape, nous générons des points de données aléatoires à l'aide de numpy.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data points
x, y = 4*(np.random.rand(2, 100) -.5)
```
