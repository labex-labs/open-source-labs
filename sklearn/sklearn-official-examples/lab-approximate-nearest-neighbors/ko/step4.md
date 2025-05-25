# MNIST 데이터셋 로드 함수 정의

MNIST 데이터셋을 로드하고, 데이터를 섞은 후 지정된 샘플 수만 반환하는 함수 `load_mnist()`를 정의합니다.

```python
def load_mnist(n_samples):
    """Load MNIST, shuffle the data, and return only n_samples."""
    mnist = fetch_openml("mnist_784", as_frame=False, parser="pandas")
    X, y = shuffle(mnist.data, mnist.target, random_state=2)
    return X[:n_samples] / 255, y[:n_samples]
```
