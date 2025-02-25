# Definieren der polaren Achsen

In diesem Schritt werden wir die polaren Achsen definieren und den Skalierungsfaktor festlegen. Wir werden `PolarAxes.PolarTransform()` verwenden, um die polaren Achsen zu definieren.

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

# Definieren der polaren Achsen
tr = Affine2D().scale(np.pi / 180., 1.) + PolarAxes.PolarTransform()
```
