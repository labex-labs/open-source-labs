# Generate Dataset

We will generate a 3-class dataset using the `make_blobs` function from scikit-learn. We will use 1000 samples and set the centers of the blobs to be at `[-5, 0], [0, 1.5], [5, -1]`. We will then transform the dataset using a transformation matrix to make the dataset more difficult to classify.

```python
centers = [[-5, 0], [0, 1.5], [5, -1]]
X, y = make_blobs(n_samples=1000, centers=centers, random_state=40)
transformation = [[0.4, 0.2], [-0.4, 1.2]]
X = np.dot(X, transformation)
```


