# Train a Ridge Regressor with Cross Validation

Next, we will create a pipeline with the `TargetEncoder` and Ridge model. The pipeline uses `TargetEncoder.fit_transform` which uses cross-validation. Run the following code to train the Ridge model with cross-validation:

```python
model_with_cv = make_pipeline(TargetEncoder(random_state=0), ridge)
model_with_cv.fit(X_train, y_train)
print("Model with CV on training set: ", model_with_cv.score(X_train, y_train))
print("Model with CV on test set: ", model_with_cv.score(X_test, y_test))
```


