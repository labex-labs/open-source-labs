# Removing features with low variance

The `VarianceThreshold` class in scikit-learn can be used to remove features with low variance. Features with low variance typically do not provide much information for the model. We will demonstrate how to use `VarianceThreshold` to remove zero-variance features.

```python
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# Initialize VarianceThreshold with a threshold of 80% variability
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))

# Select features with high variability
X_selected = sel.fit_transform(X)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", sel.get_support(indices=True))
```

This code snippet demonstrates how to use `VarianceThreshold` to remove zero-variance features from a dataset. The output will show the original shape of the dataset and the shape after selecting features with high variability.
