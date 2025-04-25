# 偏移坐标轴边框

我们将使用 `set_position()` 函数把左边框和下边框向外偏移 10 个点。`set_position()` 的参数是一个包含两个元素的元组。第一个元素表示边框的位置，第二个元素表示边框到绘图区域的距离。

```python
ax.spines[['left', 'bottom']].set_position(('outward', 10))
```
