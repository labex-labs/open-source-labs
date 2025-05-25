# 최소 각도 회귀를 이용한 Lasso

`LassoLarsCV`를 사용하여 하이퍼파라미터 튜닝을 수행합니다.

```python
from sklearn.linear_model import LassoLarsCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoLarsCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```
