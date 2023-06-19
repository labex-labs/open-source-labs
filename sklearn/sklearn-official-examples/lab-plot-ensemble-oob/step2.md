# Generate a Binary Classification Dataset

Next, we will generate a binary classification dataset using the `make_classification` function provided by scikit-learn. This function allows us to specify the number of samples, features, clusters per class, and informative features. We will use a fixed random state value to ensure reproducibility.

```python
X, y = make_classification(
    n_samples=500,
    n_features=25,
    n_clusters_per_class=1,
    n_informative=15,
    random_state=RANDOM_STATE,
)
```


