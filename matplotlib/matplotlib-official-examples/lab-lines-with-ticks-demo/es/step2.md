# Trazar una línea recta con Ticked Patheffect

Ahora trazaremos una línea diagonal recta con el efecto de ruta con marcas de graduación.

```python
# Plot a straight diagonal line with ticked style path
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1], [0, 1], label="Line",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])
```
