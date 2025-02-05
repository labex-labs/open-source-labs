# 创建散点图

使用随机生成的数据创建一个散点图。

```python
np.random.seed(19680801)
data = np.random.rand(100, 2)

subplot_kw = dict(xlim=(0, 1), ylim=(0, 1), autoscale_on=False)
fig, ax = plt.subplots(subplot_kw=subplot_kw)
pts = ax.scatter(data[:, 0], data[:, 1], s=80)
selector = SelectFromCollection(ax, pts)
```
