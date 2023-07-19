# Cross Validation

## Introduction

In machine learning, cross-validation is a technique used to evaluate the performance of a model on an independent dataset. It helps to prevent overfitting by providing a better estimate of how well the model will generalize to new, unseen data.

In this lab, we will explore the concept of cross-validation and how to implement it using the scikit-learn library in Python.

## Steps

### Step 1: Import the necessary libraries

First, let's import the necessary libraries for this lab.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
```

### Step 2: Load the dataset

Next, let's load a dataset to train our model on. In this example, we will use the Iris dataset, which is a popular dataset for classification tasks.

```python
X, y = datasets.load_iris(return_X_y=True)
```

### Step 3: Split the dataset into training and test sets

To evaluate the performance of our model, we need to split the dataset into a training set and a test set. We will use the `train_test_split` function from the scikit-learn library to do this.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```

### Step 4: Train and evaluate the model

Now, let's train a support vector machine (SVM) classifier on the training set and evaluate its performance on the test set.

```python
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Accuracy: ", score)
```

### Summary

In this lab, we learned how to implement cross-validation using the scikit-learn library in Python. We split the dataset into training and test sets, trained a model on the training set, and evaluated its performance on the test set. Cross-validation helps to prevent overfitting and provides a better estimate of how well a model will generalize to new, unseen data.
