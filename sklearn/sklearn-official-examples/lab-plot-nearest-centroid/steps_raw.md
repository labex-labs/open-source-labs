# Nearest Centroid Classification

## Introduction

This lab will guide you through the implementation of Nearest Centroid Classification using Scikit-learn. Nearest Centroid Classification is a simple classification method that works by computing the centroid for each class and then classifying new data points based on which centroid they are closest to.

## Steps

### Step 1: Import the Required Libraries

First, we need to import the necessary libraries, which include Numpy, Matplotlib, Scikit-learn datasets, NearestCentroid, and DecisionBoundaryDisplay.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.neighbors import NearestCentroid
from sklearn.inspection import DecisionBoundaryDisplay
```

### Step 2: Load the Data

Next, we load the iris dataset from Scikit-learn and select only the first two features for visualization purposes.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
```

### Step 3: Create Color Maps

We create two color maps for visualization purposes using the ListedColormap function from Matplotlib.

```python
cmap_light = ListedColormap(["orange", "cyan", "cornflowerblue"])
cmap_bold = ListedColormap(["darkorange", "c", "darkblue"])
```

### Step 4: Create and Fit the Classifier

We create an instance of Nearest Centroid Classifier with a shrinkage value of 0.2 and fit the data.

```python
clf = NearestCentroid(shrink_threshold=0.2)
clf.fit(X, y)
```

### Step 5: Predict and Measure Accuracy

We predict the class labels for the input data and measure the accuracy of the classifier.

```python
y_pred = clf.predict(X)
print("Accuracy: ", np.mean(y == y_pred))
```

### Step 6: Visualize the Decision Boundaries

We visualize the decision boundaries for the classifier using the DecisionBoundaryDisplay function from Scikit-learn.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cmap_light, ax=ax, response_method="predict"
)
```

### Step 7: Plot the Data Points

We plot the input data points using the scatter function from Matplotlib.

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor="k", s=20)
```

### Step 8: Add Title and Axis Labels

We add a title and axis labels to the plot using the title, xlabel, and ylabel functions from Matplotlib.

```python
plt.title("Nearest Centroid Classification")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
```

### Step 9: Display the Plot

We display the plot using the show function from Matplotlib.

```python
plt.show()
```

## Summary

In this lab, we learned how to implement Nearest Centroid Classification using Scikit-learn. We loaded the iris dataset, created a classifier, predicted class labels, measured accuracy, and visualized the decision boundaries and input data points.
