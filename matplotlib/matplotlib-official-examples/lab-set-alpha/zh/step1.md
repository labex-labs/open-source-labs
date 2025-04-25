# 理解 Matplotlib 中的 Alpha 值

在第一步中，我们将创建一个 Jupyter Notebook，并学习如何使用 alpha 值设置基本的可视化图表。

## 创建你的第一个 Jupyter Notebook 单元格

在这个单元格中，我们将导入必要的库，并创建两个具有不同 alpha 值的重叠圆形，以演示透明度。

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(6, 4))

# Create a circle with alpha=1.0 (completely opaque)
circle1 = plt.Circle((0.5, 0.5), 0.3, color='blue', alpha=1.0, label='Opaque (alpha=1.0)')

# Create a circle with alpha=0.5 (semi-transparent)
circle2 = plt.Circle((0.7, 0.5), 0.3, color='red', alpha=0.5, label='Semi-transparent (alpha=0.5)')

# Add circles to the axes
ax.add_patch(circle1)
ax.add_patch(circle2)

# Set axis limits
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1)

# Add a title and legend
ax.set_title('Demonstrating Alpha Values in Matplotlib')
ax.legend(loc='upper right')

# Show the plot
plt.show()
```

在单元格中输入此代码后，按下 Shift+Enter 或点击工具栏中的“Run”按钮来运行它。

## 理解输出结果

你应该会看到两个重叠的圆形：

- 左边的蓝色圆形是完全不透明的（alpha=1.0）
- 右边的红色圆形是半透明的（alpha=0.5）

注意在两个圆形重叠的部分，你可以透过红色圆形看到蓝色圆形。这就是将红色圆形的 alpha 值设置为 0.5 所产生的效果。

Alpha 值可以控制可视化图表中的透明度，在以下情况下会很有帮助：

- 展示重叠的数据点
- 突出显示某些元素
- 减少密集图表中的视觉干扰
- 创建分层的可视化图表

让我们在下一步中继续探索 alpha 值的更多应用。
