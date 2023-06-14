# Selecting Features Based on Importance

We select the two features which are the most important according to the coefficients using `SelectFromModel`. `SelectFromModel` accepts a `threshold` parameter and will select the features whose importance (defined by the coefficients) are above this threshold.

```python
from sklearn.feature_selection import SelectFromModel

threshold = np.sort(importance)[-3] + 0.01

sfm = SelectFromModel(ridge, threshold=threshold).fit(X, y)
print(f"Features selected by SelectFromModel: {feature_names[sfm.get_support()]}")
```


