# Создаем скобочные стрелочки с аннотациями углов

Мы создадим три стиля скобочных стрелочек с аннотациями углов с использованием `FancyArrowPatch`. Каждая скобочная стрелочка будет иметь разные значения угла для _angleA_ и _angleB_. Также добавим вертикальные линии, чтобы показать положение аннотаций углов.

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
