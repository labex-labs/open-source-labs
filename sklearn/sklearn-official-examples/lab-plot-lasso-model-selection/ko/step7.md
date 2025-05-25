# 좌표 하강법을 이용한 Lasso

`LassoCV`를 사용하여 하이퍼파라미터 튜닝을 수행합니다.

```python
from sklearn.linear_model import LassoCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```
