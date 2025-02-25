# Функция настройки осей

Создайте функцию для настройки осей. Эта функция будет настраивать значения делений по осям x и y.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
