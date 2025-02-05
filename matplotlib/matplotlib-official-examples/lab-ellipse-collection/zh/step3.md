# 创建椭圆集合

我们使用上述数据创建一个 `EllipseCollection`，并将单位指定为 'x'，偏移量指定为 `XY`。

```python
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
```
