# Fixez la graine aléatoire et générez les données

Dans cette étape, nous allons fixer la graine aléatoire et générer les données. Nous allons générer 100 points de données à partir d'une distribution normale avec une moyenne de 200 et un écart-type de 25.

```python
np.random.seed(19680801)
mu = 200
sigma = 25
data = np.random.normal(mu, sigma, size=100)
```
