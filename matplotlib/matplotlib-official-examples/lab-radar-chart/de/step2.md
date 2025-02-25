# Definiere die Funktion für das Radar-Chart

Als nächstes definieren wir eine Funktion, um ein Radar-Chart zu erstellen. Diese Funktion nimmt zwei Argumente entgegen: `num_vars` und `frame`. `num_vars` ist die Anzahl der Variablen für das Radar-Chart, und `frame` gibt die Form des Rahmens an, der die Achsen umgibt.

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
