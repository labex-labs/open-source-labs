# 回帰モデルのフィッティング

潜在的に過適合するために、10 次の多項式を試します。ただし、ベイズ線形モデルは多項式係数のサイズを正則化します。ARDRegression と BayesianRidge のデフォルト設定は`fit_intercept=True`なので、PolynomialFeatures は追加のバイアス特徴を導入しないはずです。`return_std=True`を設定することで、ベイズ回帰モデルはモデルパラメータの事後分布の標準偏差を返します。

```python
ard_poly = make_pipeline(
    PolynomialFeatures(degree=10, include_bias=False),
    StandardScaler(),
    ARDRegression(),
).fit(X, y)
brr_poly = make_pipeline(
    PolynomialFeatures(degree=10, include_bias=False),
    StandardScaler(),
    BayesianRidge(),
).fit(X, y)

y_ard, y_ard_std = ard_poly.predict(X_plot, return_std=True)
y_brr, y_brr_std = brr_poly.predict(X_plot, return_std=True)
```
