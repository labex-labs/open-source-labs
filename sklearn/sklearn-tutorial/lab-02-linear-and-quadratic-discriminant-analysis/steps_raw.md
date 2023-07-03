# Linear and Quadratic Discriminant Analysis

## Introduction

Linear and Quadratic Discriminant Analysis (LDA and QDA) are two classic classifiers used in machine learning. LDA uses a linear decision surface, while QDA uses a quadratic decision surface. These classifiers are popular because they have closed-form solutions, work well in practice, and have no hyperparameters to tune.

In this lab, we will explore how to perform LDA and QDA using scikit-learn, a popular machine learning library in Python.

## Steps

### Step 1: Import the required libraries

First, we need to import the required libraries, including scikit-learn (sklearn) and matplotlib, which will be used for data visualization.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
```

### Step 2: Generate synthetic data

Next, we will generate synthetic data to demonstrate the difference between LDA and QDA. We will use the `make_classification` function from scikit-learn to create two classes with distinct patterns.

```python
from sklearn.datasets import make_classification

# Generate synthetic data
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=1)
```

### Step 3: Train and visualize the classifiers

Now, we will train the LDA and QDA classifiers on the synthetic data and visualize the decision boundaries.

```python
# Train the LDA classifier
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

# Train the QDA classifier
qda = QuadraticDiscriminantAnalysis()
qda.fit(X, y)

# Plot the decision boundaries
def plot_decision_boundary(classifier, title):
    h = 0.02  # step size in the mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(title)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plot_decision_boundary(lda, 'Linear Discriminant Analysis')

plt.subplot(1, 2, 2)
plot_decision_boundary(qda, 'Quadratic Discriminant Analysis')

plt.tight_layout()
plt.show()
```

### Step 4: Perform dimensionality reduction using LDA

LDA can also be used for supervised dimensionality reduction. We will demonstrate this by reducing the dimension of the Iris dataset.

```python
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Perform dimensionality reduction using LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
```

## Summary

Linear and Quadratic Discriminant Analysis (LDA and QDA) are two classic classifiers used in machine learning. LDA uses a linear decision surface, while QDA uses a quadratic decision surface. These classifiers have closed-form solutions and perform well in practice. LDA can also be used for supervised dimensionality reduction.
