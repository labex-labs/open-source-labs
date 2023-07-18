# One-class SVM for Novelty Detection

## Introduction

This lab will guide you through an example of using one-class SVM for novelty detection. One-class SVM is an unsupervised algorithm that learns a decision function for novelty detection: classifying new data as similar or different to the training set.

## Steps

### Step 1: Import necessary libraries and generate data

The first step is to import the necessary libraries and generate data. We will use numpy and matplotlib for generating and visualizing data, and scikit-learn for building the one-class SVM model.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Generate train data
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# Generate some regular novel observations
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# Generate some abnormal novel observations
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```

### Step 2: Fit the one-class SVM model

Next, we will fit the one-class SVM model on the generated data.

```python
# Fit the model
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# Predict the labels for the training data, regular novel observations, and abnormal novel observations
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
```

### Step 3: Calculate the number of errors

We will calculate the number of errors made by the model on the training data, regular novel observations, and abnormal novel observations.

```python
# Count the number of errors
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```

### Step 4: Visualize the results

Finally, we will visualize the results of the one-class SVM model. We will plot the decision boundary, the training data, regular novel observations, and abnormal novel observations.

```python
# Visualize the results
xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("Novelty Detection")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors="darkred")
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors="palevioletred")

s = 40
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c="white", s=s, edgecolors="k")
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c="blueviolet", s=s, edgecolors="k")
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c="gold", s=s, edgecolors="k")
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend(
    [a.collections[0], b1, b2, c],
    [
        "learned frontier",
        "training observations",
        "new regular observations",
        "new abnormal observations",
    ],
    loc="upper left",
    prop=matplotlib.font_manager.FontProperties(size=11),
)
plt.xlabel(
    "error train: %d/200 ; errors novel regular: %d/40 ; errors novel abnormal: %d/40"
    % (n_error_train, n_error_test, n_error_outliers)
)
plt.show()
```

## Summary

In this lab, we learned how to use one-class SVM for novelty detection. We generated data, fit the one-class SVM model, calculated the number of errors, and visualized the results. One-class SVM is a useful algorithm for detecting anomalies in data, and can be applied to a wide variety of applications.
