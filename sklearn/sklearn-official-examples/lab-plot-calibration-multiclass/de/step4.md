# Vergleich der Log-Loss

Wir vergleichen die Log-Loss des unkalibrierten und des kalibrierten Klassifikators bei den Vorhersagen der 1000 Testproben.

```python
from sklearn.metrics import log_loss

score = log_loss(y_test, clf_probs)
cal_score = log_loss(y_test, cal_clf_probs)

print("Log-Loss von")
print(f" * unkalibrierten Klassifikator: {score:.3f}")
print(f" * kalibrierten Klassifikator: {cal_score:.3f}")
```
