# Generate a Regression Dataset

We will generate a regression dataset with the given parameters using Scikit-Learn's `make_regression` function. The dataset will have `n_train` training instances, `n_test` testing instances, `n_features` features, and `noise` of 0.1.

```python
X, y, coef = make_regression(
    n_samples=n_train + n_test, n_features=n_features, noise=noise, coef=True
)

random_seed = 13
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_train, test_size=n_test, random_state=random_seed
)
X_train, y_train = shuffle(X_train, y_train, random_state=random_seed)

X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

y_scaler = StandardScaler()
y_train = y_scaler.fit_transform(y_train[:, None])[:, 0]
y_test = y_scaler.transform(y_test[:, None])[:, 0]
```


