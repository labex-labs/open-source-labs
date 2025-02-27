# MNISTデータセットを読み込む関数を定義する

MNISTデータセットを読み込み、データをシャッフルし、指定されたサンプル数だけを返す関数`load_mnist()`を定義します。

```python
def load_mnist(n_samples):
    """Load MNIST, shuffle the data, and return only n_samples."""
    mnist = fetch_openml("mnist_784", as_frame=False, parser="pandas")
    X, y = shuffle(mnist.data, mnist.target, random_state=2)
    return X[:n_samples] / 255, y[:n_samples]
```
