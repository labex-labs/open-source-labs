# Regularization Path of L1- Logistic Regression

## Introduction

The L1-Logistic Regression model is a binary classification method that uses L1 regularization to induce sparsity in the model. The regularization path of this model shows the coefficients of the model as regularization strength increases. In this lab, we will use the Iris dataset to train L1-penalized logistic regression models and plot their regularization paths.

## Steps

### Step 1: Load the Iris dataset

We will load the Iris dataset from the scikit-learn library. The dataset contains four features: Sepal length, Sepal width, Petal length, and Petal width. We will use only the first two features for binary classification.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 2] # Use only first two features for binary classification
y = y[y != 2]

X /= X.max() # Normalize X to speed-up convergence
```

### Step 2: Compute regularization path

We will compute the regularization path by training L1-penalized logistic regression models with different regularization strengths. We will use the liblinear solver, which can efficiently optimize for the Logistic Regression loss with an L1 penalty. We will set a low value for the tolerance to make sure that the model has converged before collecting the coefficients. We will also use warm_start=True, which means that the coefficients of the models are reused to initialize the next model fit to speed-up the computation of the full-path.

```python
import numpy as np
from sklearn import linear_model
from sklearn.svm import l1_min_c

cs = l1_min_c(X, y, loss="log") * np.logspace(0, 10, 16)

clf = linear_model.LogisticRegression(
    penalty="l1",
    solver="liblinear",
    tol=1e-6,
    max_iter=int(1e6),
    warm_start=True,
    intercept_scaling=10000.0,
)
coefs_ = []
for c in cs:
    clf.set_params(C=c)
    clf.fit(X, y)
    coefs_.append(clf.coef_.ravel().copy())

coefs_ = np.array(coefs_)
```

### Step 3: Plot regularization path

We will plot the regularization path by using the coefficients of the trained models. The coefficients will be plotted against the log of the regularization strength. On the left-hand side of the figure (strong regularizers), all the coefficients are exactly 0. When regularization gets progressively looser, coefficients can get non-zero values one after the other.

```python
import matplotlib.pyplot as plt

plt.plot(np.log10(cs), coefs_, marker="o")
ymin, ymax = plt.ylim()
plt.xlabel("log(C)")
plt.ylabel("Coefficients")
plt.title("Logistic Regression Path")
plt.axis("tight")
plt.show()
```

## Summary

In this lab, we learned how to train L1-penalized logistic regression models on the Iris dataset and plot their regularization paths. The regularization path shows how the coefficients of the model change with different regularization strengths. This method is useful in feature selection, as it can identify which features have the most significant impact on the model.
