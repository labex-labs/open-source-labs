# 创建图形

要创建图形，我们首先需要定义要绘制的数据。在这个例子中，我们将使用 `numpy` 库来生成一些示例数据。

```python
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)
```

接下来，我们使用 `plt.subplots()` 创建一个新的图形和坐标轴。我们将设置图形的 x 轴和 y 轴范围，然后使用 `plot()` 绘制数据。

```python
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-1.2, 1.2])
ax.plot(x, y)
```
