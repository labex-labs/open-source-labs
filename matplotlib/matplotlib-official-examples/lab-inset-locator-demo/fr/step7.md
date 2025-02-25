# Créer un inset avec une boîte englobante à 2-uplets

Nous pouvons créer un inset avec une boîte englobante à 2-uplets en spécifiant la largeur et la hauteur en pouces et en utilisant le paramètre `bbox_to_anchor` pour spécifier le coin inférieur gauche de l'inset.

```python
# Crée un inset avec une boîte englobante à 2-uplets. Notez que cela crée une
# boîte englobante sans étendue. Cela n'a donc de sens que lorsqu'on spécifie
# la largeur et la hauteur en unités absolues (pouces).
axins2 = inset_axes(ax, width=0.5, height=0.4,
                    bbox_to_anchor=(0.33, 0.25),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
```
