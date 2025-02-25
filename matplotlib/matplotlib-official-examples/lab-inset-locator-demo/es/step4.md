# Controlar la posición y el tamaño del inset

Podemos usar los parámetros `bbox_to_anchor` y `bbox_transform` para controlar la posición y el tamaño del inset. Estos parámetros permiten un control detallado de la posición y el tamaño del inset o incluso para posicionar el inset en posiciones completamente arbitrarias.

```python
# Usamos la transformación de los ejes como bbox_transform. Por lo tanto, el cuadro delimitador
# debe especificarse en coordenadas de ejes ((0, 0) es la esquina inferior izquierda
# del eje, (1, 1) es la esquina superior derecha).
# El cuadro delimitador (.2,.4,.6,.5) comienza en (.2,.4) y abarca hasta (.8,.9)
# en esas coordenadas.
# Dentro de este cuadro delimitador se crea un inset con la mitad del ancho del cuadro delimitador y
# tres cuartos de la altura del cuadro delimitador. La esquina inferior izquierda
# del inset se alinea con la esquina inferior izquierda del cuadro delimitador (loc=3).
# El inset luego se desplaza por el valor predeterminado de 0,5 en unidades del tamaño de fuente.
axins = inset_axes(ax, width="50%", height="75%",
                   bbox_to_anchor=(.2,.4,.6,.5),
                   bbox_transform=ax.transAxes, loc=3)
```
