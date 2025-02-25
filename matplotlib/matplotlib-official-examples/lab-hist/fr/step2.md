# Mise à jour des couleurs de l'histogramme

La méthode `histogram` renvoie (entre autres choses) un objet `patches`. Cela nous donne accès aux propriétés des objets tracés. En utilisant cela, nous pouvons éditer l'histogramme selon nos goûts. Modifions la couleur de chaque barre en fonction de sa valeur y.

```python
# N est le comptage dans chaque boîte, bins est la limite inférieure de la boîte
N, bins, patches = axs[0].hist(dist1, bins=n_bins)

# Nous allons coder les couleurs en fonction de la hauteur, mais vous pouvez utiliser n'importe quel scalaire
fracs = N / N.max()

# nous devons normaliser les données de 0..1 pour toute la plage de la carte de couleurs
norm = colors.Normalize(fracs.min(), fracs.max())

# Maintenant, nous allons parcourir nos objets et définir la couleur de chacun en conséquence
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# Nous pouvons également normaliser nos entrées par le nombre total de comptages
axs[1].hist(dist1, bins=n_bins, density=True)

# Maintenant, nous formattons l'axe y pour afficher le pourcentage
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()
```
