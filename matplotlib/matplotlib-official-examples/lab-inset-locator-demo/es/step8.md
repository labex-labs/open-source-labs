# Crear un inset centrado en las coordenadas de la figura

Podemos crear un inset que está horizontalmente centrado en las coordenadas de la figura y verticalmente vinculado para alinearse con los ejes usando el método `blended_transform_factory()` para crear una transformación combinada y usándola como el parámetro `bbox_transform`.

```python
# Crea un inset horizontalmente centrado en las coordenadas de la figura y verticalmente
# vinculado para alinearse con los ejes.
from matplotlib.transforms import blended_transform_factory

transform = blended_transform_factory(fig.transFigure, ax2.transAxes)
axins4 = inset_axes(ax2, width="16%", height="34%",
                    bbox_to_anchor=(0, 0, 1, 1),
                    bbox_transform=transform, loc=8, borderpad=0)
```
