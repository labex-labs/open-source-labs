# Ajouter une barre de couleur

Ajoutez une barre de couleur à l'axe inséré à l'aide de la fonction `inset_axes`. Réglez la largeur, la hauteur, l'emplacement et la boîte englobante de la barre de couleur.

```python
cax = inset_axes(axins,
                 width="5%",  # width = 10% of parent_bbox width
                 height="100%",  # height : 50%
                 loc='lower left',
                 bbox_to_anchor=(1.05, 0., 1, 1),
                 bbox_transform=axins.transAxes,
                 borderpad=0,
                 )
fig.colorbar(im, cax=cax)
```
