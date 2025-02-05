# 自定义 y 轴刻度

我们为最左边的子图自定义 y 轴刻度。

```python
for irow in range(2):
    axs[irow, 0].yaxis.set_ticks(np.arange(0, 10, 2))
```
