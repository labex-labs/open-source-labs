# Créez une grille de 2x2 images avec chaque image ayant sa propre barre de couleur et une plage de couleur différente

Notre dernière grille sera également une grille de 2x2 images avec chaque image ayant sa propre barre de couleur, mais cette fois-ci nous utiliserons une plage de couleur différente pour chaque image. Nous définirons la plage de la barre de couleur en utilisant `vmin` et `vmax` lors du tracé de chaque image.

```python
# Créez une grille de 2x2 images avec chaque image ayant sa propre barre de couleur et une plage de couleur différente
grid = ImageGrid(
    fig,  # Objet Figure
    143,  # Emplacement du sous-graphique
    nrows_ncols=(2, 2),  # Nombre de lignes et de colonnes
    axes_pad=(0.45, 0.15),  # Espacement entre les axes
    label_mode="1",  # Mode d'étiquetage
    share_all=True,  # Partager la barre de couleur entre toutes les images
    cbar_location="right",  # Emplacement de la barre de couleur
    cbar_mode="each",  # Mode de la barre de couleur
    cbar_size="7%",  # Taille de la barre de couleur
    cbar_pad="2%"  # Espacement entre la barre de couleur et les images
)

# Tracez les images sur la grille et ajoutez les barres de couleur
limits = ((0, 1), (-2, 2), (-1.7, 1.4), (-1.5, 1))  # Plages de barres de couleur différentes
for ax, cax, vlim in zip(grid, grid.cbar_axes, limits):
    im = ax.imshow(Z, extent=extent, vmin=vlim[0], vmax=vlim[1])
    cb = cax.colorbar(im)
    cb.set_ticks((vlim[0], vlim[1]))
```
