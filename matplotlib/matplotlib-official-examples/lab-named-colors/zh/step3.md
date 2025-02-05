# 创建一个简单的图表

既然我们已经导入了Matplotlib，就可以用它来创建一个简单的图表。在这个例子中，我们将创建一个折线图，展示x值和y值之间的关系。

```python
import matplotlib.pyplot as plt

# x轴的值
x = [1, 2, 3, 4, 5]

# y轴的值
y = [2, 4, 6, 8, 10]

# 绘制线条
plt.plot(x, y)

# 设置标题
plt.title("简单折线图")

# 设置x轴标签
plt.xlabel("X轴")

# 设置y轴标签
plt.ylabel("Y轴")

# 显示图表
plt.show()
```
