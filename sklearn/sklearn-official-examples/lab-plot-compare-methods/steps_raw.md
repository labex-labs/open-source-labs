# Manifold Learning Comparison

## Introduction

In this lab, we will compare different Manifold Learning algorithms to perform non-linear dimensionality reduction. The purpose of this is to reduce the dimensionality of the dataset while preserving the original data's essential features.

We will be using the S-curve dataset, which is a commonly used dataset for dimensionality reduction. We will use algorithms like Locally Linear Embeddings, Isomap Embedding, Multidimensional Scaling, Spectral Embedding, and T-distributed Stochastic Neighbor Embedding.

## Steps

### Step 1: Dataset Preparation

We start by generating the S-curve dataset.

```python
import matplotlib.pyplot as plt
from matplotlib import ticker

# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl_toolkits.mplot3d  # noqa: F401

from sklearn import manifold, datasets

n_samples = 1500
S_points, S_color = datasets.make_s_curve(n_samples, random_state=0)

```

### Step 2: Locally Linear Embeddings

Locally linear embedding (LLE) is a series of local Principal Component Analyses which are globally compared to find the best non-linear embedding. We will be using four different methods of LLE, i.e., Standard, Local tangent space alignment, Hessian eigenmap, and Modified locally linear embedding.

```python
params = {
    "n_neighbors": n_neighbors,
    "n_components": n_components,
    "eigen_solver": "auto",
    "random_state": 0,
}

lle_standard = manifold.LocallyLinearEmbedding(method="standard", **params)
S_standard = lle_standard.fit_transform(S_points)

lle_ltsa = manifold.LocallyLinearEmbedding(method="ltsa", **params)
S_ltsa = lle_ltsa.fit_transform(S_points)

lle_hessian = manifold.LocallyLinearEmbedding(method="hessian", **params)
S_hessian = lle_hessian.fit_transform(S_points)

lle_mod = manifold.LocallyLinearEmbedding(method="modified", **params)
S_mod = lle_mod.fit_transform(S_points)
```

### Step 3: Isomap Embedding

Isomap seeks a lower-dimensional embedding that maintains geodesic distances between all points.

```python
isomap = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, p=1)
S_isomap = isomap.fit_transform(S_points)
```

### Step 4: Multidimensional Scaling

Multidimensional scaling (MDS) seeks a low-dimensional representation of the data in which the distances respect well the distances in the original high-dimensional space.

```python
md_scaling = manifold.MDS(
    n_components=n_components,
    max_iter=50,
    n_init=4,
    random_state=0,
    normalized_stress=False,
)
S_scaling = md_scaling.fit_transform(S_points)
```

### Step 5: Spectral Embedding for Non-linear Dimensionality Reduction

This implementation uses Laplacian Eigenmaps, which finds a low dimensional representation of the data using a spectral decomposition of the graph Laplacian.

```python
spectral = manifold.SpectralEmbedding(
    n_components=n_components, n_neighbors=n_neighbors
)
S_spectral = spectral.fit_transform(S_points)
```

### Step 6: T-distributed Stochastic Neighbor Embedding

It converts similarities between data points to joint probabilities and tries to minimize the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embedding and the high-dimensional data.

```python
t_sne = manifold.TSNE(
    n_components=n_components,
    perplexity=30,
    init="random",
    n_iter=250,
    random_state=0,
)
S_t_sne = t_sne.fit_transform(S_points)
```

### Summary

Manifold Learning is an approach to non-linear dimensionality reduction. In this lab, we compared different Manifold Learning algorithms like Locally Linear Embeddings, Isomap Embedding, Multidimensional Scaling, Spectral Embedding, and T-distributed Stochastic Neighbor Embedding to perform non-linear dimensionality reduction on the S-curve dataset.
