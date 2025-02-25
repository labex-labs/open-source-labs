# データのマスク化

このステップでは、ブールマスクを使用して一部の`z`値をマスクします。`np.zeros_like()`関数を使用して`mask`配列を作成し、その後、一部の値を`True`に設定してマスクします。

```python
# Mask various z values.
mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)
```
