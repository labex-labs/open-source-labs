# Предварительная обработка данных

Мы стандартизируем датасет с использованием метода StandardScaler и подберем параметры оценщика LassoLarsIC с использованием критерия AIC.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
```
