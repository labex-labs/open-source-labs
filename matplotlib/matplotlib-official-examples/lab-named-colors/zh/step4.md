# 创建散点图

我们也可以使用Matplotlib来创建散点图。在这个例子中，我们将创建一个散点图，展示x值和y值之间的关系。

```python
import matplotlib.pyplot as plt

# x轴的值
x = [1, 2, 3, 4, 5]

# y轴的值
y = [2, 4, 6, 8, 10]

# 绘制点
plt.scatter(x, y)

# 设置标题
plt.title("简单散点图")

# 设置x轴标签
plt.xlabel("X轴")

# 设置y轴标签
plt.ylabel("Y轴")

# 显示图表
plt.show()
```
