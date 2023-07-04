# Supervised Learning

## Introduction

In supervised learning, we want to learn the relationship between two datasets: the observed data `X` and an external variable `y` that we want to predict.
There are two main types of supervised learning problems: classification and regression. In classification, the goal is to predict the class or category of an observation, while in regression, the goal is to predict a continuous target variable.

In this lab, we will explore the concepts of supervised learning and see how to implement them using scikit-learn, a popular machine learning library in Python. We will cover topics such as nearest neighbor classification, linear regression, and support vector machines (SVMs).

## Steps

### Step 1: Nearest Neighbor Classification

In this step, we will explore the concept of nearest neighbor classification and how it can be implemented using scikit-learn. We will use the iris dataset, which consists of measurements of different iris flowers.

#### Load the Iris Dataset

```python
import numpy as np
from sklearn import datasets

iris_X, iris_y = datasets.load_iris(return_X_y=True)
```

#### Split the Data into Train and Test Sets

```python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

#### Create and Fit a Nearest Neighbor Classifier

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
```

#### Make Predictions

```python
predictions = knn.predict(iris_X_test)
```

### Step 2: Linear Regression

In this step, we will explore the concept of linear regression and how it can be implemented using scikit-learn. We will use the diabetes dataset, which consists of physiological variables of patients and their disease progression after one year.

#### Load the Diabetes Dataset

```python
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

#### Create and Fit a Linear Regression Model

```python
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
```

#### Make Predictions and Calculate Performance Metrics

```python
predictions = regr.predict(diabetes_X_test)
mse = np.mean((predictions - diabetes_y_test)**2)
variance_score = regr.score(diabetes_X_test, diabetes_y_test)
```

### Step 3: Support Vector Machines (SVMs)

In this step, we will explore the concept of support vector machines (SVMs) and how they can be used for classification tasks. SVMs aim to find a hyperplane that maximally separates the data points of different classes.

#### Create and Fit a Linear SVM

```python
from sklearn import svm

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
```

#### Create and Fit SVMs with Different Kernels

```python
svc_poly = svm.SVC(kernel='poly', degree=3)
svc_rbf = svm.SVC(kernel='rbf')

svc_poly.fit(iris_X_train, iris_y_train)
svc_rbf.fit(iris_X_train, iris_y_train)
```

### Summary

In this lab, we learned about different supervised learning techniques and how to implement them using scikit-learn. We covered nearest neighbor classification, linear regression, and support vector machines (SVMs). These techniques allow us to predict output variables from high-dimensional observations and classify data into different categories. By applying these techniques to real-world datasets, we can gain insights and make predictions in various domains such as healthcare, finance, and social sciences.
