# Générez des données aléatoires

Nous allons générer des données aléatoires pour le graphique en points dispersés à l'aide de NumPy. Nous allons créer 150 points de données avec des valeurs aléatoires de rayon et d'angle, et calculer l'aire et la couleur de chaque point.

```python
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
```
