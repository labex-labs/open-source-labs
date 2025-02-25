# Opciones de tamaño

La quinta propiedad de fuente que exploraremos es la opción de tamaño. Esta propiedad le permite establecer el tamaño de fuente utilizado en su gráfica.

```python
# Muestra las opciones de tamaño
sizes = ['xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
fig.text(0.9, 0.9,'size', fontproperties=heading_font, **alignment)
for k, size in enumerate(sizes):
    font = FontProperties()
    font.set_size(size)
    fig.text(0.9, yp[k], size, fontproperties=font, **alignment)
```
