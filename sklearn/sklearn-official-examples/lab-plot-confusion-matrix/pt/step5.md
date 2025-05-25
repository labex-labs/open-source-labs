# Gerar Matriz de Confusão

Geraremos uma matriz de confusão usando a classe ConfusionMatrixDisplay do scikit-learn. A matriz de confusão mostrará o número de previsões corretas e incorretas para cada classe.

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
