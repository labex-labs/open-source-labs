# Génération de données pour le graphique en nuage de points

Ensuite, nous générons des données pour le graphique en nuage de points. Nous créons 100 points de données avec des valeurs aléatoires de x et y entre 0 et 0,9, et des rayons aléatoires entre 0 et 10. La couleur de chaque point de données est déterminée par la racine carrée de sa surface.

```python
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2  # 0 à 10 rayons des points
c = np.sqrt(area)
```
