# 创建并配置断轴图

在这一步中，我们将创建实际的断轴图（broken axis plot）结构。断轴图由多个子图组成，用于展示同一数据的不同范围。我们将对这些子图进行配置，以有效地展示主要数据和离群值。

## 创建子图

首先，我们需要创建两个垂直排列的子图。上方的子图将展示离群值，而下方的子图将展示大部分数据点。

在你的 Notebook 中创建一个新的单元格，并添加以下代码：

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Add a main title to the figure
fig.suptitle('Broken Axis Plot Example', fontsize=16)

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Display the figure to see both subplots
plt.tight_layout()
plt.show()
```

![broken-axis-plot](../assets/screenshot-20250306-cawcMZv3@2x.png)

运行此单元格时，你应该会看到一个包含两个子图的图形，两个子图都展示了相同的数据。注意，离群值如何压缩了两个图中其余的数据，使得很难看清大部分数据点的细节。这正是我们试图用断轴图解决的问题。

## 配置 Y 轴范围

现在，我们需要对每个子图进行配置，使其专注于特定的 y 值范围。上方的子图将专注于离群值范围，而下方的子图将专注于主要数据范围。

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

# Add a title to each subplot
ax1.set_title('Outlier Region')
ax2.set_title('Main Data Region')

# Display the figure with adjusted y-axis limits
plt.tight_layout()
plt.show()
```

运行此单元格时，你应该会看到每个子图现在都专注于不同的 y 值范围。上方的图仅展示离群值，下方的图仅展示主要数据。这已经改善了可视化效果，但要使其成为一个合适的断轴图，我们还需要进行一些额外的配置。

## 隐藏边框并调整刻度

为了营造出“断开”坐标轴的效果，我们需要隐藏两个子图之间相连的边框，并调整刻度的位置。

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

# Add labels to the plot
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')

plt.tight_layout()
plt.show()
```

运行此单元格时，你应该会看到图中两个子图之间的边框已被隐藏，外观更加简洁。x 轴刻度现在位置正确，标签仅显示在底部。

此时，我们已经成功创建了一个基本的断轴图。在下一步中，我们将添加一些修饰，让观看者清楚地知道坐标轴是断开的。
