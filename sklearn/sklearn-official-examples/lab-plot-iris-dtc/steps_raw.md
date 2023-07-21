# Decision Trees on Iris Dataset

## Introduction

In this lab, we will use the Iris dataset and decision trees to classify the types of iris flowers. We will first visualize the decision boundaries of decision trees trained on pairs of features of the Iris dataset. Next, we will display the structure of a single decision tree trained on all the features of the Iris dataset.

## Steps

### Step 1: Load the Iris Dataset

The first step is to load the Iris dataset using scikit-learn.

```python
from sklearn.datasets import load_iris

iris = load_iris()
```

### Step 2: Visualize Decision Boundaries

We will now visualize the decision boundaries of decision trees trained on pairs of features of the Iris dataset.

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.inspection import DecisionBoundaryDisplay

# Parameters
n_classes = 3
plot_colors = "ryb"
plot_step = 0.02

for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]):
    # We only take the two corresponding features
    X = iris.data[:, pair]
    y = iris.target

    # Train
    clf = DecisionTreeClassifier().fit(X, y)

    # Plot the decision boundary
    ax = plt.subplot(2, 3, pairidx + 1)
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        cmap=plt.cm.RdYlBu,
        response_method="predict",
        ax=ax,
        xlabel=iris.feature_names[pair[0]],
        ylabel=iris.feature_names[pair[1]],
    )

    # Plot the training points
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0],
            X[idx, 1],
            c=color,
            label=iris.target_names[i],
            cmap=plt.cm.RdYlBu,
            edgecolor="black",
            s=15,
        )

plt.suptitle("Decision surface of decision trees trained on pairs of features")
plt.legend(loc="lower right", borderpad=0, handletextpad=0)
_ = plt.axis("tight")
```

### Step 3: Display Decision Tree Structure

Next, we will display the structure of a single decision tree trained on all the features of the Iris dataset.

```python
from sklearn.tree import plot_tree

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("Decision tree trained on all the iris features")
plt.show()
```

## Summary

In this lab, we used decision trees to classify the types of iris flowers. We first visualized the decision boundaries of decision trees trained on pairs of features of the Iris dataset. Next, we displayed the structure of a single decision tree trained on all the features of the Iris dataset.
