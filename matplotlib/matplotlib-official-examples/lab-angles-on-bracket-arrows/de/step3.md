# Erstellen von Klammerpfeilen mit Winkelannotationen

Wir werden mit `FancyArrowPatch` drei Klammerpfeilstile mit Winkelannotationen erstellen. Jeder Klammerpfeil wird einen anderen Winkelwert für _angleA_ und _angleB_ haben. Wir werden auch vertikale Linien hinzufügen, um die Position der Winkelannotationen anzuzeigen.

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
