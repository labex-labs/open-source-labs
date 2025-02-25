# 散布図の作成

ランダムに生成されたデータを使って散布図を作成します。

```python
np.random.seed(19680801)
data = np.random.rand(100, 2)

subplot_kw = dict(xlim=(0, 1), ylim=(0, 1), autoscale_on=False)
fig, ax = plt.subplots(subplot_kw=subplot_kw)
pts = ax.scatter(data[:, 0], data[:, 1], s=80)
selector = SelectFromCollection(ax, pts)
```
