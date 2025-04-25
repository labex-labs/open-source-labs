# 创建一个简单的折线图

在这一步中，我们将使用 Matplotlib 创建一个简单的折线图。我们将首先使用 NumPy 的`linspace()`函数和`cos()`函数生成一些要绘制的数据。然后，我们将使用`plot()`函数来创建图表。

```python
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.show()
```
