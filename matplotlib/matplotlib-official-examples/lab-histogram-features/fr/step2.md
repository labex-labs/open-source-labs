# Générez des données d'échantillonnage

Dans cette étape, nous allons générer des données d'échantillonnage à l'aide de numpy. Nous allons générer des données aléatoires à partir d'une distribution normale avec une moyenne de 100 et un écart-type de 15.

```python
np.random.seed(19680801)
mu = 100  # moyenne de la distribution
sigma = 15  # écart-type de la distribution
x = mu + sigma * np.random.randn(437)
```
