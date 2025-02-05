# 设置柱状图的 x 和 y 单位

在这一步中，我们将使用各种关键字来设置柱状图的 x 和 y 单位。我们将使用 `xunits` 和 `yunits` 参数将 x 和 y 单位分别设置为厘米和英寸。

```python
axs[0, 1].bar(cms, cms, bottom=bottom, width=width, xunits=cm, yunits=inch)
```
