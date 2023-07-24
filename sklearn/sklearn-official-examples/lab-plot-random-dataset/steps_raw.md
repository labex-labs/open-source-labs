# Random Classification Dataset Plotting

## Introduction

This lab demonstrates how to plot several randomly generated classification datasets using Python's scikit-learn library. It visualizes all datasets using two features, plotted on the x and y axis. The color of each point represents its class label.

## Steps

### Step 1: Import Libraries

We first need to import the required libraries. We will be using matplotlib and scikit-learn.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
from sklearn.datasets import make_gaussian_quantiles
```

### Step 2: Set Figure Size and Adjust Subplots

We set the figure size and adjust the subplots to make them more readable.

```python
plt.figure(figsize=(8, 8))
plt.subplots_adjust(bottom=0.05, top=0.9, left=0.05, right=0.95)
```

### Step 3: One Informative Feature, One Cluster per Class

We create a dataset with one informative feature and one cluster per class, and plot it.

```python
plt.subplot(321)
plt.title("One informative feature, one cluster per class", fontsize="small")
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```

### Step 4: Two Informative Features, One Cluster per Class

We create a dataset with two informative features and one cluster per class, and plot it.

```python
plt.subplot(322)
plt.title("Two informative features, one cluster per class", fontsize="small")
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```

### Step 5: Two Informative Features, Two Clusters per Class

We create a dataset with two informative features and two clusters per class, and plot it.

```python
plt.subplot(323)
plt.title("Two informative features, two clusters per class", fontsize="small")
X2, Y2 = make_classification(n_features=2, n_redundant=0, n_informative=2)
plt.scatter(X2[:, 0], X2[:, 1], marker="o", c=Y2, s=25, edgecolor="k")
```

### Step 6: Multi-Class, Two Informative Features, One Cluster

We create a dataset with multiple classes, two informative features, and one cluster, and plot it.

```python
plt.subplot(324)
plt.title("Multi-class, two informative features, one cluster", fontsize="small")
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1, n_classes=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```

### Step 7: Three Blobs

We create a dataset with three blobs, and plot it.

```python
plt.subplot(325)
plt.title("Three blobs", fontsize="small")
X1, Y1 = make_blobs(n_features=2, centers=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```

### Step 8: Gaussian Divided into Three Quantiles

We create a dataset with a Gaussian divided into three quantiles, and plot it.

```python
plt.subplot(326)
plt.title("Gaussian divided into three quantiles", fontsize="small")
X1, Y1 = make_gaussian_quantiles(n_features=2, n_classes=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```

### Step 9: Show Plot

We show the final plot.

```python
plt.show()
```

## Summary

This lab demonstrated how to plot several randomly generated classification datasets using Python's scikit-learn library. It visualizes all datasets using two features, plotted on the x and y axis. The color of each point represents its class label.
