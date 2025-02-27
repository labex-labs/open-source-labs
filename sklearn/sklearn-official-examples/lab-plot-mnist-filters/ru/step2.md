# Загрузка данных

Далее мы загрузим набор данных MNIST с помощью функции `fetch_openml` из библиотеки Scikit-learn.

```python
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
