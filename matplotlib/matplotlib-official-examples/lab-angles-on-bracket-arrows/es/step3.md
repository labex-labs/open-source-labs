# Crear flechas con corchetes con anotaciones de ángulo

Crearemos tres estilos de flechas con corchetes con anotaciones de ángulo usando `FancyArrowPatch`. Cada flecha con corchete tendrá un valor de ángulo diferente para _angleA_ y _angleB_. También agregaremos líneas verticales para indicar la posición de las anotaciones de ángulo.

```python
style = ']-['
for i, angle in enumerate([-40, 0, 60]):
    y = 2*i
    arrow_centers = ((1, y), (5, y))
    vlines = ((1, y + 0.5), (5, y + 0.5))
    anglesAB = (angle, -angle)
    bracketstyle = f"{style}, angleA={anglesAB[0]}, angleB={anglesAB[1]}"
    bracket = FancyArrowPatch(*arrow_centers, arrowstyle=bracketstyle,
                              mutation_scale=42)
    ax.add_patch(bracket)
    ax.text(3, y + 0.05, bracketstyle, ha="center", va="bottom", fontsize=14)
    ax.vlines([line[0] for line in vlines], [y, y], [line[1] for line in vlines],
              linestyles="--", color="C0")
```
