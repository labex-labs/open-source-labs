# Support Vector Machines with Stochastic Gradient Descent (SGD)

## Introduction

In this lab, we will learn how to use Support Vector Machines (SVM) with Stochastic Gradient Descent (SGD) to classify data. SVM is a powerful classification algorithm that is widely used in machine learning for classification and regression analysis. The idea behind SVM is to find the best hyperplane that separates the data into classes with the largest possible margin. The margin is the distance between the hyperplane and the closest data points from each class. Stochastic Gradient Descent (SGD) is an optimization algorithm that is used to find the best parameters for the SVM algorithm.

## Steps

### Step 1: Import necessary libraries and generate data

First, we need to import the necessary libraries and generate a dataset that is suitable for classification. In this example, we will generate 50 separable points using the `make_blobs` function from Scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# we create 50 separable points
X, Y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
```

### Step 2: Train the SVM model with SGD

Next, we need to train the SVM model using SGD. We will use the `SGDClassifier` class from Scikit-learn to train the model. We will set the `loss` parameter to "hinge" to use the SVM algorithm and the `alpha` parameter to 0.01 to control the regularization strength. We will also set the `max_iter` parameter to 200 to limit the number of iterations.

```python
# fit the model
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
clf.fit(X, Y)
```

### Step 3: Plot the maximum margin separating hyperplane

Finally, we can plot the maximum margin separating hyperplane that we obtained using the SVM algorithm with SGD. We will create a grid of points using `np.meshgrid` and then compute the decision function for each point on the grid using the `decision_function` method of the SVM model. We will then plot the decision boundary using `plt.contour` and the data points using `plt.scatter`.

```python
# plot the line, the points, and the nearest vectors to the plane
xx = np.linspace(-1, 5, 10)
yy = np.linspace(-1, 5, 10)

X1, X2 = np.meshgrid(xx, yy)
Z = np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1 = val
    x2 = X2[i, j]
    p = clf.decision_function([[x1, x2]])
    Z[i, j] = p[0]
levels = [-1.0, 0.0, 1.0]
linestyles = ["dashed", "solid", "dashed"]
colors = "k"
plt.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolor="black", s=20)

plt.axis("tight")
plt.show()
```

## Summary

In this lab, we learned how to use Support Vector Machines (SVM) with Stochastic Gradient Descent (SGD) to classify data. We generated a dataset that is suitable for classification, trained the SVM model using SGD, and plotted the maximum margin separating hyperplane. SVM is a powerful classification algorithm that is widely used in machine learning for classification and regression analysis. The idea behind SVM is to find the best hyperplane that separates the data into classes with the largest possible margin. Stochastic Gradient Descent (SGD) is an optimization algorithm that is used to find the best parameters for the SVM algorithm.
