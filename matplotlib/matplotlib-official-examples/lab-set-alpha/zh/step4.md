# 创建带有 Alpha 值的散点图

在这一步中，我们将运用对 alpha 值的了解来创建一个散点图。这将展示透明度如何有助于在存在重叠点的散点图中可视化数据密度。

## 添加新单元格

通过点击工具栏中的 “+” 按钮，或者在命令模式下按 “Esc” 然后按 “b”，在你的 Jupyter Notebook 中添加一个新单元格。

## 创建带有透明度的散点图

在新单元格中输入并运行以下代码：

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create two clusters of points
cluster1_x = np.random.normal(0.3, 0.15, 500)
cluster1_y = np.random.normal(0.3, 0.15, 500)

cluster2_x = np.random.normal(0.7, 0.15, 500)
cluster2_y = np.random.normal(0.7, 0.15, 500)

# Combine the clusters
x = np.concatenate([cluster1_x, cluster2_x])
y = np.concatenate([cluster1_y, cluster2_y])

# Create a scatter plot with alpha=0.5
scatter = ax.scatter(x, y, s=30, c='blue', alpha=0.5)

# Add a title and labels
ax.set_title("Scatter Plot with Alpha=0.5 Showing Data Density")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## 理解代码和输出

运行代码后，你应该会看到一个包含两个点簇的散点图。每个点的透明度级别为 0.5，这使你能够看到点的重叠位置。

让我们来分析一下代码的关键部分：

1. `cluster1_x = np.random.normal(0.3, 0.15, 500)` —— 生成 500 个遵循正态分布的随机 x 坐标，均值为 0.3，标准差为 0.15。
2. `cluster1_y = np.random.normal(0.3, 0.15, 500)` —— 为第一个点簇生成 500 个随机 y 坐标。
3. `cluster2_x` 和 `cluster2_y` —— 同样为以 (0.7, 0.7) 为中心的第二个点簇生成坐标。
4. `ax.scatter(..., alpha=0.5)` —— 创建一个点的不透明度为 50% 的散点图。

在散点图中使用 alpha 的好处包括：

1. **密度可视化**：许多点重叠的区域看起来更暗，从而揭示数据密度。
2. **减少重叠绘图**：如果没有透明度，重叠的点会完全相互遮挡。
3. **模式识别**：透明度有助于识别数据中的点簇和模式。

注意在可视化中，点重叠较多的区域是如何显得更暗的。这是一种无需使用密度估计等额外技术就能可视化数据密度的有效方法。
