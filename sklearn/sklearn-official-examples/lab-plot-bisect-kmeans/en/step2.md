# Generate Sample Data

In this step, we will generate sample data using the `make_blobs()` function from scikit-learn. We will generate 10000 samples with 2 centers.

```python
n_samples = 10000
random_state = 0
X, _ = make_blobs(n_samples=n_samples, centers=2, random_state=random_state)
```
