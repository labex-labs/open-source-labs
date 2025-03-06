# 为断轴图添加最后的修饰

在这最后一步，我们将为断轴图（broken axis plot）添加最后的修饰，以明确显示 y 轴是断开的。我们会在子图之间添加对角线来表示断点，并通过合适的标签和网格线来提升图表的整体外观。

## 添加对角断线

为了直观地表明坐标轴是断开的，我们将在两个子图之间添加对角线。这是一种常见的做法，有助于观看者理解坐标轴的某些部分被省略了。

创建一个新的单元格并添加以下代码：

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

运行此单元格时，你应该会看到完整的断轴图，其中对角线表示 y 轴的断点。图表现在有了标题、坐标轴标签和网格线，以提高可读性。

## 理解断轴图

让我们花点时间来理解断轴图的关键组成部分：

1. **两个子图**：我们创建了两个独立的子图，每个子图专注于不同的 y 值范围。
2. **隐藏边框**：我们隐藏了子图之间相连的边框，以形成视觉上的分隔。
3. **对角断线**：我们添加了对角线来表示坐标轴是断开的。
4. **Y 轴范围**：我们为每个子图设置了不同的 y 轴范围，以专注于数据的特定部分。
5. **网格线**：我们添加了网格线，以提高可读性并便于估算数值。

当你的数据中存在离群值，否则会压缩大部分数据点的可视化效果时，这种技术特别有用。通过“断开”坐标轴，你可以在一个图表中清晰地展示离群值和主要数据分布。

## 对图表进行实验

现在你已经了解了如何创建断轴图，你可以尝试不同的配置。尝试更改 y 轴范围、为图表添加更多功能，或者将此技术应用到你自己的数据上。

例如，你可以修改之前的代码，以包含图例、更改配色方案或调整标记样式：

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes with different styles
ax1.plot(pts, 'o-', color='darkblue', label='Data Points', linewidth=2)
ax2.plot(pts, 'o-', color='darkblue', linewidth=2)

# Mark the outliers with a different color
outlier_indices = [3, 14]
ax1.plot(outlier_indices, pts[outlier_indices], 'ro', markersize=8, label='Outliers')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers - Enhanced Visualization', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

# Add a legend to the top subplot
ax1.legend(loc='upper right')

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

运行这段增强后的代码时，你应该会看到一个改进后的可视化图表，其中离群值被特别标记出来，并且有一个图例解释数据点。

恭喜！你已经使用 Matplotlib 在 Python 中成功创建了一个断轴图。当处理包含离群值的数据时，这种技术将帮助你创建更有效的可视化图表。
