# Calculer le meilleur nombre d'itérations pour les données de test

Nous pouvons également calculer le meilleur nombre d'itérations pour les données de test. Nous allons calculer la perte logarithmique négative pour chaque nombre d'itérations sur les données de test.

```python
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt

test_scores = []
for i, y_pred in enumerate(clf.staged_predict_proba(X)):
    score = log_loss(y, y_pred)
    test_scores.append(score)

best_n_estimators = np.argmin(test_scores) + 1
```
