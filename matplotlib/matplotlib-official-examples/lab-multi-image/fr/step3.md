# Définir l'échelle de couleur et créer une barre de couleur

Maintenant, nous allons définir l'échelle de couleur pour nos images et créer une barre de couleur pour montrer la plage de valeurs. Nous allons trouver les valeurs minimales et maximales pour toutes les images et normaliser l'échelle de couleur en conséquence.

```python
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axs, orientation='horizontal', fraction=.1)
```
