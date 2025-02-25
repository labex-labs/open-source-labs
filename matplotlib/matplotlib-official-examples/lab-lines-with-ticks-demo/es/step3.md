# Trazar una línea curva con Ticked Patheffect

Ahora trazaremos una línea curva con el efecto de ruta con marcas de graduación.

```python
# Plot a curved line with ticked style path
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```
