# Visualisierung der Konfusionsmatrix

Wir werden die Konfusionsmatrix mit matplotlib visualisieren. Wir werden sowohl eine nicht normalisierte als auch eine normalisierte Konfusionsmatrix plotten.

```python
titles_options = [
    ("Confusion matrix, without normalization", None),
    ("Normalized confusion matrix", "true"),
]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
        classifier,
        X_test,
        y_test,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize=normalize,
    )
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)
plt.show()
```
