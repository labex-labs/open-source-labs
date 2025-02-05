# Recursive feature elimination

Recursive feature elimination (RFE) is a feature selection method that recursively considers smaller and smaller sets of features to select the most important ones. It works by training an external estimator with weights assigned to features and pruning the least important features.

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Initialize SVC as the external estimator
estimator = SVC(kernel="linear")

# Initialize RFE with the external estimator and select 2 features
selector = RFE(estimator, n_features_to_select=2)

# Select the best features
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

In this example, we use a Support Vector Classifier (SVC) as the external estimator and select the two best features from the Iris dataset. The output will show the original shape of the dataset and the shape after selecting the best features.
