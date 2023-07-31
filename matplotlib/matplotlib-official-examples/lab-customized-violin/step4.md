# Set axis style

Finally, we will set the style for the x-axis by specifying the tick labels and limits. We will define a helper function `set_axis_style` to accomplish this.

```python
# set style for the axes
labels = ['A', 'B', 'C', 'D']
set_axis_style(ax2, labels)

def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample Name')
```
