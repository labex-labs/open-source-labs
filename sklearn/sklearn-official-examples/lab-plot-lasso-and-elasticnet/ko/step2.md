# Lasso

이 단계에서는 Lasso 회귀 모델을 사용하여 데이터셋의 희소 계수를 추정하는 방법을 보여줍니다. 정규화 매개변수 `alpha`의 고정 값을 사용합니다. 실제로는 최적의 매개변수 `alpha`를 `LassoCV`에 `TimeSeriesSplit` 교차 검증 전략을 전달하여 선택해야 합니다. 예시를 간단하고 빠르게 실행하기 위해 여기서는 alpha 의 최적 값을 직접 설정합니다.

```python
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
from time import time

t0 = time()
lasso = Lasso(alpha=0.14).fit(X_train, y_train)
print(f"Lasso fit done in {(time() - t0):.3f}s")

y_pred_lasso = lasso.predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(f"Lasso r^2 on test data : {r2_score_lasso:.3f}")
```
