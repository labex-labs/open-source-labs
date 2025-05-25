# Rotacionar a Forma de Golfinho

Vamos rotacionar a forma de golfinho em 60 graus usando a função `Affine2D().rotate_deg()`.

```python
from matplotlib.transforms import Affine2D

vertices = Affine2D().rotate_deg(60).transform(vertices)
dolphin_path2 = Path(vertices, codes)
dolphin_patch2 = PathPatch(dolphin_path2, facecolor=(0.5, 0.5, 0.5),
                           edgecolor=(0.0, 0.0, 0.0))
ax.add_patch(dolphin_patch2)
```
