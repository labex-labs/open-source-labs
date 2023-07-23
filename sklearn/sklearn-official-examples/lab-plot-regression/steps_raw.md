# Nearest Neighbors Regression

## Introduction

Nearest Neighbors Regression is a machine learning algorithm that predicts the value of a new data point by finding the k-nearest data points in the training set and using their average value to predict the new value. In this lab, we will use scikit-learn to demonstrate how to resolve a regression problem using a k-Nearest Neighbor and the interpolation of the target using both barycenter and constant weights.

## Steps

### Step 1: Generate Sample Data

We first generate sample data to use for our regression problem. We create an array of 40 data points with 1 feature, and then create a target array by applying the sine function to the data. We also add some noise to every 5th data point.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

# Add noise to targets
y[::5] += 1 * (0.5 - np.random.rand(8))
```

### Step 2: Fit Regression Model

We then fit our regression model to the sample data using 5 neighbors and both uniform and distance weights. We use a for loop to iterate over each weight type and create a scatter plot of the data points and a line plot of the predicted values using the `predict` method of the fitted model.

```python
n_neighbors = 5

for i, weights in enumerate(["uniform", "distance"]):
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    y_ = knn.fit(X, y).predict(T)

    plt.subplot(2, 1, i + 1)
    plt.scatter(X, y, color="darkorange", label="data")
    plt.plot(T, y_, color="navy", label="prediction")
    plt.axis("tight")
    plt.legend()
    plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors, weights))

plt.tight_layout()
plt.show()
```

## Summary

In this lab, we demonstrated how to use the Nearest Neighbors Regression algorithm to predict the values of new data points based on the k-nearest neighbors in the training set. We used scikit-learn to generate sample data and fit our regression model using both uniform and distance weights. We then plotted the data points and predicted values to visualize the accuracy of our model.
