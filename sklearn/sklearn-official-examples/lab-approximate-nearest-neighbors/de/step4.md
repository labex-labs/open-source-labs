# Definieren Sie eine Funktion zum Laden des MNIST-Datensatzes

Wir definieren eine Funktion `load_mnist()`, um den MNIST-Datensatz zu laden, die Daten zu mischen und nur die angegebene Anzahl von Proben zurückzugeben.

```python
def load_mnist(n_samples):
    """Laden Sie MNIST, mischen Sie die Daten und geben Sie nur n_samples zurück."""
    mnist = fetch_openml("mnist_784", as_frame=False, parser="pandas")
    X, y = shuffle(mnist.data, mnist.target, random_state=2)
    return X[:n_samples] / 255, y[:n_samples]
```
