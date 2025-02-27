# Predecir y evaluar el modelo

Utilizaremos el modelo entrenado para predecir el valor de los dígitos para las muestras en el subconjunto de prueba. Luego, evaluaremos el modelo utilizando los métodos `metrics.classification_report()` y `metrics.ConfusionMatrixDisplay.from_predictions()` de `sklearn.metrics`.

```python
predicted = clf.predict(X_test)

print(
    f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")
```
