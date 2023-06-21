# Load the data and model fitting

We begin by loading the Olivetti Faces dataset and limiting the dataset to contain only the first five classes. Then we train a random forest on the dataset and evaluate the impurity-based feature importance. We will set the number of cores to use for the tasks.

```python
from sklearn.datasets import fetch_olivetti_faces

# We select the number of cores to use to perform parallel fitting of
# the forest model. `-1` means use all available cores.
n_jobs = -1

# Load the faces dataset
data = fetch_olivetti_faces()
X, y = data.data, data.target

# Limit the dataset to 5 classes.
mask = y < 5
X = X[mask]
y = y[mask]

# A random forest classifier will be fitted to compute the feature importances.
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=750, n_jobs=n_jobs, random_state=42)

forest.fit(X, y)
```
