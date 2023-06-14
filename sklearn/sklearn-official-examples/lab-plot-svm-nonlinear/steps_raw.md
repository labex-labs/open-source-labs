# Non-Linear SVM Classification

## Introduction

This lab will guide you through the process of performing binary classification using non-linear Support Vector Machine (SVM) with Radial Basis Function (RBF) kernel. The target to predict is an XOR of the inputs. The color map illustrates the decision function learned by the SVM. We will use Python scikit-learn library for this task.

## Steps

### Step 1: Import Required Libraries

In this step, we will import the required libraries for this task. We will use numpy and matplotlib for data visualization, and scikit-learn for SVM classification.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
```

### Step 2: Generate Data

In this step, we will generate the data for training and testing the SVM classifier. We will generate 300 random data points with two features. The target to predict is an XOR of the inputs.

```python
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```

### Step 3: Train the Model

In this step, we will train the SVM classifier with RBF kernel using the generated data.

```python
clf = svm.NuSVC(gamma="auto")
clf.fit(X, Y)
```

### Step 4: Visualize the Decision Function

In this step, we will visualize the decision function learned by the SVM. We will create a meshgrid of points and use the SVM classifier to predict the class of each point. We will then plot the points with their respective classes and the decision boundary learned by the SVM.

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.imshow(
    Z,
    interpolation="nearest",
    extent=(xx.min(), xx.max(), yy.min(), yy.max()),
    aspect="auto",
    origin="lower",
    cmap=plt.cm.PuOr_r,
)
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2, linestyles="dashed")
plt.scatter(X[:, 0], X[:, 1], s=30, c=Y, cmap=plt.cm.Paired, edgecolors="k")
plt.xticks(())
plt.yticks(())
plt.axis([-3, 3, -3, 3])
plt.show()
```

## Summary

In this lab, we learned how to perform binary classification using non-linear SVM with RBF kernel. We generated data with two features and an XOR target to predict. We trained the SVM classifier using the generated data and visualized the decision function learned by the SVM.
