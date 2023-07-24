# Gradient Boosting Out-of-Bag estimates

## Introduction

This lab will guide you through implementing a Gradient Boosting Classifier with out-of-bag (OOB) estimates using the scikit-learn library in Python. OOB estimates are an alternative to cross-validation estimates and can be computed on-the-fly without the need for repeated model fitting. This lab will cover the following steps:

1. Generate data
2. Fit classifier with OOB estimates
3. Estimate best number of iterations using cross-validation
4. Compute best number of iterations for test data
5. Plot the results

## Steps

### Step 1: Generate Data

The first step is to generate some example data that we can use to train and test our model. We will use the `make_classification` function from the `sklearn.datasets` module to generate a random binary classification problem with 3 informative features.

```python
import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=3, n_informative=3,
                           n_redundant=0, n_classes=2, random_state=1)
```

### Step 2: Fit Classifier with OOB Estimates

Next, we will create a Gradient Boosting Classifier with OOB estimates using the `GradientBoostingClassifier` class from the `sklearn.ensemble` module. We will set the number of estimators to 100 and the learning rate to 0.1.

```python
from sklearn.ensemble import GradientBoostingClassifier

params = {
    "n_estimators": 100,
    "learning_rate": 0.1,
    "subsample": 1.0,
    "max_depth": 3,
    "min_samples_leaf": 1,
    "random_state": 1,
    "oob_score": True
}

clf = GradientBoostingClassifier(**params)
clf.fit(X, y)
```

### Step 3: Estimate Best Number of Iterations using Cross-Validation

We can estimate the best number of iterations using cross-validation. We will use 5-fold cross-validation and compute the negative log-loss for each number of iterations.

```python
from sklearn.model_selection import cross_val_score

cv_scores = []
for i in range(1, params['n_estimators'] + 1):
    clf.set_params(n_estimators=i)
    scores = -1 * cross_val_score(clf, X, y, cv=5, scoring='neg_log_loss')
    cv_scores.append(scores.mean())
```

### Step 4: Compute Best Number of Iterations for Test Data

We can also compute the best number of iterations for the test data. We will compute the negative log-loss for each number of iterations on the test data.

```python
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt

test_scores = []
for i, y_pred in enumerate(clf.staged_predict_proba(X)):
    score = log_loss(y, y_pred)
    test_scores.append(score)

best_n_estimators = np.argmin(test_scores) + 1
```

### Step 5: Plot the Results

Finally, we can plot the results to visualize the performance of the model for different numbers of iterations. We will plot the negative log-loss on the y-axis and the number of iterations on the x-axis.

```python
plt.figure(figsize=(10, 5))
plt.plot(range(1, params['n_estimators'] + 1), cv_scores, label='CV')
plt.plot(range(1, params['n_estimators'] + 1), test_scores, label='Test')
plt.axvline(x=best_n_estimators, color='red', linestyle='--')
plt.xlabel('Number of iterations')
plt.ylabel('Negative log-loss')
plt.legend()
plt.show()
```

## Summary

In this lab, we learned how to implement a Gradient Boosting Classifier with out-of-bag estimates and estimate the best number of iterations using cross-validation. We also computed the best number of iterations for the test data and plotted the results to visualize the performance of the model for different numbers of iterations.
