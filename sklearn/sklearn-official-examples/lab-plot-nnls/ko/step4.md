# 일반 선형 회귀 적합

이제 일반 선형 회귀를 사용하여 데이터를 적합할 것입니다. 이는 scikit-learn 의 `LinearRegression` 클래스를 사용하여 수행됩니다. 그런 다음 테스트 세트에 대한 값을 예측하고 R2 점수를 계산할 것입니다.

```python
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)
r2_score_ols = r2_score(y_test, y_pred_ols)
print("OLS R2 score", r2_score_ols)
```
