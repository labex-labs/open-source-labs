# 添加标签和标题

现在我们将使用`set_xlabel()`、`set_ylabel()`和`set_title()`方法为x轴和y轴添加标签，并为图形添加标题。

```python
# 添加标签和标题
ax.set_xlabel("x Axis label", fontsize=14)
ax.set_ylabel("y Axis label", fontsize=14)
ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
```
