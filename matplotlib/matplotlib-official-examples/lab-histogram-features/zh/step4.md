# 添加最佳拟合线

在这一步中，我们将为直方图添加一条最佳拟合线。我们将计算该线的 y 值，并将其绘制在直方图之上。

```python
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
```
