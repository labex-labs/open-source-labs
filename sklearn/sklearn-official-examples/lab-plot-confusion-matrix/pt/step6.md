# Visualizar Matriz de Confusão

Visualizaremos a matriz de confusão usando matplotlib. Plotaremos tanto uma matriz de confusão não normalizada quanto uma matriz de confusão normalizada.

```python
titles_options = [
    ("Matriz de confusão, sem normalização", None),
    ("Matriz de confusão normalizada", "true"),
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
