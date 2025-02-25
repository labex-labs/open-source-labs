# Определяем полярные оси

В этом шаге мы определим полярные оси и зададим коэффициент масштабирования. Для определения полярных осей мы будем использовать `PolarAxes.PolarTransform()`.

```python
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

# Define the polar axes
tr = Affine2D().scale(np.pi / 180., 1.) + PolarAxes.PolarTransform()
```
