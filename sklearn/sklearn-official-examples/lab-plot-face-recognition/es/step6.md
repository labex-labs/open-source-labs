# Evaluar el rendimiento del modelo

```python
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
```

Predecimos los valores de la variable objetivo utilizando los datos de prueba y evaluamos el rendimiento del modelo utilizando la función `classification_report()`. También trazamos la matriz de confusión utilizando la función `ConfusionMatrixDisplay()`.
