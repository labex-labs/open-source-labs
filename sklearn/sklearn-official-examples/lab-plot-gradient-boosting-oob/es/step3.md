# Estimar el mejor número de iteraciones utilizando validación cruzada

Podemos estimar el mejor número de iteraciones utilizando validación cruzada. Utilizaremos validación cruzada de 5 pliegues y calcularemos la pérdida logarítmica negativa para cada número de iteraciones.

```python
from sklearn.model_selection import cross_val_score

cv_scores = []
for i in range(1, params['n_estimators'] + 1):
    clf.set_params(n_estimators=i)
    scores = -1 * cross_val_score(clf, X, y, cv=5, scoring='neg_log_loss')
    cv_scores.append(scores.mean())
```
