# 创建一个线条图形对象

现在，你可以使用`matplotlib.lines`中的`Line2D`类来创建线条图形对象。你可以将x和y坐标、线宽、颜色以及坐标轴对象作为参数进行指定。

```python
line = lines.Line2D(x, y, lw=2, color='black', axes=ax)
```
