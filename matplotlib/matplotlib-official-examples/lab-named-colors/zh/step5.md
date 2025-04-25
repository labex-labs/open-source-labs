# 创建柱状图

我们还可以使用 Matplotlib 来创建柱状图。在这个例子中，我们将创建一个柱状图，展示苹果、香蕉和橙子的销售数量。

```python
import matplotlib.pyplot as plt

# 要绘制的数据
苹果 = 10
香蕉 = 15
橙子 = 5

# 创建柱状图
plt.bar(["Apples", "Bananas", "Oranges"], [苹果, 香蕉, 橙子])

# 设置标题
plt.title("简单柱状图")

# 设置 x 轴标签
plt.xlabel("水果")

# 设置 y 轴标签
plt.ylabel("数量")

# 显示图表
plt.show()
```
