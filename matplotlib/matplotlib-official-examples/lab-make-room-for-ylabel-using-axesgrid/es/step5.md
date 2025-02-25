# Hacer espacio para la etiqueta del eje y y ajustar los ejes

En este paso, usamos el método `make_axes_area_auto_adjustable` para hacer espacio para la etiqueta del eje y en ambos ejes. También usamos el parámetro `use_axes` para especificar los ejes que se van a ajustar y el parámetro `pad` para ajustar el espaciado entre los ejes.

```python
make_axes_area_auto_adjustable(ax1, pad=0.1, use_axes=[ax1, ax2])
make_axes_area_auto_adjustable(ax2, pad=0.1, use_axes=[ax1, ax2])
```
