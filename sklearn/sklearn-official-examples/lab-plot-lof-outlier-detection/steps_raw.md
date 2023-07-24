# Outlier Detection with LOF

## Introduction

The Local Outlier Factor (LOF) algorithm is an unsupervised machine learning method that is used to detect anomalies in data. It computes the local density deviation of a given data point with respect to its neighbors and considers as outliers the samples that have a substantially lower density than their neighbors.

In this lab, we will use LOF to detect outliers in a dataset.

## Steps

### Step 1: Import Libraries

We will import `numpy` and `matplotlib` for data manipulation and visualization respectively. We will also import `LocalOutlierFactor` from `sklearn.neighbors` for outlier detection.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
```

### Step 2: Generate Data with Outliers

We will generate a dataset of 120 data points with 100 inliers and 20 outliers. We will then plot the data to visualize the outliers.

```python
np.random.seed(42)

X_inliers = 0.3 * np.random.randn(100, 2)
X_inliers = np.r_[X_inliers + 2, X_inliers - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
X = np.r_[X_inliers, X_outliers]

plt.scatter(X[:, 0], X[:, 1], color="k", s=3.0)
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.xlabel("Data points")
plt.title("Data with Outliers")
plt.show()
```

### Step 3: Fit the Model for Outlier Detection

We will use `LocalOutlierFactor` to fit the model for outlier detection and compute the predicted labels of the training samples.

```python
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(X)
X_scores = clf.negative_outlier_factor_
```

### Step 4: Plot Results

We will plot the data points with circles whose radius is proportional to the outlier scores.

```python
plt.scatter(X[:, 0], X[:, 1], color="k", s=3.0, label="Data points")
# plot circles with radius proportional to the outlier scores
radius = (X_scores.max() - X_scores) / (X_scores.max() - X_scores.min())
scatter = plt.scatter(
    X[:, 0],
    X[:, 1],
    s=1000 * radius,
    edgecolors="r",
    facecolors="none",
    label="Outlier scores",
)
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.xlabel("Outlier Detection")
plt.legend(
    handler_map={scatter: HandlerPathCollection(update_func=update_legend_marker_size)}
)
plt.title("Local Outlier Factor (LOF)")
plt.show()
```

## Summary

In this lab, we have learned how to use Local Outlier Factor (LOF) for outlier detection. We have generated a dataset with outliers, fit the model for outlier detection, and plotted the results. LOF is a powerful unsupervised machine learning method that can be used to detect anomalies in a wide range of applications.
