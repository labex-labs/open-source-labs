# Ajouter une barre de couleur au graphique

Maintenant, nous allons ajouter une barre de couleur à chaque sous-graphique en utilisant la fonction `make_axes_locatable` de Matplotlib. Cette fonction prend un axe existant, l'ajoute à un nouvel `AxesDivider` et renvoie l'`AxesDivider`. La méthode `append_axes` de l'`AxesDivider` peut ensuite être utilisée pour créer un nouvel axe sur un côté donné ("haut", "droite", "bas" ou "gauche") de l'axe original.

```python
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
cb1 = fig.colorbar(im1, cax=cax1)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cax2.xaxis.set_ticks_position("top")
```
