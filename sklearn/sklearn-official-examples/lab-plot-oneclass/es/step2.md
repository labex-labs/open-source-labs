# Ajustar el modelo de one-class SVM

A continuación, ajustaremos el modelo de one-class SVM a los datos generados.

```python
# Ajustar el modelo
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# Predecir las etiquetas para los datos de entrenamiento, las observaciones novedosas regulares y las observaciones novedosas anormales
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
```
