# 创建图形和子图

在这一步中，我们将创建一个带有两个用于累积分布的子图的图形。我们还将把图形大小设置为 9x4。

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```
