# Train a Ridge Regressor without Cross Validation

While `TargetEncoder.fit_transform` uses interval cross-validation, `TargetEncoder.transform` itself does not perform any cross-validation. It uses the aggregation of the complete training set to transform the categorical features. Thus, we can use `TargetEncoder.fit` followed by `TargetEncoder.transform` to disable the cross-validation. This encoding is then passed to the Ridge model. Run the following code to train the Ridge model without cross-validation:

```python
target_encoder = TargetEncoder(random_state=0)
target_encoder.fit(X_train, y_train)
X_train_no_cv_encoding = target_encoder.transform(X_train)
X_test_no_cv_encoding = target_encoder.transform(X_test)

model_no_cv = ridge.fit(X_train_no_cv_encoding, y_train)
print(
    "Model without CV on training set: ",
    model_no_cv.score(X_train_no_cv_encoding, y_train),
)
print(
    "Model without CV on test set: ", model_no_cv.score(X_test_no_cv_encoding, y_test)
)
```


