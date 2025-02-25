# マスク付き配列の作成

このステップでは、マスク付き配列を作成し、マスクをデータに適用します。

```python
# create masked array
data = (1, 2, 3, 4, 5, 6, 7, 8)
mask = (1, 0, 1, 0, 0, 0, 1, 0)
xsecs = secs * np.ma.MaskedArray(data, mask, float)
```
