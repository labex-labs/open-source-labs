# 拟合回归器

我们尝试使用10次多项式来可能地过拟合，尽管贝叶斯线性模型会对多项式系数的大小进行正则化。由于ARDRegression和BayesianRidge默认`fit_intercept=True`，那么PolynomialFeatures不应引入额外的偏差特征。通过设置`return_std=True`，贝叶斯回归器会返回模型参数后验分布的标准差。

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
