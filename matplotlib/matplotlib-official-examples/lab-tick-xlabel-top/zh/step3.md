# 将 x 轴刻度标签移至顶部

要将 x 轴刻度标签移至顶部，我们将使用 `tick_params()` 函数，并将 `top` 和 `labeltop` 参数设置为 `True`，将 `bottom` 和 `labelbottom` 参数设置为 `False`。

```python
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
```
