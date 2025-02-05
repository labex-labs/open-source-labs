# 添加图例和轴颜色

我们使用`host.legend()`方法为主轴添加一个图例。我们还使用`host.axis["left"].label.set_color(p1.get_color())`、`par1.axis["right"].label.set_color(p2.get_color())`和`par2.axis["right2"].label.set_color(p3.get_color())`方法，将主轴的左y轴标签、第一个寄生轴的右y轴标签以及第二个寄生轴的右y轴标签的颜色设置为与它们各自的线条颜色相匹配。

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
```
