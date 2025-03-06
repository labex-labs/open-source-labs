# 添加包含统计信息的文本框

现在我们已经有了一个基本的直方图，让我们通过添加一个显示数据统计信息的文本框来对其进行优化。这将使可视化内容对查看者更有参考价值。

## 创建文本内容

首先，我们需要准备要放入文本框的文本内容。在一个新的单元格中，输入并运行以下代码：

```python
# Create a string with the statistics
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu,),           # Mean
    r'$\mathrm{median}=%.2f$' % (median,),  # Median
    r'$\sigma=%.2f$' % (sigma,)       # Standard deviation
))

print("Text content for our box:")
print(textstr)
```

你应该会看到类似于以下的输出：

```
Text content for our box:
$\mu=-0.31$
$\mathrm{median}=-0.28$
$\sigma=29.86$
```

这段代码创建了一个多行字符串，其中包含了我们数据的均值、中位数和标准差。让我们来看看这段代码的一些有趣之处：

1. `\n'.join(...)` 方法将多个字符串连接起来，并用换行符分隔。
2. 每个字符串前的 `r` 使其成为“原始”字符串，在包含特殊字符时很有用。
3. `$...$` 符号用于在 matplotlib 中进行 LaTeX 风格的数学格式设置。
4. `\mu` 和 `\sigma` 是 LaTeX 符号，分别代表希腊字母 μ（mu）和 σ（sigma）。
5. `%.2f` 是一个格式化说明符，用于显示保留两位小数的浮点数。

## 创建并添加文本框

现在，让我们重新创建直方图并添加文本框。在一个新的单元格中，输入并运行以下代码：

```python
# Create a new figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data with Statistics', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Define the properties of the text box
properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# Add the text box to the plot
# Position the box in the top left corner (0.05, 0.95) in axes coordinates
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=properties)

# Display the plot
plt.tight_layout()
plt.show()
```

当你运行这个单元格时，你应该会看到直方图的左上角有一个文本框，显示着统计信息。

## 理解文本框代码

让我们来详细分析创建文本框的代码的重要部分：

1. `properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)`：
   - 这行代码创建了一个包含文本框属性的字典。
   - `boxstyle='round'`：使文本框具有圆角。
   - `facecolor='wheat'`：将文本框的背景颜色设置为小麦色。
   - `alpha=0.5`：使文本框半透明（透明度为 50%）。
2. `ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=properties)`：
   - 这行代码在坐标 (0.05, 0.95) 处向坐标轴添加文本。
   - `transform=ax.transAxes`：这一点很关键，它表示坐标使用的是坐标轴单位（0 - 1），而不是数据单位。因此，(0.05, 0.95) 表示“距离绘图左边缘 5%，距离底部边缘 95%”。
   - `fontsize=14`：设置字体大小。
   - `verticalalignment='top'`：将文本对齐，使文本的顶部位于指定的 y 坐标处。
   - `bbox=properties`：应用我们定义的文本框属性。

即使你放大绘图或更改数据范围，文本框相对于绘图坐标轴的位置也会保持不变。这是因为我们使用了 `transform=ax.transAxes`，它使用的是坐标轴坐标，而不是数据坐标。
