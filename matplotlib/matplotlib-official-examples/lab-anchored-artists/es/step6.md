# Agregar barra de escala

En este paso, agregaremos una barra de escala a la gráfica usando Objetos Anclados.

```python
def draw_sizebar(ax):
    """
    Dibuja una barra horizontal con una longitud de 0,1 en coordenadas de datos,
    con una etiqueta fija alineada al centro debajo.
    """
    size = 0.1
    text = r"1$^{\prime}$"
    sizebar = AuxTransformBox(ax.transData)
    sizebar.add_artist(Line2D([0, size], [0, 0], color="black"))
    text = TextArea(text)
    packer = VPacker(
        children=[sizebar, text], align="center", sep=5)  # separación en puntos.
    ax.add_artist(AnchoredOffsetbox(
        child=packer, loc="lower center", frameon=False,
        pad=0.1, borderpad=0.5))  # rellenos relativos al tamaño de fuente de la leyenda.

draw_sizebar(ax)
```
