# Lasso

En este paso, demostraremos cómo usar el modelo de regresión Lasso para estimar los coeficientes dispersos del conjunto de datos. Usaremos un valor fijo del parámetro de regularización `alpha`. En la práctica, el parámetro óptimo `alpha` debería seleccionarse pasando una estrategia de validación cruzada `TimeSeriesSplit` a un `LassoCV`. Para mantener el ejemplo simple y rápido de ejecutar, aquí establecemos directamente el valor óptimo para alpha.

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
