# Predict on New Data

We will use both the random forest regressor and the multi-output regressor to make predictions on our testing data.

```python
y_rf = regr_rf.predict(X_test)
y_multirf = regr_multirf.predict(X_test)
```


