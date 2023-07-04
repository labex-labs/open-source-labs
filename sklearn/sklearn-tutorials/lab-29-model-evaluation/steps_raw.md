# Model Evaluation

## Introduction

In machine learning, it is important to evaluate the quality of the predictions made by a model. This helps us understand how well the model is performing and whether it can be trusted for making accurate predictions. The scikit-learn library provides several metrics and scoring methods to quantify the quality of predictions.

In this lab, we will explore three different APIs provided by scikit-learn for model evaluation: the Estimator score method, the scoring parameter, and the metric functions.

## Steps

### Step 1: Estimator Score Method

The Estimator score method is a default evaluation criterion provided by scikit-learn for each estimator. It calculates a score that represents the quality of the model's predictions. You can find more information about this in the documentation of each estimator.

Here's an example of using the `score` method for an estimator:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Score:", score)
```

### Step 2: Scoring Parameter

Scikit-learn provides a `scoring` parameter in several model evaluation tools, such as cross-validation and grid search. The `scoring` parameter controls the metric applied to the estimators during evaluation.

Here's an example of using the `scoring` parameter with cross-validation:

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("Scores:", scores)
```

### Step 3: Metric Functions

The scikit-learn `metrics` module implements several functions for assessing prediction error for specific purposes. These functions can be used to calculate the quality of predictions made by a model.

Here's an example of using the `accuracy_score` function from the `metrics` module:

```python
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

## Summary

In this lab, we learned about three different APIs provided by scikit-learn for model evaluation: the Estimator score method, the scoring parameter, and the metric functions. These APIs allow us to evaluate the quality of predictions made by a model and understand how well the model is performing.
