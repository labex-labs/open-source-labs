# Definir os Eixos Polares

Nesta etapa, definiremos os eixos polares e definiremos o fator de escala. Usaremos `PolarAxes.PolarTransform()` para definir os eixos polares.

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

# Define the polar axes
tr = Affine2D().scale(np.pi / 180., 1.) + PolarAxes.PolarTransform()
```
