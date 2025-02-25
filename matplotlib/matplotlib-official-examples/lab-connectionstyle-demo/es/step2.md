# Definir la función para crear estilos de conexión de anotaciones

Definiremos una función que tome dos parámetros: el objeto de eje y el estilo de conexión. La función graficará dos puntos de datos y creará una anotación con el estilo de conexión especificado.

```python
def demo_con_style(ax, connectionstyle):
    x1, y1 = 0.3, 0.2
    x2, y2 = 0.8, 0.6

    ax.plot([x1, x2], [y1, y2], ".")
    ax.annotate("",
                xy=(x1, y1), xycoords='data',
                xytext=(x2, y2), textcoords='data',
                arrowprops=dict(arrowstyle="->", color="0.5",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle=connectionstyle,
                                ),
                )

    ax.text(.05,.95, connectionstyle.replace(",", ",\n"),
            transform=ax.transAxes, ha="left", va="top")
```
