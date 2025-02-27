# Modellleistung auswerten

```python
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
```

Wir prognostizieren die Zielwerte mit den Testdaten und bewerten die Modellleistung mit der Funktion `classification_report()`. Wir zeichnen auch die Konfusionsmatrix (Confusion Matrix) mit der Funktion `ConfusionMatrixDisplay()` auf.
