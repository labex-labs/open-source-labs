# Loading the Dataset

The `make_classification` function from the `sklearn.datasets` module is used to generate a classification dataset. The dataset contains 400 samples with 12 features. The code to load the dataset is as follows:

```python
rng = np.random.RandomState(0)
X, y = datasets.make_classification(n_samples=400, n_features=12, random_state=rng)
```


