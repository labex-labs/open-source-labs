# Modell auswerten

Wir werden das trainierte Modell auf den Test- und Ausreißerdaten auswerten. Wir werden die predict-Methode verwenden, um die Labels der Test- und Ausreißerdaten vorherzusagen. Anschließend werden wir die Anzahl der Fehler in den Test- und Ausreißerdaten zählen.

```python
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```