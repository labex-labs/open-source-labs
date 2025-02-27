# Definir una función para cargar el conjunto de datos MNIST

Definimos una función `load_mnist()` para cargar el conjunto de datos MNIST, mezclar los datos y devolver solo un número específico de muestras.

```python
def load_mnist(n_samples):
    """Cargar MNIST, mezclar los datos y devolver solo n_samples."""
    mnist = fetch_openml("mnist_784", as_frame=False, parser="pandas")
    X, y = shuffle(mnist.data, mnist.target, random_state=2)
    return X[:n_samples] / 255, y[:n_samples]
```
