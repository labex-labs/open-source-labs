# Kernel PCA

## Introduction

Principal Component Analysis (PCA) is a technique used to reduce the dimensionality of a dataset while preserving most of its original variation. However, PCA is a linear method and may not work well when the data has a non-linear structure. In such cases, Kernel PCA can be used instead of PCA. In this lab, we will demonstrate the differences between PCA and Kernel PCA and how to use them.

## Steps

### Step 1: Load the dataset

We will create a dataset made of two nested circles using the `make_circles` function from `sklearn.datasets`.

```python
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```

### Step 2: Visualize the dataset

We will plot the generated dataset using matplotlib to visualize the dataset.

```python
import matplotlib.pyplot as plt

_, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))

train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Feature #1")
train_ax.set_xlabel("Feature #0")
train_ax.set_title("Training data")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Feature #0")
_ = test_ax.set_title("Testing data")
```

### Step 3: Use PCA to project the dataset

PCA is used to project the dataset onto a new space that preserves most of its original variation.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_test_pca = pca.fit(X_train).transform(X_test)
```

### Step 4: Use Kernel PCA to project the dataset

Kernel PCA is used to project the dataset onto a new space that preserves most of its original variation, but also allows for non-linear structures.

```python
from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
```

### Step 5: Visualize the PCA and Kernel PCA projections

We will plot the PCA and Kernel PCA projections to visualize the differences between them.

```python
fig, (orig_data_ax, pca_proj_ax, kernel_pca_proj_ax) = plt.subplots(
    ncols=3, figsize=(14, 4)
)

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("Principal component #1")
pca_proj_ax.set_xlabel("Principal component #0")
pca_proj_ax.set_title("Projection of testing data\n using PCA")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Principal component #1")
kernel_pca_proj_ax.set_xlabel("Principal component #0")
_ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA")
```

### Step 6: Back-project the Kernel PCA projection to the original space

We will use the `inverse_transform` method of Kernel PCA to back-project the Kernel PCA projection to the original space.

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))
```

### Step 7: Visualize the reconstructed dataset

We will plot the original dataset and the reconstructed dataset to compare them.

```python
fig, (orig_data_ax, pca_back_proj_ax, kernel_pca_back_proj_ax) = plt.subplots(
    ncols=3, sharex=True, sharey=True, figsize=(13, 4)
)

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Original test data")

pca_back_proj_ax.scatter(X_reconstructed_pca[:, 0], X_reconstructed_pca[:, 1], c=y_test)
pca_back_proj_ax.set_xlabel("Feature #0")
pca_back_proj_ax.set_title("Reconstruction via PCA")

kernel_pca_back_proj_ax.scatter(
    X_reconstructed_kernel_pca[:, 0], X_reconstructed_kernel_pca[:, 1], c=y_test
)
kernel_pca_back_proj_ax.set_xlabel("Feature #0")
_ = kernel_pca_back_proj_ax.set_title("Reconstruction via KernelPCA")
```

## Summary

In this lab, we learned about the differences between PCA and Kernel PCA. We used PCA and Kernel PCA to project a dataset onto a new space, and visualized the projections. We also used Kernel PCA to back-project the projection to the original space and compared it with the original dataset.
