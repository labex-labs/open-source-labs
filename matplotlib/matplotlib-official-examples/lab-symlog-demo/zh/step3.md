# 创建图表

既然我们已经有了数据，就可以创建图表了。我们将创建三个子图，每个子图都有不同的 `symlog` 轴缩放。

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
```
