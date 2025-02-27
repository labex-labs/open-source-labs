# Daten vorverarbeiten

Wir werden den Datensatz mit der StandardScaler-Methode skalieren und den LassoLarsIC-Schätzer mit dem AIC-Kriterium anpassen.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
```
