# New SequentialFeatureSelector Transformer

A new iterative transformer to select features is available: `SequentialFeatureSelector`. Sequential Feature Selection can add features one at a time (forward selection) or remove features from the list of available features (backward selection), based on a cross-validated score maximization.

```python
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

# load the iris dataset
X, y = load_iris(return_X_y=True, as_frame=True)
feature_names = X.columns

# create the classifier
knn = KNeighborsClassifier(n_neighbors=3)
sfs = SequentialFeatureSelector(knn, n_features_to_select=2)

# fit the model
sfs.fit(X, y)
print(
    "Features selected by forward sequential selection: "
    f"{feature_names[sfs.get_support()].tolist()}"
)
```


