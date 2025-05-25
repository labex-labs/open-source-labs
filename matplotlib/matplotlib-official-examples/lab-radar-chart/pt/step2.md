# Definir a Função do Gráfico Radar

Em seguida, definiremos uma função para criar um gráfico radar. Esta função receberá dois argumentos: `num_vars` e `frame`. `num_vars` é o número de variáveis para o gráfico radar, e `frame` especifica a forma da moldura que circunda os eixos.

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
