# Multi-layer Perceptron Regularization

## Introduction

This lab demonstrates how to use regularization in multi-layer perceptron (MLP) to combat overfitting. We will compare different values for the regularization parameter, alpha, and observe how the decision functions change.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries for this lab. We will use scikit-learn to create synthetic datasets, MLPClassifier to build the MLP model, StandardScaler to standardize the data, and make_pipeline to create a pipeline of transformations and classifier.

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
```

### Step 2: Define Alphas

We will define different values for the regularization parameter, alpha. We will use np.logspace to generate 5 logarithmically spaced values between 0.1 and 10.

```python
alphas = np.logspace(-1, 1, 5)
```

### Step 3: Create Classifiers

We will create MLP classifiers for each value of alpha. We will create a pipeline that includes StandardScaler to standardize the data and MLPClassifier with different values of alpha. We will set the solver to 'lbfgs', which is an optimizer in the family of quasi-Newton methods. We will set max_iter to 2000 and early_stopping to True to prevent overfitting. We will use two hidden layers with 10 neurons each.

```python
classifiers = []
names = []
for alpha in alphas:
    classifiers.append(
        make_pipeline(
            StandardScaler(),
            MLPClassifier(
                solver="lbfgs",
                alpha=alpha,
                random_state=1,
                max_iter=2000,
                early_stopping=True,
                hidden_layer_sizes=[10, 10],
            ),
        )
    )
    names.append(f"alpha {alpha:.2f}")
```

### Step 4: Create Datasets

We will create three synthetic datasets using make_classification, make_moons, and make_circles functions from scikit-learn. We will split each dataset into training and testing sets using train_test_split.

```python
X, y = make_classification(
    n_features=2, n_redundant=0, n_informative=2, random_state=0, n_clusters_per_class=1
)
rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)
linearly_separable = (X, y)

datasets = [
    make_moons(noise=0.3, random_state=0),
    make_circles(noise=0.2, factor=0.5, random_state=1),
    linearly_separable,
]

figure = plt.figure(figsize=(17, 9))
i = 1
# iterate over datasets
for X, y in datasets:
    # split into training and test part
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42
    )
```

### Step 5: Plot Datasets

We will plot each dataset and color the training and testing points differently.

```python
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # just plot the dataset first
    cm = plt.cm.RdBu
    cm_bright = ListedColormap(["#FF0000", "#0000FF"])
    ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
    # Plot the training points
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright)
    # and testing points
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6)
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
    i += 1
```

### Step 6: Fit Classifiers and Plot Decision Boundaries

We will fit each classifier on each dataset and plot the decision boundaries. We will use contourf to plot the decision boundary and scatter to plot the training and testing points. We will also display the accuracy score on each plot.

```python
    # iterate over classifiers
    for name, clf in zip(names, classifiers):
        ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)

        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, x_max] x [y_min, y_max].
        if hasattr(clf, "decision_function"):
            Z = clf.decision_function(np.column_stack([xx.ravel(), yy.ravel()]))
        else:
            Z = clf.predict_proba(np.column_stack([xx.ravel(), yy.ravel()]))[:, 1]

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, cmap=cm, alpha=0.8)

        # Plot also the training points
        ax.scatter(
            X_train[:, 0],
            X_train[:, 1],
            c=y_train,
            cmap=cm_bright,
            edgecolors="black",
            s=25,
        )
        # and testing points
        ax.scatter(
            X_test[:, 0],
            X_test[:, 1],
            c=y_test,
            cmap=cm_bright,
            alpha=0.6,
            edgecolors="black",
            s=25,
        )

        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(name)
        ax.text(
            xx.max() - 0.3,
            yy.min() + 0.3,
            f"{score:.3f}".lstrip("0"),
            size=15,
            horizontalalignment="right",
        )
        i += 1
```

### Step 7: Show Plots

Finally, we will adjust the subplot layout and display the plots.

```python
figure.subplots_adjust(left=0.02, right=0.98)
plt.show()
```

## Summary

In this lab, we learned how to use regularization in multi-layer perceptron to combat overfitting. We compared different values of the regularization parameter, alpha, and observed how the decision functions changed. We also learned how to create synthetic datasets, standardize the data, create MLP classifiers, and plot decision boundaries.
