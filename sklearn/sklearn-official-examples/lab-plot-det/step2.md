# Define the Classifiers

We will define two different classifiers to compare their statistical performance across thresholds using ROC and DET curves. We will use scikit-learn's `make_pipeline` function to create a pipeline that scales the data using `StandardScaler` and trains a `LinearSVC` classifier. We will also use scikit-learn's `RandomForestClassifier` class to train a random forest classifier with a maximum depth of 5, 10 estimators, and a maximum of 1 feature.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

classifiers = {
    "Linear SVM": make_pipeline(StandardScaler(), LinearSVC(C=0.025, dual="auto")),
    "Random Forest": RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1
    ),
}
```


