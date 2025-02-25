# Стили заливки маркеров

Для закрашенных маркеров можно отдельно указать цвет контура и цвет заливки. Кроме того, параметр `fillstyle` можно настроить на пустую заливку, полную заливку или наполовину заливку в различных направлениях. Стили наполовину заполненных маркеров используют `markerfacecoloralt` в качестве вторичного цвета заливки. Следующий код демонстрирует, как создавать стили заливки маркеров:

```python
fig, ax = plt.subplots()
fig.suptitle('Marker fillstyle', fontsize=14)
fig.subplots_adjust(left=0.4)

filled_marker_style = dict(marker='o', linestyle=':', markersize=15,
                           color='darkgrey',
                           markerfacecolor='tab:blue',
                           markerfacecoloralt='lightsteelblue',
                           markeredgecolor='brown')

for y, fill_style in enumerate(Line2D.fillStyles):
    ax.text(-0.5, y, repr(fill_style), **text_style)
    ax.plot([y] * 3, fillstyle=fill_style, **filled_marker_style)
format_axes(ax)
```
