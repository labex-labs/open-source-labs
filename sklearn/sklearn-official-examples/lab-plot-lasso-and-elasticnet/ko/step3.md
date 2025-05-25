# 자동 관련성 결정 (ARD)

ARD 회귀는 Lasso 의 베이지안 버전입니다. 필요한 경우 오차 분산을 포함한 모든 매개변수에 대한 구간 추정값을 생성할 수 있습니다. 신호에 가우시안 잡음이 있는 경우 적절한 옵션입니다.

```python
from sklearn.linear_model import ARDRegression

t0 = time()
ard = ARDRegression().fit(X_train, y_train)
print(f"ARD fit done in {(time() - t0):.3f}s")

y_pred_ard = ard.predict(X_test)
r2_score_ard = r2_score(y_test, y_pred_ard)
print(f"ARD r^2 on test data : {r2_score_ard:.3f}")
```
