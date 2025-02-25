# Personnaliser l'apparence du diagramme à violon

Maintenant, nous allons personnaliser l'apparence du diagramme à violon. Tout d'abord, nous allons limiter ce que Matplotlib dessine en définissant les arguments `showmeans`, `showmedians` et `showextrema` sur `False`. Ensuite, nous allons changer la couleur et l'opacité des corps des violons en utilisant les méthodes `set_facecolor` et `set_alpha`. Enfin, nous allons ajouter une représentation simplifiée d'un diagramme en boîte au-dessus du diagramme à violon, en utilisant la fonction `percentile` de NumPy pour calculer les quartiles, les médianes et les barres extrêmes.

```python
# customize violin plot appearance
fig, ax2 = plt.subplots()
ax2.set_title('Customized Violin Plot')
ax2.set_ylabel('Observed Values')

# create violin plot
parts = ax2.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)

# customize violin bodies
for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

# add box plot
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax2.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)
```
