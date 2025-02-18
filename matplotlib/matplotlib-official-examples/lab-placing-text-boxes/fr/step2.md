# Création de données

Pour cet exemple, nous allons créer un ensemble de données aléatoires en utilisant `numpy.random.randn()`.

```python
np.random.seed(19680801)
x = 30*np.random.randn(10000)
mu = x.mean()
median = np.median(x)
sigma = x.std()
```
