# Ajustez le modèle de SVM à une classe

Ensuite, nous allons ajuster le modèle de SVM à une classe sur les données générées.

```python
# Ajustez le modèle
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# Prédisez les étiquettes pour les données d'entraînement, les observations nouvelles régulières et les observations nouvelles anormales
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
```
