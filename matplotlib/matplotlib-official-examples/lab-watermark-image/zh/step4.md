# 在绘图上叠加图像

既然我们已经创建了基础绘图，接下来就让我们将图像叠加到上面。我们将使用 `figimage` 方法把图像添加到图形中，并使其具有半透明效果，这样下方的绘图仍然可见。

1. 在你的 Notebook 中创建一个新单元格，并输入以下代码：

```python
# Create a figure and axes for our plot (same as before)
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
ax.set_title('Bar Chart with Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Overlay the image on the plot
# Parameters:
# - im: the image data
# - 25, 25: x and y position in pixels from the bottom left
# - zorder=3: controls the drawing order (higher numbers are drawn on top)
# - alpha=0.5: controls the transparency (0 = transparent, 1 = opaque)
fig.figimage(im, 25, 25, zorder=3, alpha=0.5)

# Display the plot
plt.tight_layout()
plt.show()
```

这段代码结合了我们之前的操作，并添加了 `figimage` 方法，将图像叠加到绘图上。以下是 `figimage` 参数的详细解释：

- `im`：以 NumPy 数组形式存在的图像数据。
- `25, 25`：从图形左下角开始计算的像素 x 和 y 坐标。
- `zorder=3`：控制绘制顺序。数值越大，元素越会绘制在数值较小的元素之上。
- `alpha=0.5`：控制图像的透明度。值为 0 表示完全透明，值为 1 表示完全不透明。

2. 按下 Shift + Enter 运行该单元格。

输出结果应显示与之前相同的条形图，但现在 Matplotlib 徽标会叠加在左下角。徽标应该是半透明的，这样下方的绘图仍然可见。

3. 让我们尝试不同的位置和透明度级别。创建一个新单元格并输入以下代码：

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)
y = x + np.random.randn(30)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Centered Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Get figure dimensions
fig_width, fig_height = fig.get_size_inches() * fig.dpi

# Calculate center position (this is approximate)
x_center = fig_width / 2 - im.shape[1] / 2
y_center = fig_height / 2 - im.shape[0] / 2

# Overlay the image at the center with higher transparency
fig.figimage(im, x_center, y_center, zorder=3, alpha=0.3)

# Display the plot
plt.tight_layout()
plt.show()
```

这段代码将图像放置在图形的中心，并设置了更高的透明度级别（alpha=0.3），使其更适合作为水印。

4. 按下 Shift + Enter 运行该单元格。

输出结果应显示条形图，徽标位于中心位置，并且比之前更透明，从而产生水印效果。
