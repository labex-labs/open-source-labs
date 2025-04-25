# 自定义图表

Matplotlib 为图表提供了广泛的自定义选项。以下是一个自定义我们简单折线图的示例代码：

```python
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 创建图表
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o', markersize=8, markerfacecolor='yellow')

# 添加标签和标题
plt.xlabel('X 轴')
plt.ylabel('Y 轴')
plt.title('自定义图表')

# 显示图表
plt.show()
```

在这段代码中，我们使用`plot()`方法的各种参数来自定义图表。我们将线条颜色更改为红色，线宽更改为 2，线型更改为虚线（`--`），标记更改为圆形（`o`），标记大小更改为 8，标记面颜色更改为黄色。
