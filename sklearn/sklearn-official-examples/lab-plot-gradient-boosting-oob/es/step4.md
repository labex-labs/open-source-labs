# Calcular el mejor número de iteraciones para los datos de prueba

También podemos calcular el mejor número de iteraciones para los datos de prueba. Calcularemos la pérdida logarítmica negativa para cada número de iteraciones en los datos de prueba.

```python
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt

test_scores = []
for i, y_pred in enumerate(clf.staged_predict_proba(X)):
    score = log_loss(y, y_pred)
    test_scores.append(score)

best_n_estimators = np.argmin(test_scores) + 1
```
