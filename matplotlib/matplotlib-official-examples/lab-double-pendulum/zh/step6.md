# 设置绘图

现在我们将为模拟设置绘图。我们将创建一个图形，其x轴和y轴的范围等于摆的最大长度，将纵横比设置为相等，并添加网格。

```python
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
ax.set_aspect('equal')
ax.grid()
```
