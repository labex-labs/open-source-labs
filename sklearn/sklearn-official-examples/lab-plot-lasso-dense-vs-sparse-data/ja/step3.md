# 密集データで Lasso を学習する

次に、密集データと疎データのそれぞれに対して 2 つの Lasso 回帰モデルを学習します。alpha パラメータを 1 に設定し、最大反復回数を 1000 に設定します。

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```
