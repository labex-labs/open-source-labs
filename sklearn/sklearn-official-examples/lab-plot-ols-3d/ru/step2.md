# Подгонка модели линейной регрессии

Далее мы подгоняем модель линейной регрессии к обучающей выборке.

```python
from sklearn import linear_model

ols = linear_model.LinearRegression()
_ = ols.fit(X_train, y_train)
```
