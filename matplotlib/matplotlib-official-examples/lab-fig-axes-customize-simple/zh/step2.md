# 创建图形并设置背景

我们将使用 `plt.figure()` 方法创建一个图形，该方法会创建一个 `matplotlib.figure.Figure` 实例。我们将使用 `rect.set_facecolor()` 方法设置图形的背景颜色。

```python
fig = plt.figure()
rect = fig.patch  # 一个矩形实例
rect.set_facecolor('lightgoldenrodyellow')
```
