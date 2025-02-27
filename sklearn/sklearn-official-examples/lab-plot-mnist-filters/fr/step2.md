# Chargement des données

Ensuite, nous chargerons l'ensemble de données MNIST à l'aide de la fonction `fetch_openml` de Scikit-learn.

```python
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
