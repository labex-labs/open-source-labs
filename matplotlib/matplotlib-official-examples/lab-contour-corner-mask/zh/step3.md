# 对数据进行掩码处理

在这一步中，我们将使用布尔掩码对一些 `z` 值进行掩码处理。我们使用 `np.zeros_like()` 函数创建一个 `mask` 数组，然后将一些值设置为 `True` 以对其进行掩码处理。

```python
# 对各种z值进行掩码处理。
mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)
```
