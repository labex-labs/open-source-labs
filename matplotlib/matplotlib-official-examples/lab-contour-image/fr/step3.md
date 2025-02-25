# Créer l'image de contour

Dans cette étape, vous allez créer l'image de contour en utilisant les fonctions contour et contourf de Matplotlib.

```python
# Augmentez la limite supérieure pour éviter les erreurs de troncature.
levels = np.arange(-2.0, 1.601, 0.4)

norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
cmap = cm.PRGn

fig, _axs = plt.subplots(nrows=2, ncols=2)
fig.subplots_adjust(hspace=0.3)
axs = _axs.flatten()

cset1 = axs[0].contourf(X, Y, Z, levels, norm=norm,
                        cmap=cmap.resampled(len(levels) - 1))
# Ce n'est pas nécessaire, mais pour la carte de couleur, nous avons seulement besoin
# du nombre de niveaux moins 1. Pour éviter l'erreur de discrétisation, utilisez
# soit ce nombre soit un nombre élevé tel que la valeur par défaut (256).

# Si nous voulons les lignes ainsi que les régions remplies, nous devons appeler
# contour séparément ; n'essayez pas de changer la couleur de bord ou la largeur de bord
# des polygones dans les collections renvoyées par contourf.
# Utilisez les niveaux de sortie de l'appel précédent pour vous assurer qu'ils sont les mêmes.

cset2 = axs[0].contour(X, Y, Z, cset1.levels, colors='k')

# Nous n'avons pas vraiment besoin de lignes de contour en tirets pour indiquer les
# régions négatives, donc désactivons-les.

for c in cset2.collections:
    c.set_linestyle('solid')

# Il est plus facile ici de faire un appel séparé à contour que
# de configurer un tableau de couleurs et de largeurs de ligne.
# Nous créons une ligne verte épaisse comme contour nul.
# Spécifiez le niveau nul comme un tuple avec seulement 0 dedans.

cset3 = axs[0].contour(X, Y, Z, (0,), colors='g', linewidths=2)
axs[0].set_title('Contours remplis')
fig.colorbar(cset1, ax=axs[0])


axs[1].imshow(Z, extent=extent, cmap=cmap, norm=norm)
axs[1].contour(Z, levels, colors='k', origin='upper', extent=extent)
axs[1].set_title("Image, origine 'upper'")

axs[2].imshow(Z, origin='lower', extent=extent, cmap=cmap, norm=norm)
axs[2].contour(Z, levels, colors='k', origin='lower', extent=extent)
axs[2].set_title("Image, origine 'lower'")

# Nous utiliserons l'interpolation "nearest" ici pour montrer les
# pixels réels de l'image.
# Notez que les lignes de contour ne s'étendent pas jusqu'au bord de la boîte.
# Cela est intentionnel. Les valeurs de Z sont définies au centre de chaque
# pixel d'image (chaque bloc de couleur dans le sous-graphe suivant), donc
# le domaine qui est conturé ne s'étend pas au-delà de ces centres de pixel.
im = axs[3].imshow(Z, interpolation='nearest', extent=extent,
                   cmap=cmap, norm=norm)
axs[3].contour(Z, levels, colors='k', origin='image', extent=extent)
ylim = axs[3].get_ylim()
axs[3].set_ylim(ylim[::-1])
axs[3].set_title("Origine à partir de rc, axe y inversé")
fig.colorbar(im, ax=axs[3])

fig.tight_layout()
plt.show()
```
