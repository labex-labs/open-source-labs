# Dirección/lado de las marcas de graduación

En este paso, cambiaremos el lado de las marcas de graduación.

```python
fig, ax = plt.subplots(figsize=(6, 6))
line_x = line_y = [0, 1]
ax.plot(line_x, line_y, label="Linea",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])

ax.plot(line_x, line_y, label="Lado opuesto",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=-135)])

ax.legend()
plt.show()
```

Este código creará una línea con marcas de graduación en ambos lados.
