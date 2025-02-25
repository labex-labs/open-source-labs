# Démo 1 - Barre de couleur sur chaque axe

Nous allons créer une grille de 3 images avec une barre de couleur sur chaque axe en utilisant le code suivant :

```python
grid = ImageGrid(
    fig, 211, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="top", cbar_mode="each", cbar_size="7%", cbar_pad="1%")
grid[0].set(xticks=[-2, 0], yticks=[-2, 0, 2])

for i, (ax, z) in enumerate(zip(grid, ZS)):
    im = ax.imshow(z, origin="lower", extent=extent)
    cb = ax.cax.colorbar(im)
    # Changing the colorbar ticks
    if i in [1, 2]:
        cb.set_ticks([-1, 0, 1])

for ax, im_title in zip(grid, ["Image 1", "Image 2", "Image 3"]):
    add_inner_title(ax, im_title, loc='lower left')
```

- Nous créons une grille de 3 images en utilisant `ImageGrid`.
- Nous définissons le `cbar_mode` sur "each" pour ajouter une barre de couleur sur chaque axe.
- Nous définissons le paramètre `share_all` sur True pour partager les axes x et y entre toutes les images.
- Nous définissons le paramètre `cbar_location` sur "top" pour positionner les barres de couleur en haut.
- Nous définissons les `xticks` et les `yticks` pour la première image.
- Nous parcourons chaque image et ajoutons l'image à l'axe en utilisant `imshow`.
- Nous ajoutons une barre de couleur à chaque axe en utilisant `ax.cax.colorbar`.
- Nous définissons les repères de la barre de couleur pour la deuxième et la troisième images.
- Nous ajoutons un titre à chaque image en utilisant `add_inner_title`.
