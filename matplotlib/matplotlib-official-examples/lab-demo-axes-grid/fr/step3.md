# Créez une grille de 2x2 images avec chaque image ayant sa propre barre de couleur

Notre prochaine grille sera une grille de 2x2 images avec chaque image ayant sa propre barre de couleur. Nous utiliserons à nouveau la fonction `ImageGrid`, mais cette fois-ci nous définirons `cbar_mode` sur `"each"` pour spécifier que chaque image devrait avoir sa propre barre de couleur.

```python
# Créez une grille de 2x2 images avec chaque image ayant sa propre barre de couleur
grid = ImageGrid(
    fig,  # Objet Figure
    142,  # Emplacement du sous-graphique
    nrows_ncols=(2, 2),  # Nombre de lignes et de colonnes
    axes_pad=0.1,  # Espacement entre les axes
    label_mode="1",  # Mode d'étiquetage
    share_all=True,  # Partager la barre de couleur entre toutes les images
    cbar_location="top",  # Emplacement de la barre de couleur
    cbar_mode="each",  # Mode de la barre de couleur
    cbar_size="7%",  # Taille de la barre de couleur
    cbar_pad="2%"  # Espacement entre la barre de couleur et les images
)

# Tracez les images sur la grille et ajoutez les barres de couleur
for ax, cax in zip(grid, grid.cbar_axes):
    im = ax.imshow(Z, extent=extent)
    cax.colorbar(im)
    cax.tick_params(labeltop=False)
```
