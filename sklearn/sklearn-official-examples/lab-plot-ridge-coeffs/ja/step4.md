# 異なる正則化強度でモデルを学習する

ループを使って異なる正則化強度でモデルを学習します。`set_params` 関数の alpha の値を変更することで正則化強度を設定します。各 alpha の値に対する係数とエラーを保存します。

```python
coefs = []
errors = []

alphas = np.logspace(-6, 6, 200)

for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X, y)
    coefs.append(clf.coef_)
    errors.append(mean_squared_error(clf.coef_, w))
```
