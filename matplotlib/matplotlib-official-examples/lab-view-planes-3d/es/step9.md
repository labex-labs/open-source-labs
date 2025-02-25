# Agregar una etiqueta al subgráfico central

Agregamos una etiqueta al subgráfico central para indicar que este es un gráfico de los planos principales de vista tridimensional.

```python
label = 'mplot3d primary view planes\n' + 'ax.view_init(elev, azim, roll)'
annotate_axes(axd['L'], label, fontsize=18)
axd['L'].set_axis_off()
```
