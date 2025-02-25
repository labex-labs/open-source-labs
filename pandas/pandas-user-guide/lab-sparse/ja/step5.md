# 疎計算の実行

NumPyのufuncをSparseArrayに適用し、結果としてSparseArrayを取得することができます。

```python
# SparseArrayを作成
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# NumPyのufuncを適用
print(np.abs(arr))
```
