# Agregar etiquetas y título al gráfico

El último paso es agregar etiquetas y un título al gráfico. Agregaremos un título al gráfico, una etiqueta para el eje x y una leyenda para el gráfico.

```python
ax.set_title('Cup height by group and beverage choice')
ax.set_xlabel('Group')
ax.legend()
ax.autoscale_view()
```
