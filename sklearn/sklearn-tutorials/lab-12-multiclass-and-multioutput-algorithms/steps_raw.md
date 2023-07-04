# Multiclass and Multioutput Algorithms

## Introduction

In this lab, we will explore the functionality and usage of multiclass and multioutput algorithms in scikit-learn. Multiclass classification is a classification task where samples are assigned to more than two classes. Multioutput classification, on the other hand, predicts multiple properties for each sample. We will cover the following topics:

1. Multiclass Classification
2. Multilabel Classification
3. Multiclass-Multioutput Classification
4. Multioutput Regression

## Steps

### Step 1: Multiclass Classification

#### Problem Description

Multiclass classification is a classification task with more than two classes. Each sample is assigned to only one class.

#### Target Format

A valid representation of multiclass targets is a 1D or column vector containing more than two discrete values.

#### Example

Let's use the Iris dataset to demonstrate multiclass classification:

```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Fit a logistic regression model using OneVsRestClassifier
model = OneVsRestClassifier(LogisticRegression())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```

### Step 2: Multilabel Classification

#### Problem Description

Multilabel classification is a classification task where each sample can be assigned multiple labels. The number of labels each sample can have is greater than two.

#### Target Format

A valid representation of multilabel targets is a binary matrix, where each row represents a sample and each column represents a class. A value of 1 indicates the presence of the label in the sample, while 0 or -1 indicates the absence.

#### Example

Let's create a multilabel classification problem using the make_classification function:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

# Generate a multilabel classification problem
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
y = y.reshape(-1, 1)

# Fit a multioutput random forest classifier
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```

### Step 3: Multiclass-Multioutput Classification

#### Problem Description

Multiclass-multioutput classification, also known as multitask classification, predicts multiple non-binary properties for each sample. Each property can have more than two classes.

#### Target Format

A valid representation of multiclass-multioutput targets is a dense matrix, where each row represents a sample and each column represents a different property or class.

#### Example

Let's create a multiclass-multioutput classification problem using the make_classification function:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC

# Generate a multiclass-multioutput classification problem
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=3, random_state=0)

# Fit a multioutput support vector classifier
model = MultiOutputClassifier(SVC())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```

### Step 4: Multioutput Regression

#### Problem Description

Multioutput regression predicts multiple numerical properties for each sample. Each property is a numerical variable, and the number of properties can be greater than or equal to two.

#### Target Format

A valid representation of multioutput regression targets is a dense matrix, where each row represents a sample and each column represents a different property.

#### Example

Let's create a multioutput regression problem using the make_regression function:

```python
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression

# Generate a multioutput regression problem
X, y = make_regression(n_samples=100, n_features=10, n_targets=3, random_state=0)

# Fit a multioutput linear regression model
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```

## Summary

In this lab, we explored multiclass and multioutput algorithms in scikit-learn. We covered multiclass classification, multilabel classification, multiclass-multioutput classification, and multioutput regression. These algorithms allow us to solve complex classification and regression tasks with multiple targets or classes.
