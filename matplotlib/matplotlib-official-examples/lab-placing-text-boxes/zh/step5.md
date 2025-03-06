# 创建包含多个文本元素的最终可视化图表

在这最后一步，我们将结合所学的所有知识，创建一个包含多种不同样式文本元素的综合可视化图表。这将展示如何使用文本框来增强数据故事性。

## 创建高级可视化图表

让我们创建一个更复杂的图表，其中既包含我们的直方图，又包含一些额外的视觉元素。在一个新的单元格中，输入并运行以下代码：

```python
# Create a figure with a larger size for our final visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the histogram with more bins and a different color
n, bins, patches = ax.hist(x, bins=75, color='lightblue',
                           edgecolor='darkblue', alpha=0.7)

# Add title and labels with improved styling
ax.set_title('Distribution of Random Data with Statistical Annotations',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Mark the mean with a vertical line
ax.axvline(x=mu, color='red', linestyle='-', linewidth=2,
           label=f'Mean: {mu:.2f}')

# Mark one standard deviation range
ax.axvline(x=mu + sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean + 1σ: {mu+sigma:.2f}')
ax.axvline(x=mu - sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean - 1σ: {mu-sigma:.2f}')

# Create a text box with statistics in the top left
stats_box_props = dict(boxstyle='round', facecolor='lightyellow',
                      alpha=0.8, edgecolor='gold', linewidth=2)

stats_text = '\n'.join((
    r'$\mathbf{Statistics:}$',
    r'$\mu=%.2f$ (mean)' % (mu,),
    r'$\mathrm{median}=%.2f$' % (median,),
    r'$\sigma=%.2f$ (std. dev.)' % (sigma,)
))

ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=stats_box_props)

# Add an informational text box in the top right
info_box_props = dict(boxstyle='round4', facecolor='lightcyan',
                     alpha=0.8, edgecolor='deepskyblue', linewidth=2)

info_text = '\n'.join((
    r'$\mathbf{About\ Normal\ Distributions:}$',
    r'$\bullet\ 68\%\ of\ data\ within\ 1\sigma$',
    r'$\bullet\ 95\%\ of\ data\ within\ 2\sigma$',
    r'$\bullet\ 99.7\%\ of\ data\ within\ 3\sigma$'
))

ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', horizontalalignment='right',
        bbox=info_box_props)

# Add a legend
ax.legend(fontsize=12)

# Tighten the layout and show the plot
plt.tight_layout()
plt.show()
```

当你运行这个单元格时，你会看到一个综合可视化图表，其中包含：

- 经过样式优化的数据直方图
- 标记均值和一个标准差范围的垂直线
- 左上角的统计信息文本框
- 右上角关于正态分布的信息文本框
- 解释垂直线含义的图例

## 理解高级元素

让我们来分析一下我们添加的一些新元素：

1. **使用 `axvline()` 绘制垂直线**：
   - 这些线直接在图表上标记重要的统计数据。
   - `label` 参数可将这些线包含在图例中。
2. **多种不同样式的文本框**：
   - 每个文本框都有不同的用途，并使用独特的样式。
   - 统计信息框显示我们从数据中计算出的值。
   - 信息框提供关于正态分布的背景信息。
3. **增强的格式设置**：
   - 使用 LaTeX 格式通过 `\mathbf{}` 创建粗体文本。
   - 使用 `\bullet` 创建项目符号。
   - 使用 `\ `（反斜杠后接一个空格）控制间距。
4. **网格和图例**：
   - 网格帮助查看者更准确地读取图表中的数值。
   - 图例解释彩色线条的含义。

## 关于文本框放置的最终提示

在可视化图表中放置多个文本元素时，请考虑以下几点：

1. **视觉层次**：最重要的信息应该最突出。
2. **位置**：将相关信息放置在可视化图表的相关部分附近。
3. **对比度**：确保文本在其背景下易于阅读。
4. **一致性**：对相似类型的信息使用一致的样式。
5. **避免杂乱**：避免在可视化图表中放置过多的文本元素。

通过精心放置和设置文本框的样式，你可以创建既信息丰富又美观的可视化图表，引导查看者理解数据中的关键见解。
