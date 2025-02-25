# Définir les axes polaires

Dans cette étape, nous allons définir les axes polaires et définir le facteur d'échelle. Nous utiliserons `PolarAxes.PolarTransform()` pour définir les axes polaires.

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

# Définir les axes polaires
tr = Affine2D().scale(np.pi / 180., 1.) + PolarAxes.PolarTransform()
```
