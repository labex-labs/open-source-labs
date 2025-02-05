# 创建不同类型的图表

Matplotlib支持多种类型的图表，包括折线图、散点图、柱状图等等。以下是一个创建散点图的示例代码：

```python
import matplotlib.pyplot as plt
import numpy as np

# 生成一些随机数据
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# 创建一个散点图
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# 添加标签和标题
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.title('散点图')

# 显示图表
plt.show()
```

在这段代码中，我们使用`scatter()`方法创建一个散点图。我们使用NumPy库生成一些随机数据，并将其传递给`scatter()`方法。我们还使用`c`参数指定数据点的颜色，`s`参数指定数据点的大小，以及`alpha`参数指定数据点的透明度。
