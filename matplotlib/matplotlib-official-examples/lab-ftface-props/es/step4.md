# Imprimir propiedades adicionales de la fuente

En este paso, imprimiremos propiedades adicionales de la fuente que solo están disponibles si la cara es escalable.

```python
if font.scalable:
    # el cuadro delimitador global de la cara (xmin, ymin, xmax, ymax)
    print('Bbox:               ', font.bbox)
    # número de unidades de fuente cubiertas por la EM
    print('EM:                 ', font.units_per_EM)
    # el ascensor en 26,6 unidades
    print('Ascender:           ', font.ascender)
    # el descensor en 26,6 unidades
    print('Descender:          ', font.descender)
    # la altura en 26,6 unidades
    print('Height:             ', font.height)
    # avance horizontal máximo del cursor
    print('Max adv width:      ', font.max_advance_width)
    # lo mismo para el diseño vertical
    print('Max adv height:     ', font.max_advance_height)
    # posición vertical de la barra de subrayado
    print('Underline pos:      ', font.underline_position)
    # grosor vertical del subrayado
    print('Underline thickness:', font.underline_thickness)
```
