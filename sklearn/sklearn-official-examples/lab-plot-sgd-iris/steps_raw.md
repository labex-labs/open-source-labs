# Scikit-Learn Multi-Class SGD Classifier

## Introduction

In this lab, we will use Scikit-Learn's SGDClassifier to implement a multi-class classification model on the famous iris dataset. We will plot the decision surface of the model on the dataset and visualize the hyperplanes corresponding to the three one-versus-all (OVA) classifiers.

## Steps

### Step 1: Load and Prepare Data

We begin by importing the necessary libraries and loading the iris dataset. We will then shuffle the data and standardize it to be used for training.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

# load iris dataset
iris = datasets.load_iris()

# take the first two features
X = iris.data[:, :2]
y = iris.target
colors = "bry"

# shuffle the data
idx = np.arange(X.shape[0])
np.random.seed(13)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# standardize the data
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std
```

### Step 2: Train the Model

We will now train the SGDClassifier model on the iris dataset with the help of the fit() method. This method takes the input data and target values as input and trains the model on the given data.

```python
clf = SGDClassifier(alpha=0.001, max_iter=100).fit(X, y)
```

### Step 3: Visualize the Decision Surface

We will now plot the decision surface of the trained model on the iris dataset. We will use the DecisionBoundaryDisplay class to visualize the decision boundary of the model.

```python
from sklearn.inspection import DecisionBoundaryDisplay

ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    xlabel=iris.feature_names[0],
    ylabel=iris.feature_names[1],
)
plt.axis("tight")
```

### Step 4: Plot Training Points

We will now plot the training points on the decision surface. We will use scatter() method to plot the training points with different colors for different target values.

```python
for i, color in zip(clf.classes_, colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=color,
        label=iris.target_names[i],
        cmap=plt.cm.Paired,
        edgecolor="black",
        s=20,
    )
plt.title("Decision surface of multi-class SGD")
plt.axis("tight")
```

### Step 5: Plot One-Against-All Classifiers

We will now plot the three one-versus-all (OVA) classifiers on the decision surface. We will use the coef* and intercept* attributes of the trained model to plot the hyperplanes corresponding to the OVA classifiers.

```python
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
coef = clf.coef_
intercept = clf.intercept_


def plot_hyperplane(c, color):
    def line(x0):
        return (-(x0 * coef[c, 0]) - intercept[c]) / coef[c, 1]

    plt.plot([xmin, xmax], [line(xmin), line(xmax)], ls="--", color=color)


for i, color in zip(clf.classes_, colors):
    plot_hyperplane(i, color)
plt.legend()
plt.show()
```

## Summary

In this lab, we learned how to use Scikit-Learn's SGDClassifier to implement a multi-class classification model on the iris dataset. We visualized the decision surface of the trained model on the dataset and plotted the hyperplanes corresponding to the three one-versus-all (OVA) classifiers.
