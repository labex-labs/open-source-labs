# 调整寄生轴

我们需要调整寄生轴的位置。`new_fixed_axis()` 函数用于在绘图右侧创建一个新的 y 轴。`toggle()` 函数用于开启右侧 y 轴的所有刻度和标签。

```python
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
```
