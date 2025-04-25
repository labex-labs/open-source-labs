# 生成稀疏数据

接下来，我们生成一些将用于 Lasso 回归的稀疏数据。我们从上一步复制密集数据，并将所有小于 2.5 的值替换为 0。我们还将稀疏数据转换为 Scipy 的压缩稀疏列格式。

```python
Xs = X.copy()
Xs[Xs < 2.5] = 0.0
Xs_sp = sparse.coo_matrix(Xs)
Xs_sp = Xs_sp.tocsc()
```
