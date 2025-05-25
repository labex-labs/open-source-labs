# Ridge 회귀 분석 적용

이제 데이터셋에 Ridge 회귀 분석을 적용하고 HuberRegressor 와의 성능을 비교합니다.

```python
# huber 회귀 분석과 비교하기 위해 ridge 회귀 분석 적용
ridge = Ridge(alpha=0.0, random_state=0)
ridge.fit(X, y)
coef_ridge = ridge.coef_
coef_ = ridge.coef_ * x + ridge.intercept_
plt.plot(x, coef_, "g-", label="ridge regression")

# 플롯에 범례 추가
plt.legend(loc=0)

# 플롯 표시
plt.title("HuberRegressor 와 Ridge 의 비교")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
