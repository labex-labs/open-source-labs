# Показать только внешние контуры

В этом шаге мы удалим контуры для внутренних подграфиков и покажем только внешние контуры. Это сделает график выглядеть чище.

```python
for ax in fig.get_axes():
    ss = ax.get_subplotspec()
    ax.spines.top.set_visible(ss.is_first_row())
    ax.spines.bottom.set_visible(ss.is_last_row())
    ax.spines.left.set_visible(ss.is_first_col())
    ax.spines.right.set_visible(ss.is_last_col())
```
