# SVM Margins

## Introduction

Support Vector Machines (SVMs) are used for classification and regression analysis. SVMs find the best possible line or hyperplane that separates the data into different classes. The line or hyperplane that maximizes the distance between the two closest data points from different classes is called the margin. In this lab, we will explore how the parameter `C` affects the margin in a linear SVM.

## Steps

### Step 1: Import Libraries

We start by importing the necessary libraries, including numpy, matplotlib, and scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
```

### Step 2: Generate Data

We generate 40 separable points using numpy's `random.randn` function. The first 20 points have a mean of [-2, -2] and the next 20 points have a mean of [2, 2]. We then assign a class label of 0 to the first 20 points and a class label of 1 to the next 20 points.

```python
np.random.seed(0)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20
```

### Step 3: Fit the Model

We fit the SVM model using scikit-learn's `SVC` class. We set the kernel to linear and the penalty parameter `C` to 1 for the unregularized case and 0.05 for the regularized case. We then calculate the separating hyperplane using the coefficients and the intercept of the model.

```python
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(X, Y)

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]
```

### Step 4: Calculate Margins

We calculate the margins for the separating hyperplane. We first calculate the margin distance using the coefficients of the model. We then calculate the vertical distance from the support vectors to the hyperplane using the slope of the hyperplane. Finally, we plot the line, the points, and the nearest vectors to the plane.

```python
margin = 1 / np.sqrt(np.sum(clf.coef_**2))
yy_down = yy - np.sqrt(1 + a**2) * margin
yy_up = yy + np.sqrt(1 + a**2) * margin

plt.plot(xx, yy, "k-")
plt.plot(xx, yy_down, "k--")
plt.plot(xx, yy_up, "k--")

plt.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=80,
    facecolors="none",
    zorder=10,
    edgecolors="k",
    cmap=plt.get_cmap("RdBu"),
)
plt.scatter(
    X[:, 0], X[:, 1], c=Y, zorder=10, cmap=plt.get_cmap("RdBu"), edgecolors="k"
)

plt.axis("tight")
x_min = -4.8
x_max = 4.2
y_min = -6
y_max = 6
```

### Step 5: Plot Contour

We plot the contour of the decision function. We first create a meshgrid using the `xx` and `yy` arrays. We then reshape the meshgrid into a 2D array and apply the `decision_function` method of the `SVC` class to get the predicted values. We then plot the contour using the `contourf` method.

```python
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

plt.contourf(XX, YY, Z, cmap=plt.get_cmap("RdBu"), alpha=0.5, linestyles=["-"])

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())
```

### Step 6: Display the Plots

We display the plots for the unregularized and regularized cases.

```python
plt.show()
```

## Summary

In this lab, we explored how the parameter `C` affects the margin in a linear SVM. We generated data, fit the model, calculated the margins, and plotted the results. We then displayed the plots for the unregularized and regularized cases.
