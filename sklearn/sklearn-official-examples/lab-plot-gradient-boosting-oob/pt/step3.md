# Estimar o Número Ideal de Iterações usando Validação Cruzada

Podemos estimar o melhor número de iterações usando validação cruzada. Usaremos validação cruzada 5-fold e calculamos a perda de log negativo para cada número de iterações.

```python
from sklearn.model_selection import cross_val_score

cv_scores = []
for i in range(1, params['n_estimators'] + 1):
    clf.set_params(n_estimators=i)
    scores = -1 * cross_val_score(clf, X, y, cv=5, scoring='neg_log_loss')
    cv_scores.append(scores.mean())
```
