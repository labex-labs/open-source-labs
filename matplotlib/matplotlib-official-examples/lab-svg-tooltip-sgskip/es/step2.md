# Agregar recuadros y anotaciones de mensaje emergente

Luego agregamos los recuadros y las anotaciones de mensaje emergente a la gráfica. Las anotaciones de mensaje emergente se crean usando el método `annotate`. Establecemos el parámetro `xy` en las coordenadas del recuadro y `xytext` en `(0, 0)` para posicionar el mensaje emergente directamente sobre el recuadro. También establecemos el parámetro `textcoords` en `'offset points'` para alinear el mensaje emergente con el recuadro. Establecemos el parámetro `color` en `'w'` para que el texto sea blanco, `ha` en `'center'` para centrar el texto horizontalmente, `fontsize` en `8` para establecer el tamaño de fuente y `bbox` para establecer el estilo de la caja del mensaje emergente.

```python
for i, (item, label) in enumerate(zip(shapes, labels)):
    patch = ax.add_patch(item)
    annotate = ax.annotate(labels[i], xy=item.get_xy(), xytext=(0, 0),
                           textcoords='offset points', color='w', ha='center',
                           fontsize=8, bbox=dict(boxstyle='round, pad=.5',
                                                 fc=(.1,.1,.1,.92),
                                                 ec=(1., 1., 1.), lw=1,
                                                 zorder=1))

    ax.add_patch(patch)
    patch.set_gid(f'mypatch_{i:03d}')
    annotate.set_gid(f'mytooltip_{i:03d}')
```
