# 创建基本直方图

现在我们已经有了数据，让我们创建一个直方图来可视化其分布。直方图将数据划分为区间（范围），并显示每个区间内数据点的频率。

## 创建直方图

在你的 Jupyter Notebook 的一个新单元格中，输入并运行以下代码：

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
```

当你运行这个单元格时，你应该会看到一个显示随机数据分布的直方图。输出看起来会是一个以零为中心的钟形曲线（正态分布）。

## 理解代码

让我们来详细分析代码中每一行的作用：

1. `fig, ax = plt.subplots(figsize=(10, 6))`：创建一个图形和坐标轴对象。`figsize` 参数以英寸为单位设置图形的大小（宽度、高度）。
2. `histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')`：为我们的数据 `x` 创建一个包含 50 个区间的直方图。区间颜色为天蓝色，边缘为黑色。
3. `ax.set_title('Distribution of Random Data', fontsize=16)`：为图形添加一个字号为 16 的标题。
4. `ax.set_xlabel('Value', fontsize=12)` 和 `ax.set_ylabel('Frequency', fontsize=12)`：为 x 轴和 y 轴添加字号为 12 的标签。
5. `plt.tight_layout()`：自动调整图形以适应图形区域。
6. `plt.show()`：显示图形。

直方图展示了我们的数据是如何分布的。由于我们使用了 `np.random.randn()` 来生成来自正态分布的数据，所以直方图呈现出以 0 为中心的钟形。每个条形的高度代表了落在该区间内的数据点数量。
