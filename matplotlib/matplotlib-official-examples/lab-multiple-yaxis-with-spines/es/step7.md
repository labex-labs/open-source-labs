# Establecer los colores de las marcas de graduación

Establecemos los colores de las marcas de graduación para cada eje y para que coincidan con el color de las etiquetas.

```python
ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())
```
