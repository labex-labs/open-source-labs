# 自定义图表

既然我们已经有了一个基本的图表，那就来对它进行自定义。

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='red', marker='o')
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()
```

在这里，我们对图表进行了一些自定义设置。我们把线条颜色改成了红色，并给每个数据点添加了圆形标记。我们还为图表添加了标题和坐标轴标签。
