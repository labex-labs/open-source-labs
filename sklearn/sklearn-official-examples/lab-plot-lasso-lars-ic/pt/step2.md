# Pré-processar os Dados

Escalaremos o conjunto de dados usando o método `StandardScaler` e ajustaremos o estimador `LassoLarsIC` com o critério AIC.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
```
