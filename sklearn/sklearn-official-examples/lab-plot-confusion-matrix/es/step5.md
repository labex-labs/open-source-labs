# Generar matriz de confusión

Generaremos una matriz de confusión utilizando la clase ConfusionMatrixDisplay de scikit-learn. La matriz de confusión mostrará la cantidad de predicciones correctas e incorrectas para cada clase.

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
