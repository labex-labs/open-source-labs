# 绘制数据

在这一步中，我们将使用 Matplotlib 的 `plot` 函数在轴对象上绘制数据。我们将绘制六条具有不同斜率和随机噪声的不同线条。

```python
ax.plot(x, np.sin(x) + x + noise)
ax.plot(x, np.sin(x) + 0.5 * x + noise)
ax.plot(x, np.sin(x) + 2 * x + noise)
ax.plot(x, np.sin(x) - 0.5 * x + noise)
ax.plot(x, np.sin(x) - 2 * x + noise)
ax.plot(x, np.sin(x) + noise)
```
