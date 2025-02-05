# 创建后续文本对象

下一步是使用 `~.Axes.annotate` 创建后续文本对象。此函数允许你相对于前一个文本对象定位文本对象。以下代码创建了三个位于前一个文本对象右侧的文本对象。

```python
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # 自定义属性
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # 自定义属性
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # 自定义属性
```
