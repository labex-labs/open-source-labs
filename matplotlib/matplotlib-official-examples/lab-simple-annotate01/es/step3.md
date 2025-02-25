# Agregar una anotación de texto

Ahora agregaremos una anotación de texto al gráfico. El siguiente código agregará el texto "Punto de datos 1" en el primer punto de datos.

```python
ax.annotate("Punto de datos 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05))
```
