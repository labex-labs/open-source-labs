# Définir une fonction pour charger l'ensemble de données MNIST

Nous définissons une fonction `load_mnist()` pour charger l'ensemble de données MNIST, mélanger les données et ne renvoyer que le nombre spécifié d'échantillons.

```python
def load_mnist(n_samples):
    """Charge MNIST, mélange les données et ne renvoie que n_samples."""
    mnist = fetch_openml("mnist_784", as_frame=False, parser="pandas")
    X, y = shuffle(mnist.data, mnist.target, random_state=2)
    return X[:n_samples] / 255, y[:n_samples]
```
