# 创建用于绘图的网格

现在，我们将创建一个用于绘图的网格。该网格将用于绘制网格上每个点的预测概率。我们还将定义网格的步长。

```python
h = 0.02  # 网格中的步长

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
```
