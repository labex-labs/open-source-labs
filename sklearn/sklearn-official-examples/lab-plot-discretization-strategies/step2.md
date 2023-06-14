# Create Datasets

We will create three datasets for visualization purposes. The first dataset will be a random set of 200 samples from a uniform distribution between -3 and 3 in both dimensions. The second dataset will be a set of 200 samples generated using the `make_blobs` function from `sklearn.datasets`. The third dataset will also be generated using the `make_blobs` function.

```python
n_samples = 200
centers_0 = np.array([[0, 0], [0, 5], [2, 4], [8, 8]])
centers_1 = np.array([[0, 0], [3, 1]])

X_list = [
    np.random.RandomState(42).uniform(-3, 3, size=(n_samples, 2)),
    make_blobs(
        n_samples=[n_samples // 10, n_samples * 4 // 10, n_samples // 10, n_samples * 4 // 10],
        cluster_std=0.5,
        centers=centers_0,
        random_state=42,
    )[0],
    make_blobs(
        n_samples=[n_samples // 5, n_samples * 4 // 5],
        cluster_std=0.5,
        centers=centers_1,
        random_state=42,
    )[0],
]
```


