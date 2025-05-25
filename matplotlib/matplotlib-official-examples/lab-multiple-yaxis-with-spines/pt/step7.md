# Definir as cores das marcas de escala (tick colors)

Definimos as cores das marcas de escala (tick colors) para cada eixo y para corresponder à cor dos rótulos.

```python
ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())
```
