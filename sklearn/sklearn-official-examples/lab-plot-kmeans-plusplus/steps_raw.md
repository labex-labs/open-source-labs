# K-Means++ Initialization

## Introduction

In this lab, we will learn about K-Means++ initialization using the scikit-learn library in Python. K-Means++ is a popular algorithm for clustering data into groups based on similarities. It is used as the default initialization for k-means. In this lab, we will generate sample data, calculate seeds from k-means++, and plot the init seeds alongside the sample data.

## Steps

### Step 1: Generate sample data

We will use the scikit-learn library's `make_blobs` function to generate sample data. This function generates isotropic Gaussian blobs for clustering. We will generate 4000 samples with 4 centers.

```python
# Generate sample data
n_samples = 4000
n_components = 4

X, y_true = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)
X = X[:, ::-1]
```

### Step 2: Calculate seeds from k-means++

We will use the scikit-learn library's `kmeans_plusplus` function to calculate seeds from k-means++. This function returns the initial cluster centers that are used for k-means clustering. We will calculate 4 clusters using k-means++.

```python
# Calculate seeds from k-means++
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```

### Step 3: Plot init seeds alongside sample data

We will use the matplotlib library to plot the init seeds alongside the sample data. The init seeds will be shown as blue points, and the sample data will be shown as colored dots.

```python
# Plot init seeds along side sample data
plt.figure(1)
colors = ["#4EACC5", "#FF9C34", "#4E9A06", "m"]

for k, col in enumerate(colors):
    cluster_data = y_true == k
    plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker=".", s=10)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
plt.title("K-Means++ Initialization")
plt.xticks([])
plt.yticks([])
plt.show()
```

## Summary

In this lab, we learned about K-Means++ initialization using the scikit-learn library in Python. We generated sample data, calculated seeds from k-means++, and plotted the init seeds alongside the sample data. K-Means++ is a popular algorithm for clustering data into groups based on similarities, and it is used as the default initialization for k-means.
