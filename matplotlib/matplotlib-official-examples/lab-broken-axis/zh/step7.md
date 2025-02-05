# 调整刻度

现在，我们将调整 x 轴上的刻度。我们将使用 `ax1.xaxis.tick_top` 把第一个子图的刻度移到顶部，使用 `ax1.tick_params(labeltop=False)` 移除第一个子图的刻度标签，并保留第二个子图的刻度标签。

```python
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()
```
