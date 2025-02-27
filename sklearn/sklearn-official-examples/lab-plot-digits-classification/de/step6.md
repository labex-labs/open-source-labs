# Vorhersagen und Auswerten des Modells

Wir werden das trainierte Modell verwenden, um die Ziffernwerte für die Proben im Testdatensatz zu prognostizieren. Anschließend werden wir das Modell mit den Methoden `metrics.classification_report()` und `metrics.ConfusionMatrixDisplay.from_predictions()` aus `sklearn.metrics` auswerten.

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
