# Model Selection: Choosing Estimators and Their Parameters

## Introduction

In machine learning, model selection is the process of choosing the best model for a given dataset. It involves selecting the appropriate estimator and tuning its parameters to achieve optimal performance. This tutorial will guide you through the process of model selection in scikit-learn.

## Steps

### Step 1: Score and Cross-Validated Scores

Estimators in scikit-learn expose a `score` method that can be used to assess the quality of the model's fit or prediction on new data. This method returns a score, where a higher value indicates better performance.

```python
from sklearn import datasets, svm

# Load the digits dataset
X_digits, y_digits = datasets.load_digits(return_X_y=True)

# Create an SVM classifier with linear kernel
svc = svm.SVC(C=1, kernel='linear')

# Fit the classifier on the training data and calculate the score on the test data
score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
```

To get a better measure of prediction accuracy, we can use cross-validation. Cross-validation involves splitting the data into multiple folds, using each fold as a test set and the remaining folds as training sets. This process is repeated multiple times, and the scores are averaged to get the overall performance.

```python
import numpy as np

# Split the data into 3 folds
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

# Perform cross-validation
scores = []
for k in range(3):
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)
```

### Step 2: Cross-Validation Generators

Scikit-learn provides a collection of classes that can be used to generate train/test indices for popular cross-validation strategies. These classes have a `split` method that accepts the input dataset and yields the train/test set indices for each iteration of the cross-validation process.

```python
from sklearn.model_selection import KFold

# Split the data into K folds using KFold cross-validation
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X_digits):
    print(f'Train: {train_indices} | test: {test_indices}')
```

The `cross_val_score` helper function can be used to calculate the cross-validation score directly. It splits the data into training and test sets for each iteration of cross-validation, trains the estimator on the training set, and computes the score based on the test set.

```python
from sklearn.model_selection import cross_val_score

# Calculate the cross-validation score for the SVM classifier
scores = cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
print(scores)
```

### Step 3: Grid-Search

Grid-search is a technique that can be used to find the best combination of parameter values for an estimator. It involves specifying a grid of parameter values, fitting the estimator on the training data for each combination of parameters, and selecting the parameters that result in the highest cross-validation score.

```python
from sklearn.model_selection import GridSearchCV

# Define a grid of parameter values
Cs = np.logspace(-6, -1, 10)

# Create a GridSearchCV object with the SVM classifier and the parameter grid
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)

# Fit the GridSearchCV object on the training data
clf.fit(X_digits[:1000], y_digits[:1000])

print(clf.best_score_)
print(clf.best_estimator_.C)
```

### Step 4: Cross-Validated Estimators

Some estimators in scikit-learn have built-in cross-validation capabilities. These cross-validated estimators automatically select their parameters by cross-validation, making the model selection process more efficient.

```python
from sklearn import linear_model, datasets

# Create a LassoCV object
lasso = linear_model.LassoCV()

# Load the diabetes dataset
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)

# Fit the LassoCV object on the dataset
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
```

## Summary

In this tutorial, we learned about the process of model selection in scikit-learn. We explored scoring methods, cross-validation, grid-search, and cross-validated estimators. By following these steps, you can choose the best estimator for a given dataset and tune its parameters to achieve optimal performance.
