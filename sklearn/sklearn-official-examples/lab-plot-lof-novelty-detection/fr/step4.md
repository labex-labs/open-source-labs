# Évaluer le modèle

Nous allons évaluer le modèle entraîné sur les données de test et les données d'anomalies. Nous utiliserons la méthode `predict` pour prédire les étiquettes des données de test et des données d'anomalies. Nous compterons ensuite le nombre d'erreurs dans les données de test et les données d'anomalies.

```python
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
