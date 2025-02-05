# 设置样式循环

我们将使用 `cycler` 为直方图设置样式循环。我们将创建三个样式循环：一个用于面颜色，一个用于标签，一个用于阴影图案。

```python
color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler(label=[f'set {n}' for n in range(4)])
hatch_cycle = cycler(hatch=['/', '*', '+', '|'])
```
