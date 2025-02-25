# Créer le graphique à barres hexagonales

Nous allons créer le graphique à barres hexagonales à l'aide de `matplotlib.pyplot.hexbin()`.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Hexagon binning")

cb = fig.colorbar(hb, ax=ax, label='counts')
```

Ici, nous définissons la taille de la grille sur 50 et la carte de couleurs sur 'inferno'. Nous ajoutons également une barre de couleur pour montrer le nombre de points de données dans chaque hexagone.
