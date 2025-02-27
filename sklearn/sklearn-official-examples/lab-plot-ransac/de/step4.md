# Vorhersagen für die Daten der geschätzten Modelle

Wir werden die Daten des linearen Modells und des RANSAC-Regressors vorhersagen und ihre Ergebnisse vergleichen.

```python
# Predict data of estimated models
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)
```
