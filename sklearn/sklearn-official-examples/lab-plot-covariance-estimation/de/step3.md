# Vergleiche verschiedene Ansätze zum Festlegen des Regularisierungsparameters

Wir vergleichen drei Ansätze zum Festlegen des Regularisierungsparameters: Kreuzvalidierung, Ledoit-Wolf und OAS.

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
