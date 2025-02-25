# Agregar una anotación de forma

Ahora agregaremos una anotación de forma al gráfico. El siguiente código agregará un rectángulo alrededor del segundo punto de datos.

```python
bbox = dict(boxstyle="round", fc="0.8")
ax.annotate("Punto de datos 2", xy=(2, 4), xytext=(2.5, 4.5),
            bbox=bbox,
            arrowprops=dict(facecolor="black", shrink=0.05))
```
