# Créer un graphique en barres groupées

Maintenant, nous pouvons créer notre graphique en utilisant la fonction `bar` de Matplotlib. Nous allons créer une boucle qui parcourt nos attributs et crée un ensemble de barres pour chacun d'entre eux. Nous allons également ajuster la largeur des barres et la position de chaque ensemble de barres.

```python
x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1
```
