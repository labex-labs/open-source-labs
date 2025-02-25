# Contrôler la position et la taille des insets

Nous pouvons utiliser les paramètres `bbox_to_anchor` et `bbox_transform` pour contrôler la position et la taille des insets. Ces paramètres permettent un contrôle fin des positions et tailles des insets, ou même de les positionner à des emplacements complètement arbitraires.

```python
# Nous utilisons la transformation des axes comme bbox_transform. Par conséquent,
# la boîte englobante doit être spécifiée en coordonnées d'axes ((0, 0) est le
# coin inférieur gauche des axes, (1, 1) est le coin supérieur droit).
# La boîte englobante (.2,.4,.6,.5) commence à (.2,.4) et s'étend jusqu'à
# (.8,.9) dans ces coordonnées.
# A l'intérieur de cette boîte englobante, un inset de moitié de la largeur
# de la boîte englobante et trois quarts de la hauteur de la boîte englobante
# est créé. Le coin inférieur gauche de l'inset est aligné sur le coin inférieur
# gauche de la boîte englobante (loc=3).
# L'inset est ensuite décalé par la valeur par défaut de 0,5 en unités de la
# taille de police.
axins = inset_axes(ax, width="50%", height="75%",
                   bbox_to_anchor=(.2,.4,.6,.5),
                   bbox_transform=ax.transAxes, loc=3)
```
