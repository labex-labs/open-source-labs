# SVM Classifier on Iris Dataset

## Introduction

The iris dataset is a classic dataset used for classification problems. In this lab, we will learn how to plot different SVM classifiers in the iris dataset using Python scikit-learn. We will compare different linear SVM classifiers on a 2D projection of the iris dataset.

## Steps

### Step 1: Import necessary libraries and load the dataset

```python
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.inspection import DecisionBoundaryDisplay

# import some data to play with
iris = datasets.load_iris()
# Take the first two features. We could avoid this by using a two-dim dataset
X = iris.data[:, :2]
y = iris.target
```

### Step 2: Create SVM classifiers and fit the data

```python
C = 1.0  # SVM regularization parameter
models = (
    svm.SVC(kernel="linear", C=C),
    svm.LinearSVC(C=C, max_iter=10000, dual="auto"),
    svm.SVC(kernel="rbf", gamma=0.7, C=C),
    svm.SVC(kernel="poly", degree=3, gamma="auto", C=C),
)
models = (clf.fit(X, y) for clf in models)
```

### Step 3: Plot the decision surface for the classifiers

```python
# Set-up 2x2 grid for plotting.
fig, sub = plt.subplots(2, 2)
plt.subplots_adjust(wspace=0.4, hspace=0.4)

X0, X1 = X[:, 0], X[:, 1]

# create a DecisionBoundaryDisplay for each classifier
for clf, title, ax in zip(models, titles, sub.flatten()):
    disp = DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        response_method="predict",
        cmap=plt.cm.coolwarm,
        alpha=0.8,
        ax=ax,
        xlabel=iris.feature_names[0],
        ylabel=iris.feature_names[1],
    )
    # plot the data points
    ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors="k")
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)

plt.show()
```

### Step 4: Interpret the results

The above code will generate a plot with four subplots. Each subplot shows the decision surface for a different SVM classifier. The title of each subplot indicates the type of SVM kernel used in that classifier. The data points are color-coded based on their target class.

## Summary

In this lab, we learned how to plot different SVM classifiers in the iris dataset using Python scikit-learn. We compared different linear SVM classifiers on a 2D projection of the iris dataset and interpreted the results. SVM classifiers are powerful tools for classification problems and can be used for a wide range of datasets.
