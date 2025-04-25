# 执行稀疏计算

我们可以将 NumPy 通用函数应用于 SparseArray，并得到一个 SparseArray 作为结果。

```python
# 创建一个 SparseArray
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# 应用一个 NumPy 通用函数
print(np.abs(arr))
```
