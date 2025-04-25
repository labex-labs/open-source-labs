# 设置坐标轴样式

最后，我们将通过指定刻度标签和限制来设置 x 轴的样式。我们将定义一个辅助函数`set_axis_style`来完成此操作。

```python
# 设置坐标轴样式
labels = ['A', 'B', 'C', 'D']
set_axis_style(ax2, labels)

def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample Name')
```
