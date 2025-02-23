# Générez des données aléatoires

Nous allons générer un tableau 3D de données aléatoires à l'aide de `numpy.random.random()`. Nous utiliserons une valeur de graine pour vous assurer que le même ensemble de données est généré chaque fois que le code est exécuté.

```python
np.random.seed(19680801)
data = np.random.random((50, 50, 50))
```
