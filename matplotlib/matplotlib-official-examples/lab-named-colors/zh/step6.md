# 创建饼图

我们也可以使用 Matplotlib 来创建饼图。在这个例子中，我们将创建一个饼图，展示喜欢不同类型披萨的人的百分比。

```python
import matplotlib.pyplot as plt

# 要绘制的数据
sizes = [30, 40, 10, 20]
labels = ["意大利辣香肠", "蘑菇", "洋葱", "香肠"]

# 创建饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# 设置标题
plt.title("简单饼图")

# 显示图表
plt.show()
```
