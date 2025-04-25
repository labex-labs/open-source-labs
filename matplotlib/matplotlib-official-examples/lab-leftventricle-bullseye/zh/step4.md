# 创建柱状图

我们将创建一个柱状图，其 X 轴值范围从 0 到 5，并具有相应的 Y 轴值。我们将使用`pyplot`模块提供的`bar`函数来创建柱状图。

```python
# 创建 X 轴值
x = np.arange(0, 5, 0.1)

# 创建 Y 轴值
y = np.sin(x)

# 创建一个柱状图
plt.bar(x, y)

# 为图表添加标题和标签
plt.title('柱状图')
plt.xlabel('X 轴')
plt.ylabel('Y 轴')

# 显示图表
plt.show()
```
