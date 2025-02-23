# Spécification des points de texte et des points d'annotation

Vous devez spécifier un point d'annotation `xy=(x, y)` pour annoter ce point. De plus, vous pouvez spécifier un point de texte `xytext=(x, y)` pour la position du texte de cette annotation. Facultativement, vous pouvez spécifier le système de coordonnées de `xy` et `xytext` avec l'une des chaînes suivantes pour `xycoords` et `textcoords` (valeur par défaut : 'data') :

- 'points de figure' : points à partir du coin inférieur gauche de la figure
- 'pixels de figure' : pixels à partir du coin inférieur gauche de la figure
- 'fraction de figure' : (0, 0) est le coin inférieur gauche de la figure et (1, 1) est le coin supérieur droit
- 'points d'axes' : points à partir du coin inférieur gauche des axes
- 'pixels d'axes' : pixels à partir du coin inférieur gauche des axes
- 'fraction d'axes' : (0, 0) est le coin inférieur gauche des axes et (1, 1) est le coin supérieur droit
- 'points d'offset' : Spécifiez un décalage (en points) à partir de la valeur xy
- 'pixels d'offset' : Spécifiez un décalage (en pixels) à partir de la valeur xy
- 'data' : utiliser le système de coordonnées de données des axes

Remarque : pour les systèmes de coordonnées physiques (points ou pixels), l'origine est le (bas, gauche) de la figure ou des axes.

Facultativement, vous pouvez spécifier les propriétés de la flèche qui trace une flèche du texte au point annoté en donnant un dictionnaire de propriétés de flèche. Les clés valides sont :

- `width` : la largeur de la flèche en points
- `frac` : la fraction de la longueur de la flèche occupée par la tête
- `headwidth` : la largeur de la base de la tête de flèche en points
- `shrink` : déplacer l'extrémité et la base d'un certain pourcentage loin du point annoté et du texte
- `n'importe quelle clé pour matplotlib.patches.polygon` (par exemple, facecolor)

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom

# Créez notre figure et les données que nous utiliserons pour tracer
fig, ax = plt.subplots(figsize=(4, 4))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

# Tracez une ligne et ajoutez quelques annotations simples
line, = ax.plot(t, s)
ax.annotate('pixels de figure',
            xy=(10, 10), xycoords='pixels de figure')
ax.annotate('points de figure',
            xy=(107, 110), xycoords='points de figure',
            fontsize=12)
ax.annotate('fraction de figure',
            xy=(.025,.975), xycoords='fraction de figure',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

# Les exemples suivants montrent comment ces flèches sont dessinées.

ax.annotate('décalage de point à partir des données',
            xy=(3, 1), xycoords='data',
            xytext=(-10, 90), textcoords='points d'offset',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')

ax.annotate('fraction d'axes',
            xy=(2, 1), xycoords='data',
            xytext=(0.36, 0.68), textcoords='fraction d'axes',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# Vous pouvez également utiliser des points ou des pixels négatifs pour spécifier à partir de (droite, haut).
# Par exemple, (-10, 10) est 10 points à gauche du côté droit des axes et 10
# points au-dessus du bas

ax.annotate('décalage de pixel à partir de la fraction d'axes',
            xy=(1, 0), xycoords='fraction d'axes',
            xytext=(-20, 20), textcoords='pixels d'offset',
            horizontalalignment='right',
            verticalalignment='bottom')

ax.set(xlim=(-1, 5), ylim=(-3, 5))
```
