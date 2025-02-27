# 疎データでLassoを学習する

次に、密集データと疎データのそれぞれに対して2つのLasso回帰モデルを学習します。alphaパラメータを0.1に設定し、最大反復回数を10000に設定します。

```python
alpha = 0.1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
```
