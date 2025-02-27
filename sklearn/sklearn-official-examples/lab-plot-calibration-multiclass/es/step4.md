# Comparación de log-loss

Comparamos la log-loss del clasificador no calibrado y del clasificador calibrado en las predicciones de las 1000 muestras de prueba.

```python
from sklearn.metrics import log_loss

score = log_loss(y_test, clf_probs)
cal_score = log_loss(y_test, cal_clf_probs)

print("Log-loss de")
print(f" * clasificador no calibrado: {score:.3f}")
print(f" * clasificador calibrado: {cal_score:.3f}")
```
