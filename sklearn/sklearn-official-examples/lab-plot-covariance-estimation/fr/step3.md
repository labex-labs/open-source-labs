#Comparer différentes approches pour définir le paramètre de régularisation

Nous comparons trois approches pour définir le paramètre de régularisation : la validation croisée, Ledoit-Wolf et OAS.

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
