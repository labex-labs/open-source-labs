# 创建简单图表

Matplotlib中最基本的图表是折线图。你可以使用`plot()`方法创建折线图。以下是一个创建简单折线图的示例代码：

```python
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 创建图表
plt.plot(x, y)

# 添加标签和标题
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.title('简单图表')

# 显示图表
plt.show()
```

在这段代码中，我们首先将数据点定义为两个列表`x`和`y`。然后，我们使用`plot()`方法创建一个图表，并传入我们的数据点。接着，我们使用`xlabel()`、`ylabel()`和`title()`方法为X轴和Y轴添加标签以及为图表添加标题。最后，我们使用`show()`方法显示图表。
