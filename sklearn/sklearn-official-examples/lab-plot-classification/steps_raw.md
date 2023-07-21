# Nearest Neighbors Classification

## Introduction

In this lab, we will be using the Nearest Neighbors Classification algorithm to classify data points in a 2-dimensional space. We will be using the Iris dataset, which is a commonly used dataset in machine learning. We will visualize the decision boundaries for each class and observe how the algorithm performs when different weights are used.

## Steps

### Step 1: Import necessary libraries

We will start by importing the necessary libraries, which include `matplotlib`, `seaborn`, `ListedColormap`, `datasets`, `neighbors`, and `DecisionBoundaryDisplay` from `sklearn`.

```python
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from sklearn.inspection import DecisionBoundaryDisplay
```

### Step 2: Load the Iris dataset

We will then load the Iris dataset using the `load_iris()` function from the `datasets` module of `sklearn`.

```python
iris = datasets.load_iris()
```

### Step 3: Prepare the data

We will only take the first two features of the Iris dataset, which are the sepal length and sepal width. We will then split the data into the feature matrix `X` and the target vector `y`.

```python
X = iris.data[:, :2]
y = iris.target
```

### Step 4: Define the color maps

We will define the color maps that will be used for plotting the decision boundaries and the training points.

```python
cmap_light = ListedColormap(["orange", "cyan", "cornflowerblue"])
cmap_bold = ["darkorange", "c", "darkblue"]
```

### Step 5: Visualize the decision boundaries

We will loop through two different weight values, "uniform" and "distance", and plot the decision boundaries for each weight value. We will use the `KNeighborsClassifier` class from `neighbors` module to perform the classification.

```python
n_neighbors = 15

for weights in ["uniform", "distance"]:
    # create an instance of Neighbours Classifier and fit the data
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # plot the decision boundaries
    _, ax = plt.subplots()
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        cmap=cmap_light,
        ax=ax,
        response_method="predict",
        plot_method="pcolormesh",
        xlabel=iris.feature_names[0],
        ylabel=iris.feature_names[1],
        shading="auto",
    )

    # plot the training points
    sns.scatterplot(
        x=X[:, 0],
        y=X[:, 1],
        hue=iris.target_names[y],
        palette=cmap_bold,
        alpha=1.0,
        edgecolor="black",
    )
    plt.title(
        "3-Class classification (k = %i, weights = '%s')" % (n_neighbors, weights)
    )

plt.show()
```

### Step 6: Interpret the results

We can observe the decision boundaries for each weight value and how well the algorithm performs in classifying the data points. The "uniform" weight value assumes all neighbors have equal weight, while the "distance" weight value assigns more weight to closer neighbors. We can see that the decision boundaries are smoother with the "distance" weight value, indicating a more accurate classification.

## Summary

In this lab, we learned how to use the Nearest Neighbors Classification algorithm to classify data points in a 2-dimensional space. We used the Iris dataset to visualize the decision boundaries for each class and observed how the algorithm performs when different weight values are used. We also learned how to interpret the results and observed that the "distance" weight value performs better in classifying the data points.
