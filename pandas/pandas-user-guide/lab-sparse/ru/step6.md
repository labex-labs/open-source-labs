# Преобразование между разреженными и плотными представлениями

Мы можем легко преобразовывать данные между разреженным и плотным представлениями, и наоборот.

```python
# Converting from sparse to dense
print(sdf.sparse.to_dense())

# Converting from dense to sparse
dense = pd.DataFrame({"A": [1, 0, 0, 1]})
dtype = pd.SparseDtype(int, fill_value=0)
print(dense.astype(dtype))
```
