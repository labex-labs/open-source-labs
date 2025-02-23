# Plus d'exemples de systèmes de coordonnées

Voici quelques exemples supplémentaires de systèmes de coordonnées et de la manière dont la position des annotations peut être spécifiée.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)

bbox_args = dict(boxstyle="round", fc="0.8")
arrow_args = dict(arrowstyle="->")

# Ici, nous allons démontrer les limites du système de coordonnées et la manière dont
# nous plaçons le texte d'annotation.

ax1.annotate('fraction de figure : 0, 0', xy=(0, 0), xycoords='fraction de figure',
             xytext=(20, 20), textcoords='points d\'offset',
             ha="gauche", va="bas",
             bbox=bbox_args,
             arrowprops=arrow_args)

ax1.annotate('fraction de figure : 1, 1', xy=(1, 1), xycoords='fraction de figure',
             xytext=(-20, -20), textcoords='points d\'offset',
             ha="droite", va="haut",
             bbox=bbox_args,
             arrowprops=arrow_args)

ax1.annotate('fraction d\'axes : 0, 0', xy=(0, 0), xycoords='fraction d\'axes',
             xytext=(20, 20), textcoords='points d\'offset',
             ha="gauche", va="bas",
             bbox=bbox_args,
             arrowprops=arrow_args)

ax1.annotate('fraction d\'axes : 1, 1', xy=(1, 1), xycoords='fraction d\'axes',
             xytext=(-20, -20), textcoords='points d\'offset',
             ha="droite", va="haut",
             bbox=bbox_args,
             arrowprops=arrow_args)

# Il est également possible de générer des annotations déplaçables

an1 = ax1.annotate('Faites-moi glisser 1', xy=(.5,.7), xycoords='data',
                   ha="centre", va="centre",
                   bbox=bbox_args)

an2 = ax1.annotate('Faites-moi glisser 2', xy=(.5,.5), xycoords=an1,
                   xytext=(.5,.3), textcoords='fraction d\'axes',
                   ha="centre", va="centre",
                   bbox=bbox_args,
                   arrowprops=dict(patchB=an1.get_bbox_patch(),
                                   connectionstyle="arc3,rad=0.2",
                                   **arrow_args))
an1.draggable()
an2.draggable()

an3 = ax1.annotate('', xy=(.5,.5), xycoords=an2,
                   xytext=(.5,.5), textcoords=an1,
                   ha="centre", va="centre",
                   bbox=bbox_args,
                   arrowprops=dict(patchA=an1.get_bbox_patch(),
                                   patchB=an2.get_bbox_patch(),
                                   connectionstyle="arc3,rad=0.2",
                                   **arrow_args))

# Enfin, nous allons montrer quelques annotations et positions plus complexes

text = ax2.annotate('xy=(0, 1)\nxycoords=("data", "fraction d\'axes")',
                    xy=(0, 1), xycoords=("data", 'fraction d\'axes'),
                    xytext=(0, -20), textcoords='points d\'offset',
                    ha="centre", va="haut",
                    bbox=bbox_args,
                    arrowprops=arrow_args)

ax2.annotate('xy=(0.5, 0)\nxycoords=artist',
             xy=(0.5, 0.), xycoords=text,
             xytext=(0, -20), textcoords='points d\'offset',
             ha="centre", va="haut",
             bbox=bbox_args,
             arrowprops=arrow_args)

ax2.annotate('xy=(0.8, 0.5)\nxycoords=ax1.transData',
             xy=(0.8, 0.5), xycoords=ax1.transData,
             xytext=(10, 10),
             textcoords=OffsetFrom(ax2.bbox, (0, 0), "points"),
             ha="gauche", va="bas",
             bbox=bbox_args,
             arrowprops=arrow_args)

ax2.set(xlim=[-2, 2], ylim=[-2, 2])
```
