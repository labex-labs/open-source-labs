# 使用随机数据创建基本绘图

在添加图像叠加层之前，我们需要创建一个绘图，作为可视化的基础。让我们使用随机数据创建一个简单的条形图。

1. 在你的 Notebook 中创建一个新单元格，并输入以下代码：

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Random Data')

# Display the plot
plt.tight_layout()
plt.show()
```

这段代码的功能如下：

- 使用 `plt.subplots()` 创建一个具有特定大小的图形和坐标轴。
- 设置随机种子，以确保每次运行代码时都能得到相同的随机值。
- 生成 30 个 x 值（从 0 到 29）以及对应的 y 值（x 加上随机噪声）。
- 使用 `ax.bar()` 创建一个绿色条形图。
- 使用 `ax.grid()` 为绘图添加网格线。
- 为 x 轴、y 轴添加标签，并为绘图添加标题。
- 使用 `plt.tight_layout()` 调整间距，使外观更美观。
- 使用 `plt.show()` 显示绘图。

2. 按下 Shift + Enter 运行该单元格。

输出结果应显示一个绿色条形图，代表随机数据。x 轴显示从 0 到 29 的整数，y 轴显示加上随机噪声后的对应值。

这个绘图将作为下一步叠加图像的基础。注意，我们将图形对象存储在变量 `fig` 中，将坐标轴对象存储在变量 `ax` 中。我们需要这些变量来添加图像叠加层。
