# Scikit-Learn Tutorial

## Introduction

This tutorial will walk you through the new features and improvements in scikit-learn 0.24. Scikit-learn is a popular machine learning library in Python. It is built on top of NumPy, SciPy, and matplotlib. Scikit-learn has a variety of tools for machine learning including classification, regression, clustering, and dimensionality reduction.

## Steps

### Step 1: Successive Halving Estimators

Successive Halving is a new state-of-the-art method for exploring the space of hyper-parameters to identify the best combination. In this step, we will explore the `HalvingGridSearchCV` and `HalvingRandomSearchCV` classes that can be used as drop-in replacements for `GridSearchCV` and `RandomizedSearchCV`.

```python
import numpy as np
from scipy.stats import randint
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingRandomSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# create a random dataset
rng = np.random.RandomState(0)
X, y = make_classification(n_samples=700, random_state=rng)

# create a random forest classifier
clf = RandomForestClassifier(n_estimators=10, random_state=rng)

# set the parameter distribution
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 11),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}

# use HalvingRandomSearchCV to find the best parameters
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
rsh.fit(X, y)
print(rsh.best_params_)
```

### Step 2: Native Support for Categorical Features in HistGradientBoosting Estimators

`HistGradientBoostingClassifier` and `HistGradientBoostingRegressor` now have native support for categorical features. They can consider splits on non-ordered, categorical data. In this step, we will explore the new `categorical_features` parameter.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import HistGradientBoostingClassifier

# load the breast cancer dataset
data = load_breast_cancer()

# create the classifier
clf = HistGradientBoostingClassifier(
    max_iter=100, learning_rate=0.1, max_depth=3, random_state=0
)

# specify the categorical features
cat_features = [False] * data.data.shape[1]
cat_features[3] = True
cat_features[5] = True

# fit the model
clf.fit(data.data, data.target, categorical_features=cat_features)
```

### Step 3: Improved Performance of HistGradientBoosting Estimators

The memory footprint of `HistGradientBoostingRegressor` and `HistGradientBoostingClassifier` has been significantly improved during calls to `fit`. In addition, histogram initialization is now done in parallel which results in slight speed improvements.

### Step 4: New Self-Training Meta-Estimator

A new self-training implementation, based on Yarowski's algorithm can now be used with any classifier that implements `predict_proba`. The sub-classifier will behave as a semi-supervised classifier, allowing it to learn from unlabeled data.

```python
import numpy as np
from sklearn import datasets
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# load the iris dataset
iris = datasets.load_iris()

# add random unlabeled points
rng = np.random.RandomState(42)
random_unlabeled_points = rng.rand(iris.target.shape[0]) < 0.3
iris.target[random_unlabeled_points] = -1

# create the classifier
svc = SVC(probability=True, gamma="auto")
self_training_model = SelfTrainingClassifier(svc)

# fit the model
self_training_model.fit(iris.data, iris.target)
```

### Step 5: New SequentialFeatureSelector Transformer

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

### Step 6: New PolynomialCountSketch Kernel Approximation Function

The new `PolynomialCountSketch` approximates a polynomial expansion of a feature space when used with linear models, but uses much less memory than `PolynomialFeatures`.

```python
from sklearn.datasets import fetch_covtype
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.kernel_approximation import PolynomialCountSketch
from sklearn.linear_model import LogisticRegression

# load the covtype dataset
X, y = fetch_covtype(return_X_y=True)

# create the pipeline
pipe = make_pipeline(
    MinMaxScaler(),
    PolynomialCountSketch(degree=2, n_components=300),
    LogisticRegression(max_iter=1000),
)

# split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# fit the model
pipe.fit(X_train, y_train).score(X_test, y_test)
```

### Step 7: Individual Conditional Expectation Plots

A new kind of partial dependence plot is available: the Individual Conditional Expectation (ICE) plot. ICE plots visualize the dependence of the prediction on a feature for each sample separately, with one line per sample.

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.inspection import PartialDependenceDisplay

# load the california housing dataset
X, y = fetch_california_housing(return_X_y=True, as_frame=True)
features = ["MedInc", "AveOccup", "HouseAge", "AveRooms"]

# create the classifier
est = RandomForestRegressor(n_estimators=10)
est.fit(X, y)

# plot the ICE plot
display = PartialDependenceDisplay.from_estimator(
    est,
    X,
    features,
    kind="individual",
    subsample=50,
    n_jobs=3,
    grid_resolution=20,
    random_state=0,
)
display.figure_.suptitle(
    "Partial dependence of house value on non-location features\n"
    "for the California housing dataset, with BayesianRidge"
)
display.figure_.subplots_adjust(hspace=0.3)
```

### Step 8: New Poisson Splitting Criterion for DecisionTreeRegressor

`DecisionTreeRegressor` now supports a new 'poisson' splitting criterion. Setting `criterion="poisson"` might be a good choice if your target is a count or a frequency.

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import numpy as np

# create a random dataset
n_samples, n_features = 1000, 20
rng = np.random.RandomState(0)
X = rng.randn(n_samples, n_features)
y = rng.poisson(lam=np.exp(X[:, 5]) / 2)

# split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rng)

# create the regressor
regressor = DecisionTreeRegressor(criterion="poisson", random_state=0)

# fit the model
regressor.fit(X_train, y_train)
```

## Summary

In this tutorial, we explored the new features and improvements in scikit-learn 0.24. We learned about Successive Halving estimators for tuning hyper-parameters, native support for categorical features in HistGradientBoosting estimators, improved performances of HistGradientBoosting estimators, a new self-training meta-estimator, a new SequentialFeatureSelector transformer, a new PolynomialCountSketch kernel approximation function, Individual Conditional Expectation plots, and a new Poisson splitting criterion for DecisionTreeRegressor.
