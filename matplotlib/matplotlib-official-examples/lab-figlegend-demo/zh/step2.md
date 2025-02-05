# 创建一个基本图表

要创建一个基本图表，我们需要定义 x 和 y 值，然后使用 `plt.plot()` 绘制它们。在这里，我们将绘制两个正弦波。

```python
x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.sin(4 * np.pi * x)

plt.plot(x, y1, label='sin(2pix)')
plt.plot(x, y2, label='sin(4pix)')
```
