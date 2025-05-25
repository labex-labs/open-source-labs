# 음수가 아닌 최소 제곱 회귀 적합

이제 음수가 아닌 최소 제곱 회귀를 사용하여 데이터를 적합할 것입니다. 이는 scikit-learn 의 `LinearRegression` 클래스를 사용하여 `positive=True` 매개변수로 수행됩니다. 그런 다음 테스트 세트에 대한 값을 예측하고 R2 점수를 계산할 것입니다.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

reg_nnls = LinearRegression(positive=True)
y_pred_nnls = reg_nnls.fit(X_train, y_train).predict(X_test)
r2_score_nnls = r2_score(y_test, y_pred_nnls)
print("NNLS R2 score", r2_score_nnls)
```
