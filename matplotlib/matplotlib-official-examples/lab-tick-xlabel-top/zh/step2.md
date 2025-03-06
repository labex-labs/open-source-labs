# 使用默认设置创建基本图表

既然你已经导入了 Matplotlib，那么让我们使用默认设置创建一个简单的图表，以了解默认情况下坐标轴和刻度标签的位置。

## 了解 Matplotlib 组件

在 Matplotlib 中，图表由多个组件组成：

- **Figure（图形）**：图表的整体容器
- **Axes（坐标轴）**：使用自身坐标系绘制数据的区域
- **Axis（轴）**：定义坐标系的类似数轴的对象
- **Ticks（刻度）**：坐标轴上表示特定值的标记
- **Tick Labels（刻度标签）**：指示每个刻度处数值的文本标签

默认情况下，x 轴刻度标签显示在图表的底部。

## 创建简单图表

在 Notebook 的新单元格中，让我们创建一个简单的折线图：

```python
# Create a figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.sin(x)

# Plot the data
ax.plot(x, y, marker='o', linestyle='-', color='blue', label='sin(x)')

# Add a title and labels
ax.set_title('A Simple Sine Wave Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis (sin(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Notice that the x-axis tick labels are at the bottom of the plot by default.")
```

运行此代码时，你将看到一个正弦波图表，x 轴刻度标签位于图表底部，这是 Matplotlib 中的默认位置。

花点时间观察图表的结构以及刻度标签的位置。这种理解将有助于你理解下一步所做的更改。
