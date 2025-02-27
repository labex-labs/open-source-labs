# Cargar datos y definir tubería

Cargaremos el conjunto de datos de dígitos de scikit-learn y definiremos una tubería que consta de PCA y LinearSVC.

```python
pipe = Pipeline(
    [
        ("reduce_dim", PCA(random_state=42)),
        ("classify", LinearSVC(random_state=42, C=0.01, dual="auto")),
    ]
)

X, y = load_digits(return_X_y=True)
```
