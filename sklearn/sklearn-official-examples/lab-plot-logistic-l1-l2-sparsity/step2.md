# Load the Dataset

We will load the digits dataset using `datasets.load_digits(return_X_y=True)`. We will also standardize the data using `StandardScaler().fit_transform(X)`. The target variable will be binary, where 0-4 will be classified as 0 and 5-9 will be classified as 1.

```python
X, y = datasets.load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X)
y = (y > 4).astype(int)
```


