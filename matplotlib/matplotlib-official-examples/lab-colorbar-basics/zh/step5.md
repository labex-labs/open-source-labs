# 创建包含正数和负数数据的图

我们创建一个同时包含正数和负数数据的图，并使用 `colorbar` 函数为该图添加颜色条。这次，我们使用 `vmin` 和 `vmax` 参数指定颜色条的最小值和最大值。

```python
# 绘制介于 +/- 1.2 之间的正数和负数
pos_neg_clipped = plt.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2,
                             interpolation='none')

# 在颜色条上添加次刻度，以便于从颜色条上读取数值。
cbar = plt.colorbar(pos_neg_clipped, extend='both')
cbar.minorticks_on()
```
