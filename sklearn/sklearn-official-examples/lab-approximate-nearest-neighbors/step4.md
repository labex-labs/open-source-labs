# Define a Function to Load MNIST Dataset

We define a function `load_mnist()` to load the MNIST dataset, shuffle the data, and return only the specified number of samples.

```python
def load_mnist(n_samples):
    """Load MNIST, shuffle the data, and return only n_samples."""
    mnist = fetch_openml("mnist_784", as_frame=False, parser="pandas")
    X, y = shuffle(mnist.data, mnist.target, random_state=2)
    return X[:n_samples] / 255, y[:n_samples]
```


