# Fit the Model for Outlier Detection

We will use `LocalOutlierFactor` to fit the model for outlier detection and compute the predicted labels of the training samples.

```python
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(X)
X_scores = clf.negative_outlier_factor_
```
