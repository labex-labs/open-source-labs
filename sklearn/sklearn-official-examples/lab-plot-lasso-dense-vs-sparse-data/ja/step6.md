# 疎データの生成

次に、Lasso 回帰に使用する疎データを生成します。前のステップの密集データをコピーし、2.5 未満のすべての値を 0 に置き換えます。また、疎データを Scipy の圧縮疎列形式に変換します。

```python
Xs = X.copy()
Xs[Xs < 2.5] = 0.0
Xs_sp = sparse.coo_matrix(Xs)
Xs_sp = Xs_sp.tocsc()
```
