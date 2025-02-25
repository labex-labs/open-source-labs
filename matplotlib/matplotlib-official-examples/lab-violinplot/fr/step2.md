# Création d'un ensemble de données d'échantillonnage

Nous allons créer un ensemble de données d'échantillonnage à l'aide de la bibliothèque numpy. Nous allons créer six ensembles de données avec des écarts-types différents.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake data
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]
```
