# 疎データの生成

次に、Lasso回帰に使用する疎データを生成します。前のステップの密集データをコピーし、2.5未満のすべての値を0に置き換えます。また、疎データをScipyの圧縮疎列形式に変換します。

```python
Xs = X.copy()
Xs[Xs < 2.5] = 0.0
Xs_sp = sparse.coo_matrix(Xs)
Xs_sp = Xs_sp.tocsc()
```
