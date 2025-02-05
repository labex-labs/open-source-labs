# 创建一个简单的折线图

我们将创建一个简单的折线图，其X轴值范围从0到5，并具有相应的Y轴值。我们将使用`pyplot`模块提供的`plot`函数来创建折线图。

```python
# 创建X轴值
x = np.arange(0, 5, 0.1)

# 创建Y轴值
y = np.sin(x)

# 创建一个折线图
plt.plot(x, y)

# 为图表添加标题和标签
plt.title('简单折线图')
plt.xlabel('X轴')
plt.ylabel('Y轴')

# 显示图表
plt.show()
```
