# Comparar diferentes enfoques para establecer el parámetro de regularización

Comparamos tres enfoques para establecer el parámetro de regularización: validación cruzada, Ledoit-Wolf y OAS.

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
