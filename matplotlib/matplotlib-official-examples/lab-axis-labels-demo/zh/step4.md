# 设置颜色条标签的位置

我们可以使用`colorbar`方法和`set_label`方法来设置颜色条标签的位置。我们可以将位置设置为`'top'`（顶部）、`'bottom'`（底部）、`'left'`（左侧）或`'right'`（右侧）。在这个例子中，我们将把位置设置为`'top'`。

```python
cbar = fig.colorbar(sc)
cbar.set_label("ZLabel", loc='top')
```
