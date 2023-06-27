# Generate Training Data

In this step, we will generate some training data from clustering. We will use the `make_blobs` function from scikit-learn to generate 5000 samples with 3 clusters having different standard deviations and centers.

```python
X, y = make_blobs(
    n_samples=5000,
    cluster_std=[1.0, 1.0, 0.5],
    centers=[(-5, -5), (0, 0), (5, 5)],
    random_state=42,
)
```
