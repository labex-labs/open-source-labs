# 正則化パラメータの設定方法を比較する

正則化パラメータの設定方法として、交差検証、Ledoit-Wolf、および OAS の 3 つのアプローチを比較します。

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
