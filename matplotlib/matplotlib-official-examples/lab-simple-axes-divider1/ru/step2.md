# Определение вспомогательной функции

Мы определим вспомогательную функцию `label_axes()`, которая будет использоваться для размещения метки в центре оси и удаления делений на оси.

```python
def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5,.5, text, transform=ax.transAxes,
            horizontalalignment="center", verticalalignment="center")
    ax.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False)
```
