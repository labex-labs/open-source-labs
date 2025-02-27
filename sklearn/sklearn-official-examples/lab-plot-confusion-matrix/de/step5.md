# Konfusionsmatrix generieren

Wir werden eine Konfusionsmatrix mit der Klasse ConfusionMatrixDisplay aus scikit-learn generieren. Die Konfusionsmatrix wird die Anzahl der korrekten und falschen Vorhersagen für jede Klasse anzeigen.

```python
np.set_printoptions(precision=2)
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    y_test,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize=None,
)
```
