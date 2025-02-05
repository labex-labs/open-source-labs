# 创建柱状图

在这一步中，我们将使用Matplotlib创建一个柱状图。我们将首先使用NumPy的`random()`函数生成一些用于绘图的数据。然后，我们将使用`bar()`函数来创建图表。

```python
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

plt.bar(x, y)
plt.show()
```
