# Keeping the number of features constant

By default, scikit-learn imputers drop columns containing only missing values. However, in some cases, it is necessary to keep the empty features to maintain the shape of the data. We can achieve this by setting the `keep_empty_features` parameter to True.

```python
imputer = SimpleImputer(keep_empty_features=True)
X = np.array([[np.nan, 1], [np.nan, 2], [np.nan, 3]])
imputed_X = imputer.fit_transform(X)
```
