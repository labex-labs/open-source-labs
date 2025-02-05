# 创建散点图

在这一步中，我们将使用Matplotlib创建一个散点图。我们将首先使用NumPy的`random()`函数生成一些随机数据用于绘图。然后，我们将使用`scatter()`函数来创建图表。

```python
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.show()
```
