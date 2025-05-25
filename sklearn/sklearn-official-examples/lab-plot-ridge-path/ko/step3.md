# 릿지 회귀 경로 계산

이 단계에서는 서로 다른 정규화 강도에 대한 릿지 회귀 경로를 계산합니다.

```python
n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)

coefs = []
for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)
```
