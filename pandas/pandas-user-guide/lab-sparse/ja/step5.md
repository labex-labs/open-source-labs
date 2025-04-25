# 疎計算の実行

NumPy の ufunc を SparseArray に適用し、結果として SparseArray を取得することができます。

```python
# SparseArray を作成
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# NumPy の ufunc を適用
print(np.abs(arr))
```
