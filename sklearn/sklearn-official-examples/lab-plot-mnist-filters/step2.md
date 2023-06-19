# Load Data

Next, we will load the MNIST dataset using Scikit-learn's `fetch_openml` function.

```python
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```


