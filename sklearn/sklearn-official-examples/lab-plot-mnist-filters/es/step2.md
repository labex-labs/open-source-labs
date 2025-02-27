# Cargar datos

A continuación, cargaremos el conjunto de datos MNIST utilizando la función `fetch_openml` de Scikit-learn.

```python
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
