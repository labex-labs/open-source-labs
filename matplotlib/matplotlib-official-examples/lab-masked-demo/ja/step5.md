# NaNに設定する

y > 0.7の箇所をNaNに設定します。NaN値を持つ新しいy配列を作成します。

```python
y4 = y.copy()
y4[y3 > 0.7] = np.nan
```
