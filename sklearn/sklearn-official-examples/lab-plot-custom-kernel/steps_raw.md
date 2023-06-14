# SVM Classification using Custom Kernel

## Introduction

In this lab, we will learn how to use Support Vector Machines (SVM) to classify a sample using a custom kernel. We will use Python's scikit-learn library to perform SVM classification with a custom kernel. SVM is a popular machine learning algorithm used for classification, regression, and outlier detection. SVM works by creating a boundary or a line (hyperplane) that separates the data into classes.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries for this lab. We will be using numpy, matplotlib, scikit-learn, and DecisionBoundaryDisplay.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.inspection import DecisionBoundaryDisplay
```

### Step 2: Load Data

In this step, we will load the iris dataset using scikit-learn's datasets module. We will select the first two features of the dataset and assign it to the variable X. We will also assign the target variable to Y.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
```

### Step 3: Create Custom Kernel

In this step, we will create a custom kernel. The custom kernel will be a dot product of two matrices. We will create a matrix M with the values [[2, 0], [0, 1.0]]. We will then multiply the matrices X and Y with M and take their dot product.

```python
def my_kernel(X, Y):
    """
    We create a custom kernel:

                 (2  0)
    k(X, Y) = X  (    ) Y.T
                 (0  1)
    """
    M = np.array([[2, 0], [0, 1.0]])
    return np.dot(np.dot(X, M), Y.T)
```

### Step 4: Create SVM Classifier

In this step, we will create an instance of SVM classifier and fit our data. We will use the custom kernel created in the previous step.

```python
clf = svm.SVC(kernel=my_kernel)
clf.fit(X, Y)
```

### Step 5: Plot Decision Boundary

In this step, we will plot the decision surface and the support vectors. We will use the DecisionBoundaryDisplay module from scikit-learn's inspection module to plot the decision boundary. We will also scatter plot the training points.

```python
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
)

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolors="k")
plt.title("3-Class classification using Support Vector Machine with custom kernel")
plt.axis("tight")
plt.show()
```

## Summary

In this lab, we learned how to use Support Vector Machines (SVM) to classify a sample using a custom kernel. We used scikit-learn library to perform SVM classification with a custom kernel. We loaded the iris dataset, created a custom kernel, created an instance of SVM classifier and fit our data, and plotted the decision boundary and the support vectors. SVM is a popular machine learning algorithm used for classification, regression, and outlier detection.
