# 绘制图表

既然我们已经有了示例数据，就可以使用 `errorbar()` 函数来绘制图表了。我们将把 `x` 和 `y` 数组作为前两个参数传入。然后，我们将分别使用 `xerr` 和 `yerr` 参数，将 x 方向的误差指定为 0.2，y 方向的误差指定为 0.4。

```python
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()
```
