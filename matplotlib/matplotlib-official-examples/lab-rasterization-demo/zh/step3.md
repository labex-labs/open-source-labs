# 创建一个包含四个子图的图形

我们将创建一个包含四个子图的图形，以说明光栅化的不同方面。

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```
