# Evaluate the Model

We will evaluate the trained model on the testing and outlier data. We will use the predict method to predict the labels of the testing and outlier data. We will then count the number of errors in the testing and outlier data.

```python
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
