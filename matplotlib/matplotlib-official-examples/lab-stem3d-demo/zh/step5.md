# 更改绘图方向

在这一步中，我们将使用 `orientation` 参数来更改绘图的方向。我们将方向设置为 `'x'`，以便茎沿 x 方向投影，并且基线位于 yz 平面中。

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()
```
