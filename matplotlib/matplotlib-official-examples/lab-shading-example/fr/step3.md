# Créer des graphiques de relief ombré

Nous allons maintenant créer les graphiques de relief ombré à l'aide de la classe `LightSource`. Nous allons créer deux sous-graphiques, l'un avec des données colorées et l'autre avec l'intensité d'éclairage.

```python
# Éclairer la scène du nord-ouest
ls = LightSource(azdeg=315, altdeg=45)

fig, axs = plt.subplots(ncols=2, nrows=2)
for ax in axs.flat:
    ax.set(xticks=[], yticks=[])

axs[0, 0].imshow(z, cmap=cmap)
axs[0, 0].set(xlabel='Données colorées')

axs[0, 1].imshow(ls.hillshade(z, vert_exag=ve), cmap='gray')
axs[0, 1].set(xlabel='Intensité d\'éclairage')
```

Nous allons créer deux autres sous-graphiques, l'un avec le `blend_mode` défini sur "hsv" et l'autre défini sur "overlay".

```python
rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='hsv')
axs[1, 0].imshow(rgb)
axs[1, 0].set(xlabel='Mode de mélange : "hsv" (par défaut)')

rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='overlay')
axs[1, 1].imshow(rgb)
axs[1, 1].set(xlabel='Mode de mélange : "overlay"')
```
