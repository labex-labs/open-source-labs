# Preprocesar los datos

Escalaremos el conjunto de datos utilizando el método StandardScaler y ajustaremos el estimador LassoLarsIC con el criterio AIC.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
```
