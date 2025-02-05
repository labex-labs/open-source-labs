# 定义颜色循环示例函数

我们定义了 `color_cycle_example` 函数，该函数以一个轴对象为输入，并为颜色循环中的每种颜色绘制一条正弦波。颜色循环由 `rcParams` 定义。

```python
def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
```
