# Adjust Parasite Axis

We need to adjust the position of the parasite axes. The `new_fixed_axis()` function is used to create a new y-axis on the right side of the plot. The `toggle()` function is used to turn on all the ticks and labels of the right y-axis.

```python
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
```
