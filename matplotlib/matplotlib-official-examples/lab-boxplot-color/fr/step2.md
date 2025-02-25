# Création de données de test aléatoires

Ensuite, nous allons créer des données de test aléatoires à l'aide de la bibliothèque `numpy`. Nous allons générer 3 ensembles de données, chacun avec une écart-type différent.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']
```
