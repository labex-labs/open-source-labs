# 定义一个加载 MNIST 数据集的函数

我们定义一个函数 `load_mnist()` 来加载 MNIST 数据集，对数据进行洗牌（打乱顺序），并仅返回指定数量的样本。

```python
def load_mnist(n_samples):
    """Load MNIST, shuffle the data, and return only n_samples."""
    mnist = fetch_openml("mnist_784", as_frame=False, parser="pandas")
    X, y = shuffle(mnist.data, mnist.target, random_state=2)
    return X[:n_samples] / 255, y[:n_samples]
```
