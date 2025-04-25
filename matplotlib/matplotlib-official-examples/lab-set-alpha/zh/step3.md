# 创建具有不同 Alpha 值的条形图

在这一步中，我们将使用 `(matplotlib_color, alpha)` 元组格式，根据每个条形的数据值为其分配不同的透明度级别。

## 添加新单元格

通过点击工具栏中的“+”按钮，或者在命令模式下按“Esc”然后按“b”，在你的 Jupyter Notebook 中添加一个新单元格。

## 创建具有不同 Alpha 值的条形图

在新单元格中输入并运行以下代码：

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data (using the same data as in Step 2 for comparison)
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Calculate alpha values based on the absolute y-values
# Normalize y values to get alpha values between 0.2 and 1.0
abs_y = [abs(y) for y in y_values]
max_abs_y = max(abs_y)
face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]

# Create color-alpha tuples for each bar
colors_with_alphas = list(zip(facecolors, face_alphas))

# Create the bar chart with varying alpha values
ax.bar(x_values, y_values, color=colors_with_alphas, edgecolor=edgecolors)

# Add a title and labels
ax.set_title("Bar Chart with Varying Alpha Values Based on Bar Height")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## 理解代码和输出

运行代码后，你应该会看到一个包含 20 个条形的条形图。每个条形的透明度级别与其 y 值的绝对值成正比 —— 较高的条形更不透明，较短的条形更透明。

让我们来分析一下代码的关键部分：

1. `abs_y = [abs(y) for y in y_values]` —— 这会创建一个包含所有 y 值绝对值的列表。
2. `max_abs_y = max(abs_y)` —— 找到最大的绝对值，以便对数据进行归一化处理。
3. `face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]` —— 根据归一化后的 y 值绝对值，计算出介于 0.2 和 1.0 之间的 alpha 值。
4. `colors_with_alphas = list(zip(facecolors, face_alphas))` —— 通过将每种颜色与其对应的 alpha 值配对，创建一个 `(颜色, alpha)` 元组列表。
5. `ax.bar(..., color=colors_with_alphas, ...)` —— 使用 `(颜色, alpha)` 元组为每个条形设置不同的 alpha 值。

这种使用不同透明度级别的方法在以下方面非常有效：

- 强调更重要的数据点
- 弱化不太重要的数据点
- 根据数据值创建视觉层次结构
- 为你的可视化图表添加额外的信息维度

你可以清楚地看到，不同的 alpha 值如何产生一种视觉效果，即数据点的大小不仅通过条形的高度，还通过其不透明度得到强调。
