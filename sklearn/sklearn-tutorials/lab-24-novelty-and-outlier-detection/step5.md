# Predict outliers

Once the model is fitted, we can use the `predict` method to predict whether new observations are outliers or not. The `predict` method returns 1 for inliers and -1 for outliers.

```python
X_test = [5.5, 8.5]
predictions = estimator.predict(X_test)
print(predictions)
```
