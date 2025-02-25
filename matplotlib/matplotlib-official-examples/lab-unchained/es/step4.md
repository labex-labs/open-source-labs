# Estableciendo límites y eliminando marcas de graduación

En este paso, estableceremos el límite de y y eliminaremos las marcas de graduación del gráfico.

```python
# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 70)

# No ticks
ax.set_xticks([])
ax.set_yticks([])
```
