# Principal Components Analysis

## Introduction

Principal Components Analysis (PCA) is a statistical technique used to simplify data. It is a linear transformation technique that finds the most important features or patterns in the data. PCA is widely used in data analysis and machine learning for dimensionality reduction, data compression, and feature extraction. In this lab, we will use Python's scikit-learn library to perform PCA on a dataset and visualize the results.

## Steps

### Step 1: Import Libraries

We start by importing the necessary libraries for this lab. We will be using numpy for numerical operations, matplotlib for visualization, and scikit-learn for PCA.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
```

### Step 2: Create Data

We will generate a random dataset for this lab. The dataset will have three variables `x`, `y`, and `z`. We will define `x` and `y` as normally distributed random variables with mean 0 and standard deviation of 0.5. `z` is also normally distributed with mean 0 and standard deviation of 0.1.

```python
e = np.exp(1)
np.random.seed(4)

y = np.random.normal(scale=0.5, size=(30000))
x = np.random.normal(scale=0.5, size=(30000))
z = np.random.normal(scale=0.1, size=len(x))
```

### Step 3: Perform PCA

Next, we will perform PCA on our dataset. We first concatenate `x`, `y`, and `z` to form a 3D array `Y`. We then create an instance of the PCA class and fit it to our data. We can then access the principal components using the `components_` attribute of the PCA object.

```python
Y = np.c_[x, y, z]
pca = PCA(n_components=3)
pca.fit(Y)
components = pca.components_
```

### Step 4: Visualize PCA Results

We can visualize the results of our PCA by plotting the principal components. We create a 3D scatter plot of our data and color each point based on its density. We then plot the first two principal components as a plane. We repeat this process for two different views of the data.

```python
fig = plt.figure(figsize=(10, 5))

# First view
ax = fig.add_subplot(121, projection="3d", elev=-40, azim=-80)
ax.set_title("View 1")

# Plot the data
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Plot the principal components
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

# Second view
ax = fig.add_subplot(122, projection="3d", elev=30, azim=20)
ax.set_title("View 2")

# Plot the data
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Plot the principal components
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

plt.show()
```

### Summary

In this lab, we learned how to perform PCA on a dataset using Python's scikit-learn library. We generated a random dataset with three variables, performed PCA, and visualized the results. We plotted the data in a 3D scatter plot and added a plane for the first two principal components. PCA is a powerful technique for reducing the dimensionality of data and finding the most important patterns or features.
