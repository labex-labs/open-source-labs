# Trainiere ein lineares Regressionsmodell

Als nächstes trainieren wir ein lineares Regressionsmodell auf dem Trainingsset.

```python
from sklearn import linear_model

ols = linear_model.LinearRegression()
_ = ols.fit(X_train, y_train)
```
