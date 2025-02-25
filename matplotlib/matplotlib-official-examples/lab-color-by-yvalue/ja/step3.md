# マスク配列を作成する

このステップでは、3つのマスク配列を作成します。1つは特定の閾値を超える値用、1つは特定の閾値未満の値用、そして1つは2つの閾値の間の値用です。

```python
upper = 0.77
lower = -0.77

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)
```
