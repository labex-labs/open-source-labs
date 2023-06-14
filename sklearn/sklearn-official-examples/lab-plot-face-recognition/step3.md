# Data Preprocessing

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

We split the dataset into a training set and a test set and preprocess the data by scaling the input data using the `StandardScaler()` function.


