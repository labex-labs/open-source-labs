# Démo 2 - Barre de couleur partagée

Nous allons créer une grille de 3 images avec une barre de couleur partagée en utilisant le code suivant :

```python
grid2 = ImageGrid(
    fig, 212, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="right", cbar_mode="single", cbar_size="10%", cbar_pad=0.05)
grid2[0].set(xlabel="X", ylabel="Y", xticks=[-2, 0], yticks=[-2, 0, 2])

clim = (np.min(ZS), np.max(ZS))
for ax, z in zip(grid2, ZS):
    im = ax.imshow(z, clim=clim, origin="lower", extent=extent)

# With cbar_mode="single", cax attribute of all axes are identical.
ax.cax.colorbar(im)

for ax, im_title in zip(grid2, ["(a)", "(b)", "(c)"]):
    add_inner_title(ax, im_title, loc='upper left')
```

- Nous créons une grille de 3 images en utilisant `ImageGrid`.
- Nous définissons le `cbar_mode` sur "single" pour ajouter une barre de couleur partagée.
- Nous définissons le paramètre `share_all` sur True pour partager les axes x et y entre toutes les images.
- Nous définissons le paramètre `cbar_location` sur "right" pour positionner la barre de couleur à droite.
- Nous définissons les `xticks` et les `yticks` pour la première image.
- Nous parcourons chaque image et ajoutons l'image à l'axe en utilisant `imshow`.
- Nous définissons le paramètre `clim` pour vous assurer que toutes les images utilisent la même échelle de couleur.
- Nous ajoutons une barre de couleur partagée à l'axe en utilisant `ax.cax.colorbar`.
- Nous ajoutons un titre à chaque image en utilisant `add_inner_title`.
