# Scikit-learn Tutorial

## Introduction

Scikit-learn is a machine learning library in Python that provides tools for data mining and analysis. It features various classification, regression, and clustering algorithms including support vector machines, random forests, gradient boosting, k-means, and DBSCAN. In this tutorial, we will cover some of the new features in version 0.22 of scikit-learn.

## Steps

### Step 1: New plotting API

A new plotting API is available for creating visualizations. This new API allows for quickly adjusting the visuals of a plot without involving any recomputation. It is also possible to add different plots to the same figure.

```python
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import RocCurveDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

X, y = make_classification(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

svc = SVC(random_state=42)
svc.fit(X_train, y_train)
rfc = RandomForestClassifier(random_state=42)
rfc.fit(X_train, y_train)

svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=svc_disp.ax_)
rfc_disp.figure_.suptitle("ROC curve comparison")

plt.show()
```

### Step 2: Stacking Classifier and Regressor

StackingClassifier and StackingRegressor allow you to have a stack of estimators with a final classifier or a regressor. Stacked generalization consists of stacking the output of individual estimators and using a classifier to compute the final prediction.

```python
from sklearn.datasets import load_iris
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import StackingClassifier
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
estimators = [
    ("rf", RandomForestClassifier(n_estimators=10, random_state=42)),
    ("svr", make_pipeline(StandardScaler(), LinearSVC(random_state=42))),
]
clf = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
clf.fit(X_train, y_train).score(X_test, y_test)
```

### Step 3: Permutation-based feature importance

The permutation_importance function can be used to get an estimate of the importance of each feature for any fitted estimator.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance

X, y = make_classification(random_state=0, n_features=5, n_informative=3)
feature_names = np.array([f"x_{i}" for i in range(X.shape[1])])

rf = RandomForestClassifier(random_state=0).fit(X, y)
result = permutation_importance(rf, X, y, n_repeats=10, random_state=0, n_jobs=2)

fig, ax = plt.subplots()
sorted_idx = result.importances_mean.argsort()
ax.boxplot(
    result.importances[sorted_idx].T, vert=False, labels=feature_names[sorted_idx]
)
ax.set_title("Permutation Importance of each feature")
ax.set_ylabel("Features")
fig.tight_layout()
plt.show()
```

### Step 4: Native support for missing values for gradient boosting

The HistGradientBoostingClassifier and HistGradientBoostingRegressor now have native support for missing values (NaNs). This means that there is no need for imputing data when training or predicting.

```python
from sklearn.ensemble import HistGradientBoostingClassifier

X = np.array([0, 1, 2, np.nan]).reshape(-1, 1)
y = [0, 0, 1, 1]

gbdt = HistGradientBoostingClassifier(min_samples_leaf=1).fit(X, y)
print(gbdt.predict(X))
```

### Step 5: Precomputed sparse nearest neighbors graph

Most estimators based on nearest neighbors graphs now accept precomputed sparse graphs as input, to reuse the same graph for multiple estimator fits.

```python
from tempfile import TemporaryDirectory
from sklearn.neighbors import KNeighborsTransformer
from sklearn.manifold import Isomap
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_classification

X, y = make_classification(random_state=0)

with TemporaryDirectory(prefix="sklearn_cache_") as tmpdir:
    estimator = make_pipeline(
        KNeighborsTransformer(n_neighbors=10, mode="distance"),
        Isomap(n_neighbors=10, metric="precomputed"),
        memory=tmpdir,
    )
    estimator.fit(X)

    estimator.set_params(isomap__n_neighbors=5)
    estimator.fit(X)
```

### Step 6: KNN Based Imputation

We now support imputation for completing missing values using k-Nearest Neighbors. Each sample's missing values are imputed using the mean value from n_neighbors nearest neighbors found in the training set.

```python
from sklearn.impute import KNNImputer

X = [[1, 2, np.nan], [3, 4, 3], [np.nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
print(imputer.fit_transform(X))
```

### Step 7: Tree pruning

It is now possible to prune most tree-based estimators once the trees are built. The pruning is based on minimal cost-complexity.

```python
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

X, y = make_classification(random_state=0)

rf = RandomForestClassifier(random_state=0, ccp_alpha=0).fit(X, y)
print(
    "Average number of nodes without pruning {:.1f}".format(
        np.mean([e.tree_.node_count for e in rf.estimators_])
    )
)

rf = RandomForestClassifier(random_state=0, ccp_alpha=0.05).fit(X, y)
print(
    "Average number of nodes with pruning {:.1f}".format(
        np.mean([e.tree_.node_count for e in rf.estimators_])
    )
)
```

### Step 8: Retrieve dataframes from OpenML

fetch_openml can now return pandas dataframe and thus properly handle datasets with heterogeneous data.

```python
from sklearn.datasets import fetch_openml

titanic = fetch_openml("titanic", version=1, as_frame=True, parser="pandas")
print(titanic.data.head()[["pclass", "embarked"]])
```

### Step 9: Checking scikit-learn compatibility of an estimator

Developers can check the compatibility of their scikit-learn compatible estimators using check_estimator.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils.estimator_checks import parametrize_with_checks

@parametrize_with_checks([LogisticRegression(), DecisionTreeRegressor()])
def test_sklearn_compatible_estimator(estimator, check):
    check(estimator)
```

### Step 10: ROC AUC now supports multiclass classification

The roc_auc_score function can also be used in multi-class classification.

```python
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score

X, y = make_classification(n_classes=4, n_informative=16)
clf = SVC(decision_function_shape="ovo", probability=True).fit(X, y)
print(roc_auc_score(y, clf.predict_proba(X), multi_class="ovo"))
```

## Summary

In this tutorial, we covered some of the new features in version 0.22 of scikit-learn. These features include a new plotting API, Stacking Classifier and Regressor, permutation-based feature importance, native support for missing values for gradient boosting, precomputed sparse nearest neighbors graph, KNN based imputation, tree pruning, retrieving dataframes from OpenML, checking scikit-learn compatibility of an estimator, and ROC AUC now supports multiclass classification.
