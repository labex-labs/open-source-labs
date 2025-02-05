# 创建误差线

在这一步中，我们将在极坐标轴上创建误差线。我们将使用 `errorbar()` 函数来创建半径和 theta 误差线。

```python
ax.errorbar(theta, r, xerr=0.25, yerr=0.1, capsize=7, fmt="o", c="seagreen")
```
