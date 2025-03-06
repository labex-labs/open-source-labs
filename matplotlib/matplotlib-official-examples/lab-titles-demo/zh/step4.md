# 使用子图进行高级标题定位

在这一步中，你将学习在使用子图布局和轴对象时进行标题定位的高级技巧。你还将学习如何使用 `suptitle()` 函数为包含多个子图的图形添加一个整体标题。

## 创建带有子图和独立标题的图形

让我们创建一个 2x2 的子图网格，每个子图的标题位置都不同：

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data and set titles with different positions for each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)

# Top-left subplot: Default centered title
axes[0].set_title('Default (Centered)')

# Top-right subplot: Left-aligned title
axes[1].set_title('Left-Aligned', loc='left')

# Bottom-left subplot: Right-aligned title
axes[2].set_title('Right-Aligned', loc='right')

# Bottom-right subplot: Custom positioned title
axes[3].set_title('Custom Position', y=0.85, loc='center')

# Add spacing between subplots
plt.tight_layout()
plt.show()
```

运行该单元格。你应该会看到四个子图，每个子图的标题位置都不同。

## 使用 `suptitle()` 添加图形级别的标题

在处理多个子图时，你可能想要为整个图形添加一个整体标题。这可以使用 `suptitle()` 函数来完成：

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1}')

# Add an overall title to the figure
fig.suptitle('Multiple Subplots with an Overall Title', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

运行该单元格。你应该会看到四个子图，每个子图都有自己的标题，并且图形顶部有一个整体标题。

## 结合轴标题和图形标题

你可以将各个子图的标题与图形的整体标题结合起来：

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot data on each subplot with different title positions
axes[0, 0].plot(range(10))
axes[0, 0].grid(True)
axes[0, 0].set_title('Centered Title', loc='center')

axes[0, 1].plot(range(10))
axes[0, 1].grid(True)
axes[0, 1].set_title('Left-Aligned Title', loc='left')

axes[1, 0].plot(range(10))
axes[1, 0].grid(True)
axes[1, 0].set_title('Right-Aligned Title', loc='right')

axes[1, 1].plot(range(10))
axes[1, 1].grid(True)
axes[1, 1].set_title('Lower Title', y=0.85)

# Add an overall title to the figure
fig.suptitle('Advanced Title Positioning Demo', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

运行该单元格。你应该会看到一个包含四个子图的图形，每个子图的标题位置都不同，并且图形顶部有一个整体标题。

`suptitle()` 函数对于添加描述整个图形的主标题很有用，而在轴对象上单独调用 `set_title()` 则可以为每个子图添加更具体的标题。
