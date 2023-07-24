# Ensemble Methods

## Introduction

In this lab, we will explore ensemble methods using scikit-learn. Ensemble methods are machine learning techniques that combine multiple models to achieve better performance than a single model. We will specifically focus on two popular ensemble methods: Bagging and Random Forests.

## Steps

### Step 1: Import Dependencies

Let's start by importing the necessary dependencies.

```python
import numpy as np
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
```

### Step 2: Load the Data

Next, we will load the iris dataset from scikit-learn using the `load_iris` function.

```python
data = load_iris()
X, y = data.data, data.target
```

### Step 3: Split the Data

We will split the data into training and test sets using the `train_test_split` function from scikit-learn.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### Step 4: Fit a Bagging Classifier

Now, we will fit a Bagging Classifier on the training data. The Bagging Classifier is an ensemble method that uses bootstrap sampling to create multiple base models (often decision trees) and aggregates their predictions using majority voting.

```python
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X_train, y_train)
```

### Step 5: Evaluate the Bagging Classifier

Let's evaluate the Bagging Classifier by computing the accuracy score on the test data using the `score` method.

```python
accuracy = bagging.score(X_test, y_test)
print(f"Bagging Classifier Accuracy: {accuracy}")
```

### Step 6: Fit a Random Forest Classifier

Next, we will fit a Random Forest Classifier on the training data. The Random Forest Classifier is also an ensemble method that uses bootstrap sampling to create multiple decision trees, but it also adds additional randomness by considering only a subset of features at each split.

```python
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, y_train)
```

### Step 7: Evaluate the Random Forest Classifier

Let's evaluate the Random Forest Classifier by computing the accuracy score on the test data.

```python
accuracy = random_forest.score(X_test, y_test)
print(f"Random Forest Classifier Accuracy: {accuracy}")
```

## Summary

In this lab, we explored ensemble methods using scikit-learn. We fit a Bagging Classifier and a Random Forest Classifier on the iris dataset and evaluated their performance. Ensemble methods like Bagging and Random Forests can be powerful tools for improving the predictive performance of machine learning models.
