# 给图表添加误差线

我们使用 `Axes3D` 对象的 `errorbar` 方法给图表添加误差线。我们将 `zuplims` 和 `zlolims` 参数设置为数组，这些数组指定了哪些数据点有上限和下限。我们设置 `errorevery` 参数来控制误差线的频率。

```python
estep = 15
i = np.arange(t.size)
zuplims = (i % estep == 0) & (i // estep % 3 == 0)
zlolims = (i % estep == 0) & (i // estep % 3 == 2)

ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)
```
