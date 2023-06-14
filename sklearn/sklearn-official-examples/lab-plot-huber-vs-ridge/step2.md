# Generate Toy Data

We will now generate a toy dataset using make_regression function from scikit-learn. We will generate a dataset with 20 samples, one feature, and a random seed of 0. We will also add some noise to the dataset.

```python
rng = np.random.RandomState(0)
X, y = make_regression(
    n_samples=20, n_features=1, random_state=0, noise=4.0, bias=100.0
)
```


