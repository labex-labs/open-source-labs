# Définir la fonction de graphique radar

Ensuite, nous allons définir une fonction pour créer un graphique radar. Cette fonction prendra deux arguments : `num_vars` et `frame`. `num_vars` est le nombre de variables pour le graphique radar, et `frame` spécifie la forme du cadre entourant les axes.

```python
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    # code for the function goes here
```
