# 创建箭袋图

我们可以使用 `ax.quiver()` 函数创建箭袋图。我们将 `X`、`Y`、`U` 和 `V` 数组作为参数传入。

```python
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
```
