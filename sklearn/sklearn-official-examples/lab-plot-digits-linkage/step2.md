# Load and Prepare the Dataset

We load the digits dataset and prepare it for clustering by extracting the data and target labels. We also set the random seed to zero to ensure reproducibility.

```python
digits = datasets.load_digits()
X, y = digits.data, digits.target
n_samples, n_features = X.shape
np.random.seed(0)
```


