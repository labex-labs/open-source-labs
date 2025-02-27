# Estimer le meilleur nombre d'itérations en utilisant la validation croisée

Nous pouvons estimer le meilleur nombre d'itérations en utilisant la validation croisée. Nous utiliserons une validation croisée à 5 plis et calculerons la perte logarithmique négative pour chaque nombre d'itérations.

```python
from sklearn.model_selection import cross_val_score

cv_scores = []
for i in range(1, params['n_estimators'] + 1):
    clf.set_params(n_estimators=i)
    scores = -1 * cross_val_score(clf, X, y, cv=5, scoring='neg_log_loss')
    cv_scores.append(scores.mean())
```
