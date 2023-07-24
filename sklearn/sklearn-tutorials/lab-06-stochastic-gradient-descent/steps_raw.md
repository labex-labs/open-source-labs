# Stochastic Gradient Descent

## Introduction

Stochastic Gradient Descent (SGD) is a popular optimization algorithm used in machine learning. It is a variation of the gradient descent algorithm that uses a randomly selected subset of the training data at each iteration. This makes it computationally efficient and suitable for handling large datasets. In this lab, we will walk through the steps of implementing SGD in Python using scikit-learn.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries for this lab, including scikit-learn.

```python
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

### Step 2: Load Data

Next, we will load the iris dataset from scikit-learn. This dataset is a classic machine learning dataset that consists of measurements of iris flowers, along with their species labels.

```python
iris = load_iris()
X = iris.data
y = iris.target
```

### Step 3: Preprocess Data

Before applying SGD, it is often beneficial to preprocess the data. In this case, we will standardize the features using scikit-learn's StandardScaler.

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
```

### Step 4: Split Data

We will split the dataset into a training set and a test set. The training set will be used to train the SGD classifier, while the test set will be used to evaluate its performance.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### Step 5: Train the Classifier

Now we can create and train the SGD classifier using scikit-learn's SGDClassifier class. We will use the 'hinge' loss function, which is commonly used for linear classifiers.

```python
clf = SGDClassifier(loss='hinge', random_state=42)
clf.fit(X_train, y_train)
```

### Step 6: Make Predictions

Once the classifier is trained, we can use it to make predictions on new data. Here, we will use it to predict the target classes for the test set.

```python
y_pred = clf.predict(X_test)
```

### Step 7: Evaluate Performance

Finally, we will evaluate the performance of the classifier by calculating the accuracy of its predictions on the test set.

```python
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

## Summary

In this lab, we learned how to implement Stochastic Gradient Descent (SGD) using scikit-learn. We loaded the iris dataset, preprocessed the data, split it into training and test sets, trained an SGD classifier, made predictions, and evaluated the classifier's performance. SGD is a powerful optimization algorithm that is widely used in machine learning for large-scale problems.
