# Créez une grille de 2x2 images avec une seule barre de couleur

Notre première grille sera une grille de 2x2 images avec une seule barre de couleur. Nous utiliserons la fonction `ImageGrid` pour créer la grille et spécifier le nombre de lignes et de colonnes que nous souhaitons. Nous spécifierons également l'emplacement de la barre de couleur et définirons `share_all` sur `True` pour partager la barre de couleur entre toutes les images.

```python
# Créez une grille de 2x2 images avec une seule barre de couleur
grid = ImageGrid(
    fig,  # Objet Figure
    141,  # Emplacement du sous-graphique
    nrows_ncols=(2, 2),  # Nombre de lignes et de colonnes
    axes_pad=0.0,  # Espacement entre les axes
    label_mode="L",  # Mode d'étiquetage
    share_all=True,  # Partager la barre de couleur entre toutes les images
    cbar_location="top",  # Emplacement de la barre de couleur
    cbar_mode="single"  # Mode de la barre de couleur
)

# Tracez les images sur la grille
for ax in grid:
    im = ax.imshow(Z, extent=extent)

# Ajoutez une barre de couleur à la grille
grid.cbar_axes[0].colorbar(im)
for cax in grid.cbar_axes:
    cax.tick_params(labeltop=False)
```
