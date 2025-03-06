# 创建可重复使用的图像叠加函数

为了让我们的代码更具可复用性，我们来创建一个函数，它可以将图像叠加到任何 Matplotlib 图形上。这样，我们就能轻松地将相同的效果应用到不同的绘图中。

1. 在你的 Notebook 中创建一个新单元格，并输入以下代码：

```python
def add_image_overlay(fig, image_path, x_pos=25, y_pos=25, alpha=0.5, zorder=3):
    """
    Add an image overlay to a matplotlib figure.

    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure to add the image to
    image_path : str
        Path to the image file
    x_pos : int
        X position in pixels from the bottom left
    y_pos : int
        Y position in pixels from the bottom left
    alpha : float
        Transparency level (0 to 1)
    zorder : int
        Drawing order (higher numbers are drawn on top)

    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure with the image overlay
    """
    # Load the image
    with cbook.get_sample_data(image_path) as file:
        im = image.imread(file)

    # Add the image to the figure
    fig.figimage(im, x_pos, y_pos, zorder=zorder, alpha=alpha)

    return fig

# Example usage: Create a scatter plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data for a scatter plot
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10

# Create a scatter plot
ax.scatter(x, y, s=100, c=np.random.rand(50), cmap='viridis', alpha=0.7)
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Scatter Plot with Image Overlay')

# Add the image overlay using our function
add_image_overlay(fig, 'logo2.png', x_pos=50, y_pos=50, alpha=0.4)

# Display the plot
plt.tight_layout()
plt.show()
```

这段代码定义了一个名为 `add_image_overlay` 的函数，它的功能如下：

- 接收图形、图像路径、位置、透明度和 z 顺序等参数。
- 加载指定的图像。
- 使用 `figimage` 将图像添加到图形中。
- 返回修改后的图形。

定义完函数后，我们通过创建一个带有随机数据的散点图，并将 Matplotlib 徽标作为叠加层添加到图中，来演示该函数的使用方法。

2. 按下 Shift + Enter 运行该单元格。

输出结果应显示一个散点图，其中的点随机分布且颜色各异，Matplotlib 徽标以 40% 的不透明度叠加在位置 (50, 50) 处。

3. 让我们再尝试一个折线图的示例。创建一个新单元格并输入以下代码：

```python
# Example usage: Create a line plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data for a line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
ax.plot(x, y, linewidth=2, color='#d62728')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Sine Wave with Image Overlay')
ax.set_ylim(-1.5, 1.5)

# Add the image overlay using our function
# Place it in the bottom right corner
fig_width, fig_height = fig.get_size_inches() * fig.dpi
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
    x_pos = fig_width - im.shape[1] - 50  # 50 pixels from the right edge

add_image_overlay(fig, 'logo2.png', x_pos=x_pos, y_pos=50, alpha=0.6)

# Display the plot
plt.tight_layout()
plt.show()
```

这段代码创建了一个显示正弦波的折线图，并将 Matplotlib 徽标添加到绘图的右下角。

4. 按下 Shift + Enter 运行该单元格。

输出结果应显示一个正弦波的折线图，Matplotlib 徽标以 60% 的不透明度叠加在右下角。

这些示例展示了我们的 `add_image_overlay` 函数如何轻松地将图像叠加到不同类型的绘图中，使其成为自定义可视化效果的通用工具。
