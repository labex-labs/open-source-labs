# 将 X 轴刻度标签移至顶部

既然你已经了解了刻度标签的默认位置，那么让我们把 x 轴刻度标签移到图表的顶部。

## 了解刻度参数

Matplotlib 提供了 `tick_params()` 方法来控制刻度和刻度标签的外观。该方法允许你：

- 显示/隐藏刻度和刻度标签
- 更改它们的位置（顶部、底部、左侧、右侧）
- 调整它们的大小、颜色和其他属性

## 创建 X 轴刻度标签位于顶部的图表

让我们创建一个新的图表，将 x 轴刻度标签移到顶部：

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.cos(x)

# Plot the data
ax.plot(x, y, marker='s', linestyle='-', color='green', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',         # Apply changes to the x-axis
    top=True,         # Show ticks on the top side
    labeltop=True,    # Show tick labels on the top side
    bottom=False,     # Hide ticks on the bottom side
    labelbottom=False # Hide tick labels on the bottom side
)

# Add a title and labels
ax.set_title('Cosine Wave with X-Axis Tick Labels at the Top')
ax.set_xlabel('X-axis (now at the top!)')
ax.set_ylabel('Y-axis (cos(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Now the x-axis tick labels are at the top of the plot!")
```

运行此代码时，你将看到一个余弦波图表，x 轴刻度标签位于图表的顶部。

注意 `tick_params()` 方法是如何使用多个参数的：

- `axis='x'`：指定要修改 x 轴
- `top=True` 和 `labeltop=True`：使顶部的刻度和标签可见
- `bottom=False` 和 `labelbottom=False`：隐藏底部的刻度和标签

这样，你就能清晰地看到数据，并且 x 轴标签位于顶部而非底部。
