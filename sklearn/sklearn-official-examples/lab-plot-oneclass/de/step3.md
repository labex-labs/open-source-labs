# Berechne die Anzahl der Fehler

Wir werden die Anzahl der Fehler berechnen, die das Modell bei den Trainingsdaten, den regulären neuartigen Beobachtungen und den abnormen neuartigen Beobachtungen macht.

```python
# Zähle die Anzahl der Fehler
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
