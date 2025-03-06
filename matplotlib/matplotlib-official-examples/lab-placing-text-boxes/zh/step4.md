# 自定义文本框

既然我们已经成功地在绘图中添加了文本框，那么让我们探索各种自定义选项，使它在视觉上更具吸引力，并适用于不同的场景。

## 尝试不同的样式

让我们创建一个函数，以便更轻松地尝试不同的文本框样式。在一个新的单元格中，输入并运行以下代码：

```python
def plot_with_textbox(boxstyle, facecolor, alpha, position=(0.05, 0.95)):
    """
    Create a histogram with a custom text box.

    Parameters:
    boxstyle (str): Style of the box ('round', 'square', 'round4', etc.)
    facecolor (str): Background color of the box
    alpha (float): Transparency of the box (0-1)
    position (tuple): Position of the box in axes coordinates (x, y)
    """
    # Create figure and plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title and labels
    ax.set_title(f'Text Box Style: {boxstyle}', fontsize=16)
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)

    # Create text box properties
    box_props = dict(boxstyle=boxstyle, facecolor=facecolor, alpha=alpha)

    # Add text box
    ax.text(position[0], position[1], textstr, transform=ax.transAxes,
            fontsize=14, verticalalignment='top', bbox=box_props)

    plt.tight_layout()
    plt.show()
```

现在，让我们使用这个函数来尝试不同的文本框样式。在一个新的单元格中，输入并运行：

```python
# Try a square box with light green color
plot_with_textbox('square', 'lightgreen', 0.7)

# Try a rounded box with light blue color
plot_with_textbox('round', 'lightblue', 0.5)

# Try a box with extra rounded corners
plot_with_textbox('round4', 'lightyellow', 0.6)

# Try a sawtooth style box
plot_with_textbox('sawtooth', 'lightcoral', 0.4)
```

当你运行这个单元格时，你会看到四个不同的绘图，每个绘图都有不同样式的文本框。

## 更改文本框的位置

文本框的位置对于可视化效果至关重要。让我们将文本框放置在绘图的不同角落。在一个新的单元格中，输入并运行：

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()  # Flatten to easily iterate

# Define positions for the four corners
positions = [
    (0.05, 0.95),  # Top left
    (0.95, 0.95),  # Top right
    (0.05, 0.05),  # Bottom left
    (0.95, 0.05)   # Bottom right
]

# Define alignments for each position
alignments = [
    ('top', 'left'),          # Top left
    ('top', 'right'),         # Top right
    ('bottom', 'left'),       # Bottom left
    ('bottom', 'right')       # Bottom right
]

# Corner labels
corner_labels = ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']

# Create four plots with text boxes in different corners
for i, ax in enumerate(axes):
    # Plot histogram
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title
    ax.set_title(f'Text Box in {corner_labels[i]}', fontsize=14)

    # Create text box properties
    box_props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # Add text box
    ax.text(positions[i][0], positions[i][1], textstr,
            transform=ax.transAxes, fontsize=12,
            verticalalignment=alignments[i][0],
            horizontalalignment=alignments[i][1],
            bbox=box_props)

plt.tight_layout()
plt.show()
```

这段代码创建了一个 2x2 的直方图网格，每个直方图的不同角落都有一个文本框。

## 理解文本框的定位

有几个关键参数可以控制文本框的定位：

1. **位置坐标**：`(x, y)` 坐标决定了文本框的放置位置。当使用 `transform=ax.transAxes` 时，这些坐标是坐标轴坐标，其中 `(0, 0)` 是左下角，`(1, 1)` 是右上角。
2. **垂直对齐方式**：`verticalalignment` 参数控制文本相对于 y 坐标的垂直对齐方式：
   - `'top'`：文本的顶部位于指定的 y 坐标处。
   - `'center'`：文本的中心位于指定的 y 坐标处。
   - `'bottom'`：文本的底部位于指定的 y 坐标处。
3. **水平对齐方式**：`horizontalalignment` 参数控制文本相对于 x 坐标的水平对齐方式：
   - `'left'`：文本的左边缘位于指定的 x 坐标处。
   - `'center'`：文本的中心位于指定的 x 坐标处。
   - `'right'`：文本的右边缘位于指定的 x 坐标处。

这些对齐选项在将文本放置在角落时尤为重要。例如，在右上角，你需要使用 `horizontalalignment='right'`，这样文本的右边缘才能与绘图的右边缘对齐。
