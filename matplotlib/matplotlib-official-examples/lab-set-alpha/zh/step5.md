# 使用不同 Alpha 技术创建组合可视化图表

在这最后一步中，我们将结合多种技术，创建一个更复杂的可视化图表，在一个图中同时展示统一和不同的 Alpha 值。

## 添加新单元格

通过点击工具栏中的 “+” 按钮，或者在命令模式下按 “Esc” 然后按 “b”，在你的 Jupyter Notebook 中添加一个新单元格。

## 创建组合可视化图表

在新单元格中输入并运行以下代码：

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Generate some common data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# First subplot: Fixed alpha for all lines
ax1.plot(x, y1, color='red', linewidth=2, label='sin(x)', alpha=0.7)
ax1.plot(x, y2, color='blue', linewidth=2, label='cos(x)', alpha=0.7)
ax1.plot(x, y3, color='green', linewidth=2, label='sin(x)cos(x)', alpha=0.7)

# Add title and legend to first subplot
ax1.set_title("Multiple Lines with Uniform Alpha")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Scatter plot with varying alpha based on y-value
sizes = np.abs(y3 * 100) + 10  # Vary point sizes based on y3
colors = y3  # Use y3 values for coloring

# Calculate varying alpha values between 0.3 and 1.0 based on absolute y3 values
alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))

# Create a scatter plot with varying sizes, colors, and alphas
scatter = ax2.scatter(x, y3, s=sizes, c=colors, cmap='viridis',
                     alpha=alphas)

# Add title and labels to second subplot
ax2.set_title("Scatter Plot with Varying Alpha Based on Y-Value")
ax2.set_xlabel("x")
ax2.set_ylabel("sin(x)cos(x)")
ax2.grid(True, linestyle='--', alpha=0.5)

# Add a colorbar to the second subplot
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Value of sin(x)cos(x)')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
```

## 理解代码和输出

运行代码后，你应该会看到一个包含两个并排子图的图表：

1. **左子图（统一 Alpha）**：展示了以相同 Alpha 值（0.7）绘制的三个三角函数。
2. **右子图（不同 Alpha）**：展示了一个散点图，其中：
   - x 坐标是输入值
   - y 坐标是 sin(x)cos(x)
   - 每个点的大小根据 y 值的绝对值而变化
   - 每个点的颜色根据 y 值而变化
   - 每个点的 Alpha（透明度）根据 y 值的绝对值而变化

让我们分析一下代码的关键部分：

1. `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))` —— 创建一个包含两个并排子图的图表。
2. 对于第一个子图：
   - `ax1.plot(..., alpha=0.7)` —— 对所有三条线使用统一的 Alpha 值。
3. 对于第二个子图：
   - `alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))` —— 计算介于 0.3 和 1.0 之间的不同 Alpha 值。
   - `ax2.scatter(..., alpha=alphas)` —— 对散点使用不同的 Alpha 值。

这种技术组合展示了如何以各种方式使用 Alpha 值来增强可视化效果：

- **统一 Alpha** 在你需要展示多个具有同等重要性的重叠元素时很有帮助。
- **不同 Alpha** 在你想根据数据点的值强调某些数据点时很有用。

通过掌握这些技术，你可以创建更有效且视觉上更吸引人的数据可视化图表。
