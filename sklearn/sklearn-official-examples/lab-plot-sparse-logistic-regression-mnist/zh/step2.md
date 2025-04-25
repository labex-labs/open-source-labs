# 加载 MNIST 数据集

我们将使用 scikit-learn 中的`fetch_openml`函数来加载 MNIST 数据集。我们还将通过将`train_samples`的数量设置为 5000 来选择数据的一个子集。

```python
# Turn down for faster convergence
t0 = time.time()
train_samples = 5000

# Load data from https://www.openml.org/d/554
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
