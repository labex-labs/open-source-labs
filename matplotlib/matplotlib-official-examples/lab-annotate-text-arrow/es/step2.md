# Agregar anotaciones de texto al gráfico

A continuación, agregaremos anotaciones de texto al gráfico utilizando la función `ax.text()`. Crearemos dos anotaciones, una para "Muestra A" y otra para "Muestra B".

```python
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Muestra A", ha="center", va="center", size=20,
        bbox=bbox_props)
ax.text(2, 2, "Muestra B", ha="center", va="center", size=20,
        bbox=bbox_props)
```
