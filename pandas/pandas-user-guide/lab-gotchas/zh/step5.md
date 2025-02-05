# 理解与 NumPy 的差异

Pandas 和 NumPy 在计算方差的方式上存在细微差异。在两个库之间切换时，这一点需要加以考虑。

```python
# pandas 中的方差
var_pandas = df.var()

# NumPy 中的方差
var_numpy = np.var(df.values)
```
