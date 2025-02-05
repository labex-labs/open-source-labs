# 使用相关方法设置虚线的其他属性

虚线的其他属性也可以使用诸如`~.Line2D.set_dash_joinstyle()`、`~.Line2D.set_dash_joinstyle()`和`~.Line2D.set_gapcolor()`等相关方法来设置。在本示例中，我们将使用`dashes`和`gapcolor`参数为`line3`设置虚线序列和交替颜色。

```python
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')
```
