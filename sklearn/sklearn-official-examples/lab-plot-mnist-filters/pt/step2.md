# Carregar Dados

Em seguida, carregaremos o conjunto de dados MNIST usando a função `fetch_openml` do Scikit-learn.

```python
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
