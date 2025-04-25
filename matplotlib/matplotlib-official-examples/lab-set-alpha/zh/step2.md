# 创建具有统一 Alpha 值的条形图

在这一步中，我们将使用 `alpha` 关键字参数创建一个条形图，其中所有条形都具有相同的透明度级别。

## 添加新单元格

通过点击工具栏中的“+”按钮，或者在命令模式下按“Esc”然后按“b”，在你的 Jupyter Notebook 中添加一个新单元格。

## 创建具有统一 Alpha 值的条形图

在新单元格中输入并运行以下代码：

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Create the bar chart with alpha=0.5 for all bars
ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)

# Add a title and labels
ax.set_title("Bar Chart with Uniform Alpha Value (alpha=0.5)")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## 理解代码和输出

运行代码后，你应该会看到一个包含 20 个条形的条形图。每个条形要么是绿色（y 值为正），要么是红色（y 值为负），并且具有相同的透明度级别（alpha=0.5）。

让我们来分析一下关键部分：

1. `np.random.seed(19680801)` —— 这确保了你每次运行代码时生成的随机数都是相同的。
2. `x_values = list(range(20))` —— 创建一个从 0 到 19 的整数列表，用于 x 轴。
3. `y_values = np.random.randn(20)` —— 从标准正态分布中生成 20 个随机值，用于 y 轴。
4. `facecolors = ['green' if y > 0 else 'red' for y in y_values]` —— 这个列表推导式将正值设为绿色，负值设为红色。
5. `ax.bar(..., alpha=0.5)` —— 这是为所有条形设置统一 alpha 值 0.5 的关键部分。

统一的 alpha 值使所有条形具有相同的透明度，当你想要实现以下目的时，这会很有用：

- 透过条形显示背景网格线
- 创建更柔和的可视化效果
- 同等程度地减少所有元素的视觉主导性

在下一步中，我们将探索如何为不同的条形设置不同的 alpha 值。
