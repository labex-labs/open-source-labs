# Créer un graphique en barres empilées

Nous allons créer un graphique en barres empilées à l'aide de `matplotlib.pyplot.bar` et parcourir chaque catégorie de poids pour empiler les barres.

```python
fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")
```
