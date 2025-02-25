# Créez une image avec un zoom d'incrustation et une incrustation marquée

Dans le second sous-graphique, nous allons créer une image avec un zoom d'incrustation et une incrustation marquée. Cela montrera comment utiliser la méthode `.mark_inset` pour marquer la région d'intérêt et la connecter aux axes de l'incrustation.

```python
# Chargez les données d'échantillonnage pour l'image
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # Tableau 15x15
extent = (-3, 4, -4, 3)
Z2 = np.zeros((150, 150))
ny, nx = Z.shape
Z2[30:30+ny, 30:30+nx] = Z

# Affichez l'image dans le sous-graphique
ax2.imshow(Z2, extent=extent, origin="lower")

# Créez une incrustation zoomée dans le coin supérieur gauche du graphique
axins2 = zoomed_inset_axes(ax2, zoom=6, loc=1)

# Affichez l'image dans le graphique incrusté
axins2.imshow(Z2, extent=extent, origin="lower")

# Fixez les limites x et y du graphique incrusté pour afficher la région d'intérêt
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
axins2.set_xlim(x1, x2)
axins2.set_ylim(y1, y2)

# Fixez le nombre d'étiquettes de graduation sur les axes de l'incrustation
axins2.yaxis.get_major_locator().set_params(nbins=7)
axins2.xaxis.get_major_locator().set_params(nbins=7)

# Cachez les étiquettes de graduation sur les axes de l'incrustation
axins2.tick_params(labelleft=False, labelbottom=False)

# Marquez la région d'intérêt et la connectez aux axes de l'incrustation
mark_inset(ax2, axins2, loc1=2, loc2=4, fc="none", ec="0.5")
```
