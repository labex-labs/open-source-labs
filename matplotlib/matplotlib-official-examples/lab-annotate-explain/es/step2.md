# Conectar dos puntos con una flecha

En este paso, conectaremos los dos puntos con una flecha. Utilizaremos la función `annotate` para crear la flecha y personalizaremos el estilo y el color de la flecha.

```python
ax = axs.flat[0]
ax.plot([x1, x2], [y1, y2], ".")
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
