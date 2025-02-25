# Utiliser une carte de couleurs pour spécifier les couleurs des courbes de niveau

Nous pouvons utiliser une carte de couleurs pour spécifier les couleurs des lignes de courbes de niveau.

```python
fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', origin='lower',
               cmap=cm.gray, extent=(-3, 3, -2, 2))
levels = np.arange(-1.2, 1.6, 0.2)
CS = ax.contour(Z, levels, origin='lower', cmap='flag', extend='both',
                linewidths=2, extent=(-3, 3, -2, 2))

# Épaissez la courbe de niveau zéro.
CS.collections[6].set_linewidth(4)

ax.clabel(CS, levels[1::2],  # étiquetez chaque seconde ligne de niveau
          inline=True, fmt='%1.1f', fontsize=14)

# Créez une barre de couleur pour les lignes de courbes de niveau
CB = fig.colorbar(CS, shrink=0.8)

ax.set_title('Lignes avec barre de couleur')

# Nous pouvons toujours ajouter une barre de couleur pour l'image également.
CBI = fig.colorbar(im, orientation='horizontal', shrink=0.8)

# Cela rend la barre de couleur d'origine un peu décalée,
# donc améliorons sa position.

l, b, w, h = ax.get_position().bounds
ll, bb, ww, hh = CB.ax.get_position().bounds
CB.ax.set_position([ll, b + 0.1*h, ww, h*0.8])
```
