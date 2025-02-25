# Agregar una barra de colores

Agrega una barra de colores al eje insertado utilizando la función `inset_axes`. Establece el ancho, alto, ubicación y cuadro delimitador de la barra de colores.

```python
cax = inset_axes(axins,
                 width="5%",  # width = 10% of parent_bbox width
                 height="100%",  # height : 50%
                 loc='lower left',
                 bbox_to_anchor=(1.05, 0., 1, 1),
                 bbox_transform=axins.transAxes,
                 borderpad=0,
                 )
fig.colorbar(im, cax=cax)
```
