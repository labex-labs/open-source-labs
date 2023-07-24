# Feature selection using SelectFromModel

The `SelectFromModel` class is a meta-transformer that can be used with any estimator that assigns importance to each feature. It selects features based on their importance and removes features below a specified threshold.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Initialize RandomForestClassifier as the estimator
estimator = RandomForestClassifier()

# Initialize SelectFromModel with the estimator and threshold of "mean"
selector = SelectFromModel(estimator, threshold="mean")

# Select the best features
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

In this example, we use a Random Forest Classifier as the estimator and select features with an importance greater than the mean importance. The output will show the original shape of the dataset and the shape after selecting the best features.
