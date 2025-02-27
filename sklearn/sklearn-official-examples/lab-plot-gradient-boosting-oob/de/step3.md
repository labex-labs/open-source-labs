# Besten Iterationszähler mit Hilfe der Kreuzvalidierung abschätzen

Wir können den besten Iterationszähler mithilfe der Kreuzvalidierung abschätzen. Wir werden eine 5-fache Kreuzvalidierung verwenden und die negative Log-Loss-Funktion für jede Anzahl an Iterationen berechnen.

```python
from sklearn.model_selection import cross_val_score

cv_scores = []
for i in range(1, params['n_estimators'] + 1):
    clf.set_params(n_estimators=i)
    scores = -1 * cross_val_score(clf, X, y, cv=5, scoring='neg_log_loss')
    cv_scores.append(scores.mean())
```
