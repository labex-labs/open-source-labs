# 设置刻度和网格线的 Zorder

我们可以使用 `set_axisbelow()` 方法或 `axes.axisbelow` 参数来设置刻度和网格线的 `zorder`。

```python
ax = plt.axes()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
```
