# Crear función para las cajas de error

Ahora crearemos una función llamada `make_error_boxes` que creará el parche rectangular definido por los límites de las barras en ambas direcciones x e y.

```python
def make_error_boxes(ax, xdata, ydata, xerror, yerror, facecolor='r',
                     edgecolor='none', alpha=0.5):

    # Bucle sobre los puntos de datos; crear caja a partir de los errores en cada punto
    errorboxes = [Rectangle((x - xe[0], y - ye[0]), xe.sum(), ye.sum())
                  for x, y, xe, ye in zip(xdata, ydata, xerror.T, yerror.T)]

    # Crear colección de parches con el color/transparencia especificados
    pc = PatchCollection(errorboxes, facecolor=facecolor, alpha=alpha,
                         edgecolor=edgecolor)

    # Agregar la colección al eje
    ax.add_collection(pc)

    # Graficar barras de error
    artists = ax.errorbar(xdata, ydata, xerr=xerror, yerr=yerror,
                          fmt='none', ecolor='k')

    return artists
```
