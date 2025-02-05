# 创建子图

接下来，我们将创建两个子图——一个用于展示离群值，另一个用于展示大部分数据。我们将使用 `plt.subplots` 创建子图，并将 `sharex` 参数设置为 `True`，以便它们共享相同的 x 轴。

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
```
