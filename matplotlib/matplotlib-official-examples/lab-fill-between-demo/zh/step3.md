# 选择性填充水平区域

参数 `where` 允许指定要填充的 x 范围。它是一个与 `x` 大小相同的布尔数组。只有连续 `True` 序列的 x 范围会被填充。因此，相邻 `True` 和 `False` 值之间的范围永远不会被填充。所以，除非数据点的 x 距离足够精细以至于上述效果不明显，否则建议设置 `interpolate=True`。

```python
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title('interpolation=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolation=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                 interpolate=True)
ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                 interpolate=True)
fig.tight_layout()
```

在上述代码中：

第一个子图（`ax1`）设置了 `interpolation=False`。它绘制了两条线 `y1` 和 `y2`，然后根据 `where=(y1 > y2)` 和 `where=(y1 < y2)` 条件分别填充了相应区域。

第二个子图（`ax2`）设置了 `interpolation=True`。同样绘制了两条线 `y1` 和 `y2`，并根据相同的条件填充区域，但由于设置了 `interpolate=True`，填充效果会有所不同，相邻 `True` 和 `False` 值之间的区域会被更平滑地处理。最后通过 `fig.tight_layout()` 调整图形布局。
