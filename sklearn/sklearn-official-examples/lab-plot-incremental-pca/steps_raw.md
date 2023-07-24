# Scikit-Learn IPCA

## Introduction

This lab will guide you through a step-by-step process of using the Incremental Principal Component Analysis (IPCA) algorithm to perform dimensionality reduction on the Iris dataset. IPCA is used when the dataset is too large to fit into memory and requires an incremental approach. We will compare the results of IPCA with the traditional PCA algorithm.

## Steps

### Step 1: Import Libraries

We will import necessary libraries including numpy, matplotlib, and the scikit-learn PCA and IPCA modules.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA, IncrementalPCA
```

### Step 2: Load Data

We will load the Iris dataset from scikit-learn's datasets module.

```python
iris = load_iris()
X = iris.data
y = iris.target
```

### Step 3: Perform IPCA

We will perform IPCA on the Iris dataset by initializing an instance of the IPCA class and fitting it to the data.

```python
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)
```

### Step 4: Perform PCA

We will perform PCA on the Iris dataset by initializing an instance of the PCA class and fitting it to the data.

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
```

### Step 5: Visualize Results

We will visualize the results of IPCA and PCA by plotting the transformed data on a scatter plot.

```python
colors = ["navy", "turquoise", "darkorange"]

for X_transformed, title in [(X_ipca, "Incremental PCA"), (X_pca, "PCA")]:
    plt.figure(figsize=(8, 8))
    for color, i, target_name in zip(colors, [0, 1, 2], iris.target_names):
        plt.scatter(
            X_transformed[y == i, 0],
            X_transformed[y == i, 1],
            color=color,
            lw=2,
            label=target_name,
        )

    if "Incremental" in title:
        err = np.abs(np.abs(X_pca) - np.abs(X_ipca)).mean()
        plt.title(title + " of iris dataset\nMean absolute unsigned error %.6f" % err)
    else:
        plt.title(title + " of iris dataset")
    plt.legend(loc="best", shadow=False, scatterpoints=1)
    plt.axis([-4, 4, -1.5, 1.5])

plt.show()
```

### Summary

In this lab, we learned how to use the Incremental Principal Component Analysis (IPCA) algorithm to perform dimensionality reduction on the Iris dataset. We compared the results of IPCA with traditional PCA and visualized the transformed data on a scatter plot. IPCA is useful when the dataset is too large to fit into memory and requires an incremental approach.
