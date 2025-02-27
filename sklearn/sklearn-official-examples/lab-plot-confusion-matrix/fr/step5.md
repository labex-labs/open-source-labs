# Générer la matrice de confusion

Nous allons générer une matrice de confusion à l'aide de la classe ConfusionMatrixDisplay de scikit-learn. La matrice de confusion montrera le nombre de prédictions correctes et incorrectes pour chaque classe.

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
