# Tuning Hyperparameters of an Estimator

## Introduction

Hyperparameters are parameters that are not directly learned by an estimator. They are passed as arguments to the constructor of the estimator classes. Tuning the hyperparameters of an estimator is an important step in building effective machine learning models. It involves finding the optimal combination of hyperparameters that result in the best performance of the model.

Scikit-learn provides several tools to search for the best hyperparameters: `GridSearchCV` and `RandomizedSearchCV`. In this lab, we will walk through the process of tuning hyperparameters using these tools.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the necessary libraries for our analysis. We will be using `sklearn.model_selection` to perform the hyperparameter tuning.

```python
import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
```

### Step 2: Load the dataset

Next, let's load the dataset that we will be working with. We can use any dataset of our choice for this exercise.

```python
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Split the data into features and target
X = iris.data
y = iris.target
```

### Step 3: Define the estimator and parameter grid

Now we need to define the estimator that we want to tune and the parameter grid that we want to search. The parameter grid specifies the values that we want to try for each hyperparameter.

```python
from sklearn.svm import SVC

# Create an instance of the support vector classifier
svc = SVC()

# Define the parameter grid
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 0.01, 0.001], 'kernel': ['linear', 'rbf']}
```

### Step 4: Perform grid search with cross-validation

Grid search exhaustively searches through all possible combinations of hyperparameters in the specified parameter grid. It evaluates the performance of each combination using cross-validation.

```python
# Create an instance of GridSearchCV
grid_search = GridSearchCV(svc, param_grid, cv=5)

# Fit the data to perform grid search
grid_search.fit(X, y)

# Print the best combination of hyperparameters
print('Best hyperparameters:', grid_search.best_params_)
```

### Step 5: Perform randomized search with cross-validation

Randomized search randomly samples a subset of the parameter grid and evaluates the performance of each combination using cross-validation. It is useful when the parameter space is large and searching exhaustively is not feasible.

```python
# Create an instance of RandomizedSearchCV
random_search = RandomizedSearchCV(svc, param_grid, cv=5, n_iter=10, random_state=0)

# Fit the data to perform randomized search
random_search.fit(X, y)

# Print the best combination of hyperparameters
print('Best hyperparameters:', random_search.best_params_)
```

## Summary

In this lab, we learned how to tune the hyperparameters of an estimator using `GridSearchCV` and `RandomizedSearchCV`. We defined the estimator and the parameter grid, and then performed grid search and randomized search, respectively, to find the best combination of hyperparameters. Hyperparameter tuning is an important step in building machine learning models to improve their performance.
