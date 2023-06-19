# Predict data of estimated models

We will predict the data of the linear model and the RANSAC regressor and compare their results.

```python
# Predict data of estimated models
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)
```
