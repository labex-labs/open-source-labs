# Hyperparameter Optimization: Randomized Search vs Grid Search

## Introduction

In machine learning, hyperparameters are parameters that are not learned from data, but rather set prior to training. Selecting appropriate hyperparameters is crucial to achieving high accuracy in machine learning models. Two common methods for hyperparameter optimization are randomized search and grid search. In this lab, we will compare these two methods for optimizing hyperparameters of a linear Support Vector Machine (SVM) with Stochastic Gradient Descent (SGD) training.

## Steps

### Step 1: Import necessary libraries and load data

We will start by importing the necessary libraries and loading the digits dataset from scikit-learn.

```python
import numpy as np
from time import time
import scipy.stats as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier

# load digits dataset
X, y = load_digits(return_X_y=True, n_class=3)
```

### Step 2: Create an SVM model

We will create a linear SVM model with SGD training.

```python
# create SVM model with SGD training
clf = SGDClassifier(loss="hinge", penalty="elasticnet", fit_intercept=True)
```

### Step 3: Randomized search for hyperparameter optimization

We will use randomized search to explore the hyperparameter space and find the best hyperparameters for our SVM model.

```python
# specify parameters and distributions to sample from
param_dist = {
    "average": [True, False],
    "l1_ratio": stats.uniform(0, 1),
    "alpha": stats.loguniform(1e-2, 1e0),
}

# run randomized search
n_iter_search = 15
random_search = RandomizedSearchCV(
    clf, param_distributions=param_dist, n_iter=n_iter_search
)

start = time()
random_search.fit(X, y)
print(
    "RandomizedSearchCV took %.2f seconds for %d candidates parameter settings."
    % ((time() - start), n_iter_search)
)

# print results
report(random_search.cv_results_)
```

### Step 4: Grid search for hyperparameter optimization

We will use grid search to explore the hyperparameter space and find the best hyperparameters for our SVM model.

```python
# specify parameters to search over
param_grid = {
    "average": [True, False],
    "l1_ratio": np.linspace(0, 1, num=10),
    "alpha": np.power(10, np.arange(-2, 1, dtype=float)),
}

# run grid search
grid_search = GridSearchCV(clf, param_grid=param_grid)

start = time()
grid_search.fit(X, y)

print(
    "GridSearchCV took %.2f seconds for %d candidate parameter settings."
    % (time() - start, len(grid_search.cv_results_["params"]))
)

# print results
report(grid_search.cv_results_)
```

## Summary

In this lab, we compared randomized search and grid search for hyperparameter optimization of a linear SVM model with SGD training. We found that both methods explored the same hyperparameter space, but randomized search was significantly faster. The best hyperparameters found by each method were similar in performance, but randomized search may have slightly worse performance due to noise. In practice, we would not search over so many hyperparameters simultaneously, but only the most important ones.
