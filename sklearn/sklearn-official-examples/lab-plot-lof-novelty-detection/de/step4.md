# Das Modell auswerten

Wir werden das trainierte Modell anhand der Test- und Ausreißer-Daten auswerten. Wir verwenden die `predict`-Methode, um die Labels der Test- und Ausreißer-Daten vorherzusagen. Anschließend zählen wir die Anzahl der Fehler in den Test- und Ausreißer-Daten.

```python
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
