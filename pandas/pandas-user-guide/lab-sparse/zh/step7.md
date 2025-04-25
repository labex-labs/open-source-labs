# 与 scipy 稀疏矩阵交互

最后，我们可以从 scipy 稀疏矩阵创建一个具有稀疏值的 DataFrame，反之亦然。

```python
# 导入必要的库
from scipy.sparse import csr_matrix

# 使用 scipy 创建一个稀疏矩阵
arr = np.random.random(size=(1000, 5))
arr[arr <.9] = 0
sp_arr = csr_matrix(arr)

# 从稀疏矩阵创建一个 DataFrame
sdf = pd.DataFrame.sparse.from_spmatrix(sp_arr)

# 打印 DataFrame
print(sdf.head())
print(sdf.dtypes)

# 转换回稀疏矩阵
print(sdf.sparse.to_coo())
```
