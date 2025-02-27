# Besten Iterationszähler für Testdaten berechnen

Wir können auch den besten Iterationszähler für die Testdaten berechnen. Wir werden die negative Log-Loss-Funktion für jede Anzahl an Iterationen auf den Testdaten berechnen.

```python
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt

test_scores = []
for i, y_pred in enumerate(clf.staged_predict_proba(X)):
    score = log_loss(y, y_pred)
    test_scores.append(score)

best_n_estimators = np.argmin(test_scores) + 1
```
