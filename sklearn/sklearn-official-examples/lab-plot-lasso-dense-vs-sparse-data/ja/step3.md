# 密集データでLassoを学習する

次に、密集データと疎データのそれぞれに対して2つのLasso回帰モデルを学習します。alphaパラメータを1に設定し、最大反復回数を1000に設定します。

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```
