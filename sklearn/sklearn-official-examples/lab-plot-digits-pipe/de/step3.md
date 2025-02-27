# Laden des Datensatzes und Definieren von Parametern für GridSearchCV

Wir laden den digits-Datensatz und definieren die Parameter für GridSearchCV. Wir legen den Parameter für die PCA-Abschneidung und die Klassifizierer-Regularisierung fest.

```python
X_digits, y_digits = datasets.load_digits(return_X_y=True)

param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
```
