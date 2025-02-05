# 在稀疏和密集格式之间转换

我们可以轻松地将数据从稀疏格式转换为密集格式，反之亦然。

```python
# 从稀疏转换为密集
print(sdf.sparse.to_dense())

# 从密集转换为稀疏
dense = pd.DataFrame({"A": [1, 0, 0, 1]})
dtype = pd.SparseDtype(int, fill_value=0)
print(dense.astype(dtype))
```
