# 理解SparseDtype

`SparseDtype` 存储非稀疏值的数据类型和标量填充值。我们可以仅通过传递一个数据类型来构造它，也可以传递一个显式的填充值。

```python
# 创建一个SparseDtype
print(pd.SparseDtype(np.dtype('datetime64[ns]')))

# 创建一个带有显式填充值的SparseDtype
print(pd.SparseDtype(np.dtype('datetime64[ns]'), fill_value=pd.Timestamp('2017-01-01')))
```
