# 将文本框添加到绘图中

最后，我们将使用`matplotlib.pyplot.text()`把文本框添加到绘图中。我们将在坐标轴坐标中指定文本框的位置，并使用`bbox`参数来添加框的属性。

```python
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
```
