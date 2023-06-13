# Selecting Features with Sequential Feature Selection

We use Sequential Feature Selector (SFS) to select features. SFS is a greedy procedure where, at each iteration, we choose the best new feature to add to our selected features based on a cross-validation score. We can also go in the reverse direction (backward SFS), i.e. start with all the features and greedily choose features to remove one by one.

```python
from sklearn.feature_selection import SequentialFeatureSelector

sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="forward").fit(X, y)
sfs_backward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="backward").fit(X, y)

print(f"Features selected by forward sequential selection: {feature_names[sfs_forward.get_support()]}")
print(f"Features selected by backward sequential selection: {feature_names[sfs_backward.get_support()]}")
```

#
