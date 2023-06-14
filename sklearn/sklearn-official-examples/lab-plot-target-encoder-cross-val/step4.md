# Train a Ridge Regressor on Raw Data

In this section, we will train a Ridge regressor on the dataset with and without encoding and explore the influence of target encoder with and without the interval cross-validation. First, we will train a Ridge model on the raw features. Run the following code to train the Ridge model:

```python
ridge = Ridge(alpha=1e-6, solver="lsqr", fit_intercept=False)

raw_model = ridge.fit(X_train, y_train)
print("Raw Model score on training set: ", raw_model.score(X_train, y_train))
print("Raw Model score on test set: ", raw_model.score(X_test, y_test))
```


