# Stochastic Gradient Descent

## Introduction

In this lab, we will explore Stochastic Gradient Descent (SGD), which is a powerful optimization algorithm commonly used in machine learning for solving large-scale and sparse problems. We will learn how to use the SGDClassifier and SGDRegressor classes from the scikit-learn library to train linear classifiers and regressors.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the necessary libraries. We will be using the scikit-learn library for machine learning and data preprocessing.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
```

### Step 2: Load and preprocess the data

Next, we will load the iris dataset and preprocess it by scaling the features using StandardScaler.

```python
# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```

### Step 3: Train a classifier using SGD

Now we will train a classifier using the SGDClassifier class. We will use the log_loss loss function and the l2 penalty.

```python
# Train a classifier using SGD
clf = SGDClassifier(loss="log", penalty="l2", max_iter=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = clf.predict(X_test)

# Measure the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Classifier Accuracy:", accuracy)
```

### Step 4: Train a regressor using SGD

Next, we will train a regressor using the SGDRegressor class. We will use the squared_error loss function and the l2 penalty.

```python
# Train a regressor using SGD
reg = SGDRegressor(loss="squared_error", penalty="l2", max_iter=100, random_state=42)
reg.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = reg.predict(X_test)

# Measure the mean squared error of the regressor
mse = mean_squared_error(y_test, y_pred)

# Print the mean squared error
print("Regressor Mean Squared Error:", mse)
```

## Summary

In this lab, we learned how to use Stochastic Gradient Descent (SGD) for training linear classifiers and regressors using the scikit-learn library. We trained a classifier on the iris dataset and measured its accuracy, and we trained a regressor and measured its mean squared error. SGD is a powerful optimization algorithm that can handle large-scale and sparse machine learning problems efficiently.
