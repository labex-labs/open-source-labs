# Visualiser la matrice de confusion

Nous allons visualiser la matrice de confusion à l'aide de matplotlib. Nous allons tracer à la fois une matrice de confusion non normalisée et une matrice de confusion normalisée.

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
