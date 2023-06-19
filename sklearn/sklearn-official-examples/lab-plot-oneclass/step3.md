# Calculate the number of errors

We will calculate the number of errors made by the model on the training data, regular novel observations, and abnormal novel observations.

```python
# Count the number of errors
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
