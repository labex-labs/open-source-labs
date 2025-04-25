# 保存并分享你的图表

最后一步是保存你自定义的图表，这样你就可以将其包含在报告、演示文稿中，或者与他人分享。

## 以不同格式保存图表

Matplotlib 允许你以多种格式保存图表，包括 PNG、JPG、PDF、SVG 等。让我们学习如何以不同格式保存图表：

```python
# Create a plot similar to our previous customized one
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the data
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False
)

# Customize tick labels
ax.set_xticks(np.arange(0, 2*np.pi + 0.1, np.pi/2))
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Add title and labels
ax.set_title('Plot with X-Axis Labels at the Top', fontsize=14)
ax.set_xlabel('X-axis at the top')
ax.set_ylabel('Y-axis')

# Add grid and legend
ax.grid(True)
ax.legend()

# Save the figure in different formats
plt.savefig('plot_with_top_xlabels.png', dpi=300, bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.pdf', bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.svg', bbox_inches='tight')

# Show the plot
plt.show()

print("The plot has been saved in PNG, PDF, and SVG formats in the current directory.")
```

运行此代码时，图表将以三种不同格式保存：

- PNG：一种光栅图像格式，适用于网页和一般用途
- PDF：一种矢量格式，非常适合出版物和报告
- SVG：一种矢量格式，非常适合网页和可编辑图形

这些文件将保存在你的 Jupyter 笔记本的当前工作目录中。

## 理解保存参数

让我们来看看 `savefig()` 使用的参数：

- `dpi=300`：为 PNG 等光栅格式设置分辨率（每英寸点数）
- `bbox_inches='tight'`：自动调整图形边界，以包含所有元素，且无多余空白

## 查看保存的文件

你可以通过导航到 Jupyter 的文件浏览器来查看保存的文件：

1. 点击左上角的“Jupyter”徽标
2. 在文件浏览器中，你应该能看到保存的图像文件
3. 点击任何文件即可查看或下载

## 其他图表导出选项

为了更精确地控制保存的图表，你可以根据需要自定义图形大小、调整背景或更改 DPI：

```python
# Control the background color and transparency
fig.patch.set_facecolor('white')  # Set figure background color
fig.patch.set_alpha(0.8)          # Set background transparency

# Save with custom settings
plt.savefig('custom_background_plot.png',
            dpi=400,              # Higher resolution
            facecolor=fig.get_facecolor(),  # Use the figure's background color
            edgecolor='none',     # No edge color
            bbox_inches='tight',  # Tight layout
            pad_inches=0.1)       # Add a small padding

print("A customized plot has been saved with specialized export settings.")
```

这展示了如何精确控制输出格式和外观来保存图表。
