# 加载数据

接下来，我们将使用 Scikit-learn 的 `fetch_openml` 函数加载 MNIST 数据集。

```python
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
