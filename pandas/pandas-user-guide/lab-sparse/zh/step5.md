# 执行稀疏计算

我们可以将NumPy通用函数应用于SparseArray，并得到一个SparseArray作为结果。

```python
# 创建一个SparseArray
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# 应用一个NumPy通用函数
print(np.abs(arr))
```
