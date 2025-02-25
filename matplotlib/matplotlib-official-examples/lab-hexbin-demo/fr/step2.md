# Générer des données

Nous allons générer 100 000 points de données à l'aide de `numpy.random.standard_normal()` et `numpy.random.standard_normal()`. `standard_normal()` génère des nombres aléatoires à partir d'une distribution normale standard avec une moyenne de 0 et un écart-type de 1.

```python
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()
```
