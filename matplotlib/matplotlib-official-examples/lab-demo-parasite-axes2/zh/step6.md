# 添加图例和颜色

我们将使用 `legend()` 和 `label.set_color()` 函数为图表添加图例，并将每个轴的标签颜色设置为与相应数据集的颜色匹配。

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())
```
