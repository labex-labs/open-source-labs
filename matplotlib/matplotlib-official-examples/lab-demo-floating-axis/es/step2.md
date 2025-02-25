# Definir los ejes polares

En este paso, definiremos los ejes polares y estableceremos el factor de escala. Utilizaremos `PolarAxes.PolarTransform()` para definir los ejes polares.

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

# Define the polar axes
tr = Affine2D().scale(np.pi / 180., 1.) + PolarAxes.PolarTransform()
```
