# Créer le tracé

Nous créons une grille de tracé 4x3 pour afficher les tracés ombragés de collines avec différents modes de mélange et exagération verticale. Nous montrons d'abord l'image d'intensité d'ombrage de colline dans la première ligne, puis nous plaçons des tracés ombragés de collines avec différents modes de mélange dans les autres lignes. Nous utilisons une boucle `for` pour itérer à travers les différentes valeurs d'exagération verticale et les modes de mélange.

```python
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(8, 9))
plt.setp(axs.flat, xticks=[], yticks=[])

for col, ve in zip(axs.T, [0.1, 1, 10]):
    col[0].imshow(ls.hillshade(z, vert_exag=ve, dx=dx, dy=dy), cmap='gray')
    for ax, mode in zip(col[1:], ['hsv', 'overlay','soft']):
        rgb = ls.shade(z, cmap=cmap, blend_mode=mode,
                       vert_exag=ve, dx=dx, dy=dy)
        ax.imshow(rgb)
```
