# Multivariate feature imputation using IterativeImputer

The `IterativeImputer` class is a more advanced approach to imputing missing values. It models each feature with missing values as a function of other features and uses that estimate for imputation. It iteratively learns the relationships between features and imputes the missing values based on these relationships.

```python
imp = IterativeImputer()
X = [[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
imputed_X_test = imp.transform(X_test)
```
