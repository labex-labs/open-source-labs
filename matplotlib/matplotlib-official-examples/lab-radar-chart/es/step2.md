# Definir la función del gráfico de radar

A continuación, definiremos una función para crear un gráfico de radar. Esta función tomará dos argumentos: `num_vars` y `frame`. `num_vars` es el número de variables para el gráfico de radar, y `frame` especifica la forma del marco que rodea los ejes.

```python
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    # código de la función va aquí
```
