# Générer des données pour les graphiques en barres

Nous allons maintenant générer les données pour les graphiques en barres. Nous allons créer quatre ensembles de données, chacun avec 20 valeurs. Nous utiliserons la méthode `arange()` de NumPy pour créer un tableau de 20 valeurs et la méthode `random.rand()` de NumPy pour générer des valeurs aléatoires pour chaque ensemble de données.

```python
colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)
```
