# Créez une incrustation zoomée avec une échelle de taille

Dans le premier sous-graphique, nous allons créer une incrustation zoomée avec une échelle de taille. Cela montrera comment utiliser la méthode `.zoomed_inset_axes` pour créer une incrustation zoomée.

```python
# Fixez le rapport d'aspect du graphique à 1
ax.set_aspect(1)

# Créez une incrustation zoomée dans le coin supérieur droit du graphique
axins = zoomed_inset_axes(ax, zoom=0.5, loc='upper right')

# Fixez le nombre d'étiquettes de graduation sur les axes de l'incrustation
axins.yaxis.get_major_locator().set_params(nbins=7)
axins.xaxis.get_major_locator().set_params(nbins=7)

# Cachez les étiquettes de graduation sur les axes de l'incrustation
axins.tick_params(labelleft=False, labelbottom=False)

# Définissez une fonction pour ajouter une échelle de taille au graphique
def add_sizebar(ax, size):
    asb = AnchoredSizeBar(ax.transData,
                          size,
                          str(size),
                          loc=8,
                          pad=0.1, borderpad=0.5, sep=5,
                          frameon=False)
    ax.add_artist(asb)

# Ajoutez une échelle de taille au graphique principal et au graphique incrusté
add_sizebar(ax, 0.5)
add_sizebar(axins, 0.5)
```
