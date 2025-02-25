# Génération des données aléatoires

Nous allons générer deux ensembles de données aléatoires à l'aide de NumPy. Ces données seront tracées pour créer un nuage de points.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 200)
```
