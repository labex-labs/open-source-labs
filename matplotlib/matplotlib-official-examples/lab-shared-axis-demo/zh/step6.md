# 移除刻度标签

我们可以通过使用 `ax.get_xticklabels()` 方法更改标签的可见性，从而从特定子图中移除刻度标签。在这个例子中，我们将移除第二个子图 x 轴上的刻度标签。

```python
plt.tick_params('x', labelbottom=False)
```
