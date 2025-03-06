# 自定义标题垂直位置

有时你可能想要调整标题的垂直位置。在这一步中，你将学习如何手动控制图表标题的垂直（y 轴）位置。

## 理解标题的 Y 轴位置

标题的垂直位置可以使用 `title()` 函数中的 `y` 参数进行调整。`y` 参数接受归一化坐标值，其中：

- `y = 1.0`（默认值）将标题置于图表顶部。
- `y > 1.0` 将标题置于图表顶部上方。
- `y < 1.0` 将标题置于图表顶部下方，使其更靠近图表内容。

## 创建具有自定义标题 Y 轴位置的图表

让我们创建一个标题位置比默认位置更高的图表。在一个新的单元格中，输入以下代码：

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Higher Title Position', y=1.1)  # Position the title higher
plt.show()
```

运行该单元格。注意，与默认位置相比，标题现在出现在图表上方稍高的位置。

现在，让我们创建一个标题位置比默认位置更低的图表：

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Lower Title Position', y=0.9)  # Position the title lower
plt.show()
```

运行该单元格。标题现在应该更靠近图表内容。

## 比较不同的 Y 轴位置

让我们并排创建多个图表，以比较不同的标题垂直位置：

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Default Y-position
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Default Position (y=1.0)')

# Plot 2: Higher Y-position
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Higher Position', y=1.15)

# Plot 3: Lower Y-position
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Lower Position', y=0.85)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

运行该单元格，你将看到三种垂直位置并排显示。这种比较有助于你理解 `y` 参数如何影响标题的垂直位置。

## 结合水平和垂直定位

你可以将 `loc` 参数（用于水平对齐）与 `y` 参数（用于垂直位置）结合使用，将标题精确地放置在你想要的位置：

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Custom Positioned Title', loc='right', y=1.1)  # Right-aligned and higher
plt.show()
```

运行该单元格。标题现在应该与图表的右边缘对齐，并且位置比默认位置更高。
