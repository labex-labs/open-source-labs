# Crear ejes insertados

A continuación, crearemos ejes insertados en cada uno de los subgráficos. Usaremos el método `inset_axes()` para crear los ejes insertados. Crearemos cuatro insets con diferentes tamaños y ubicaciones.

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Crea un inset de 1,3 pulgadas de ancho y 0,9 pulgadas de alto
# en la ubicación predeterminada de la esquina superior derecha
axins = inset_axes(ax, width=1.3, height=0.9)

# Crea un inset con un 30% del ancho y un 40% de la altura del
# cuadro delimitador del eje padre
# en la esquina inferior izquierda (loc=3)
axins2 = inset_axes(ax, width="30%", height="40%", loc=3)

# Crea un inset con especificaciones mixtas en el segundo subgráfico;
# el ancho es el 30% del cuadro delimitador del eje padre y
# la altura es de 1 pulgada en la esquina superior izquierda (loc=2)
axins3 = inset_axes(ax2, width="30%", height=1., loc=2)

# Crea un inset en la esquina inferior derecha (loc=4) con un borde de 1, es decir,
# 10 puntos de relleno (ya que 10pt es el tamaño de fuente predeterminado)
# con respecto al eje padre
axins4 = inset_axes(ax2, width="20%", height="20%", loc=4, borderpad=1)
```
