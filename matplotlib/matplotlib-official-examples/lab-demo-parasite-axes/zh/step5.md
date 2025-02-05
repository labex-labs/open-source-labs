# 显示寄生轴1的右y轴

我们使用`par1.axis["right"].set_visible(True)`方法显示第一个寄生轴的右y轴。我们还设置`par1.axis["right"].major_ticklabels.set_visible(True)`和`par1.axis["right"].label.set_visible(True)`来显示右y轴的刻度标签和标签。

```python
par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)
```
