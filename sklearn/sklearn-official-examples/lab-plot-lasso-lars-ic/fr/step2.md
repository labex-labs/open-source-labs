# Prétraiter les données

Nous allons mettre à l'échelle le jeu de données en utilisant la méthode StandardScaler et ajuster l'estimateur LassoLarsIC avec le critère AIC.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
```
