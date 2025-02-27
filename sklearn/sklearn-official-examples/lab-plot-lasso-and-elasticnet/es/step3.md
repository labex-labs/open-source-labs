# Determinación Automática de Relevancia (ARD)

Una regresión ARD es la versión bayesiana del Lasso. Puede producir estimaciones de intervalo para todos los parámetros, incluyendo la varianza del error, si es necesario. Es una opción adecuada cuando las señales tienen ruido gaussiano.

```python
from sklearn.linear_model import ARDRegression

t0 = time()
ard = ARDRegression().fit(X_train, y_train)
print(f"ARD fit done in {(time() - t0):.3f}s")

y_pred_ard = ard.predict(X_test)
r2_score_ard = r2_score(y_test, y_pred_ard)
print(f"ARD r^2 on test data : {r2_score_ard:.3f}")
```
