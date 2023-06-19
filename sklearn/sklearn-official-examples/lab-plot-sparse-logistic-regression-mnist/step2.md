# Load the MNIST dataset

We will load the MNIST dataset using the `fetch_openml` function from scikit-learn. We will also select a subset of the data by setting the number of `train_samples` to 5000.

```python
# Turn down for faster convergence
t0 = time.time()
train_samples = 5000

# Load data from https://www.openml.org/d/554
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```


