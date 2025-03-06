# 进一步自定义图表

既然你已经将 x 轴刻度标签移到了顶部，那么让我们进一步自定义图表，使其更具视觉吸引力和信息性。

## 高级图表自定义技巧

Matplotlib 提供了众多自定义图表的选项。让我们来探索其中一些选项：

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate some data with more points for a smoother curve
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot multiple datasets
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Fill the area between curves
ax.fill_between(x, y1, y2, where=(y1 > y2), alpha=0.3, color='green', interpolate=True)
ax.fill_between(x, y1, y2, where=(y1 <= y2), alpha=0.3, color='purple', interpolate=True)

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False
)

# Customize tick labels
ax.set_xticks(np.arange(0, 2*np.pi + 0.1, np.pi/2))
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Add title and labels with custom styles
ax.set_title('Sine and Cosine Functions with Customized X-Axis Labels at the Top',
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Angle (radians)', fontsize=12)
ax.set_ylabel('Function Value', fontsize=12)

# Add a grid and customize its appearance
ax.grid(True, linestyle='--', alpha=0.7, which='both')

# Customize the axis limits
ax.set_ylim(-1.2, 1.2)

# Add a legend with custom location and style
ax.legend(loc='upper right', fontsize=12, framealpha=0.8)

# Add annotations to highlight important points
ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=10, ha='center')

# Display the plot
plt.tight_layout()  # Adjust spacing for better appearance
plt.show()

print("We have created a fully customized plot with x-axis tick labels at the top!")
```

运行此代码时，你将看到一个更加精致、专业的图表，它具有以下特点：

- 两条曲线（正弦和余弦）
- 曲线之间的彩色区域
- 自定义刻度标签（使用 π 符号）
- 指向关键特征的注释
- 更好的间距和样式

注意，你使用 `tick_params()` 方法将 x 轴刻度标签保持在顶部，同时通过额外的自定义增强了图表的效果。

## 理解自定义设置

让我们详细分析一下添加的一些关键自定义设置：

1. `fill_between()`：在正弦和余弦曲线之间创建彩色区域
2. `set_xticks()` 和 `set_xticklabels()`：自定义刻度位置和标签
3. `tight_layout()`：自动调整图表间距，以获得更好的外观
4. `annotate()`：添加带有箭头指向特定点的文本
5. 对各种元素进行字体、颜色和样式的自定义

这些自定义设置展示了你如何在将 x 轴刻度标签保持在顶部的同时，创建出具有视觉吸引力和信息性的图表。
