# 정규화 매개변수 설정을 위한 다양한 접근 방식 비교

교차 검증, Ledoit-Wolf, 및 OAS 세 가지 접근 방식을 사용하여 정규화 매개변수를 설정하는 방법을 비교합니다.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.covariance import LedoitWolf, OAS

tuned_parameters = [{"shrinkage": shrinkages}]
cv = GridSearchCV(ShrunkCovariance(), tuned_parameters)
cv.fit(X_train)

lw = LedoitWolf()
loglik_lw = lw.fit(X_train).score(X_test)

oa = OAS()
loglik_oa = oa.fit(X_train).score(X_test)
```
