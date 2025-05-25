# Definir uma Função para Carregar o Conjunto de Dados MNIST

Definimos uma função `load_mnist()` para carregar o conjunto de dados MNIST, embaralhar os dados e retornar apenas o número especificado de amostras.

```python
def load_mnist(n_samples):
    """Load MNIST, shuffle the data, and return only n_samples."""
    mnist = fetch_openml("mnist_784", as_frame=False, parser="pandas")
    X, y = shuffle(mnist.data, mnist.target, random_state=2)
    return X[:n_samples] / 255, y[:n_samples]
```
