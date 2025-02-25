# Création de données

Ensuite, nous allons créer des données aléatoires à utiliser dans notre visualisation. Dans cet exemple, nous allons créer deux tableaux de données aléatoires à l'aide de numpy.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.rand(20)
y = 1e7 * np.random.rand(20)
```
