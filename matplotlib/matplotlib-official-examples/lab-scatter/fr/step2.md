# Générez des données aléatoires

Dans cette étape, nous allons générer des données aléatoires pour notre graphique en nuage de points. Nous allons générer 50 points de données pour chaque variable à l'aide de la bibliothèque NumPy.

```python
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
```
