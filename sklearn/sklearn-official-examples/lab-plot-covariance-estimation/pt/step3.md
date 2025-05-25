# Comparar Diferentes Abordagens para Definir o Parâmetro de Regularização

Comparamos três abordagens para definir o parâmetro de regularização: validação cruzada, Ledoit-Wolf e OAS.

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
