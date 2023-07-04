# Linear Models

## Introduction

In this lab, we will explore linear models in scikit-learn. Linear models are a set of methods used for regression and classification tasks. They assume that the target variable is a linear combination of the features. These models are widely used in machine learning due to their simplicity and interpretability.

We will cover the following topics:

- Ordinary Least Squares
- Ridge Regression
- Lasso
- Logistic Regression
- Stochastic Gradient Descent
- Perceptron

## Steps

### Step 1: Ordinary Least Squares

Ordinary Least Squares (OLS) is a linear regression method that minimizes the sum of squared differences between the observed targets and the predicted targets. Mathematically, it solves a problem of the form:
$$\min_{w} || X w - y||_2^2$$

Let's start by fitting a linear regression model using OLS.

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

print(reg.coef_)
```

- We import the `linear_model` module from scikit-learn.
- We create an instance of `LinearRegression`.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the linear model.

### Step 2: Ridge Regression

Ridge regression is a linear regression method that adds a penalty term to the ordinary least squares objective function. This penalty term helps to reduce overfitting by shrinking the coefficients towards zero. The complexity of the model can be controlled by the regularization parameter.

Let's fit a ridge regression model.

```python
reg = linear_model.Ridge(alpha=0.5)
reg.fit([[0, 0], [0, 0], [1, 1]], [0, 0.1, 1])

print(reg.coef_)
```

- We create an instance of `Ridge` with the regularization parameter `alpha` set to 0.5.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the ridge regression model.

### Step 3: Lasso

Lasso is a linear regression method that adds a penalty term to the ordinary least squares objective function. The penalty term has the effect of setting some coefficients to exactly zero, thus performing feature selection. Lasso can be used for sparse model estimation.

Let's fit a lasso model.

```python
reg = linear_model.Lasso(alpha=0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])

print(reg.coef_)
```

- We create an instance of `Lasso` with the regularization parameter `alpha` set to 0.1.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the lasso model.

### Step 4: Logistic Regression

Logistic regression is a classification method that estimates the probabilities of the possible outcomes using a logistic function. It is commonly used for binary classification tasks. Logistic regression can also be extended to handle multi-class classification problems.

Let's fit a logistic regression model.

```python
clf = linear_model.LogisticRegression(random_state=0).fit(X, y)
print(clf.coef_)
```

- We create an instance of `LogisticRegression` with the `random_state` parameter set to 0.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the logistic regression model.

### Step 5: Stochastic Gradient Descent (SGD)

Stochastic Gradient Descent (SGD) is a simple yet efficient approach for training linear models. It is particularly useful when the number of samples and features is very large. SGD updates the model parameters using a small subset of the training data at each iteration, which makes it suitable for online learning and out-of-core learning.

Let's fit a logistic regression model using SGD.

```python
clf = linear_model.SGDClassifier(loss="log", max_iter=1000)
clf.fit(X, y)

print(clf.coef_)
```

- We create an instance of `SGDClassifier` with the `loss` parameter set to "log" to perform logistic regression.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the logistic regression model obtained using SGD.

### Step 6: Perceptron

The Perceptron is a simple linear classification algorithm suitable for large-scale learning. It updates its model only on mistakes, making it faster to train than the stochastic gradient descent (SGD) with hinge loss. The resulting models are also sparser.

Let's fit a perceptron model.

```python
clf = linear_model.Perceptron(alpha=0.1)
clf.fit(X, y)

print(clf.coef_)
```

- We create an instance of `Perceptron` with the regularization parameter `alpha` set to 0.1.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the perceptron model.

## Summary

In this lab, we explored linear models in scikit-learn. We learned about ordinary least squares, ridge regression, lasso, logistic regression, stochastic gradient descent, and perceptron. These models can be used for both regression and classification tasks. We also saw how to fit these models using various algorithms and techniques such as online learning and feature selection.
