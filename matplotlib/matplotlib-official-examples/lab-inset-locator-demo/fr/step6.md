# Créer un inset en dehors des axes

Nous pouvons créer un inset en dehors des axes en utilisant le paramètre `bbox_to_anchor` pour spécifier une boîte englobante en coordonnées d'axes qui s'étend en dehors des axes.

```python
# Crée un inset en dehors des axes
axins = inset_axes(ax, width="100%", height="100%",
                   bbox_to_anchor=(1.05,.6,.5,.4),
                   bbox_transform=ax.transAxes, loc=2, borderpad=0)
```
