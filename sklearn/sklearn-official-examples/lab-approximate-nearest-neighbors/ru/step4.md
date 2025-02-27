# Определяем функцию для загрузки датасета MNIST

Мы определяем функцию `load_mnist()`, чтобы загрузить датасет MNIST, перемешать данные и вернуть только указанное количество образцов.

```python
def load_mnist(n_samples):
    """Load MNIST, shuffle the data, and return only n_samples."""
    mnist = fetch_openml("mnist_784", as_frame=False, parser="pandas")
    X, y = shuffle(mnist.data, mnist.target, random_state=2)
    return X[:n_samples] / 255, y[:n_samples]
```
