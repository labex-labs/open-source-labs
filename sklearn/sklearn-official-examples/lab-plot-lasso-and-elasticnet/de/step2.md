# Lasso

In diesem Schritt werden wir demonstrieren, wie man das Lasso-Regressionsmodell verwendet, um die dünn besetzten Koeffizienten des Datensatzes zu schätzen. Wir werden einen festen Wert für den Regularisierungsparameter `alpha` verwenden. In der Praxis sollte der optimale Parameter `alpha` durch Übergeben einer `TimeSeriesSplit`-Querverifizierungsstrategie an ein `LassoCV` ausgewählt werden. Um das Beispiel einfach und schnell auszuführen, legen wir hier direkt den optimalen Wert für alpha fest.

```python
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
from time import time

t0 = time()
lasso = Lasso(alpha=0.14).fit(X_train, y_train)
print(f"Lasso fit done in {(time() - t0):.3f}s")

y_pred_lasso = lasso.predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(f"Lasso r^2 on test data : {r2_score_lasso:.3f}")
```
