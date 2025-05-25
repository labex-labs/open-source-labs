# 회귀자 맞추기

10 차 다항식을 시도하여 과적합될 가능성이 있지만, 베이지안 선형 모델은 다항식 계수의 크기를 규제합니다. ARDRegression 및 BayesianRidge 의 기본값으로 `fit_intercept=True`이므로 PolynomialFeatures 는 추가적인 편향 특징을 도입하지 않아야 합니다. `return_std=True`를 설정하면 베이지안 회귀자는 모델 매개변수에 대한 사후 분포의 표준 편차를 반환합니다.

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
