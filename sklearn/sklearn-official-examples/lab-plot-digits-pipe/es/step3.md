# Cargar el conjunto de datos y definir parámetros para GridSearchCV

Cargaremos el conjunto de datos de dígitos y definiremos los parámetros para GridSearchCV. Estableceremos el parámetro para el truncamiento del PCA y la regularización del clasificador.

```python
X_digits, y_digits = datasets.load_digits(return_X_y=True)

param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
```
