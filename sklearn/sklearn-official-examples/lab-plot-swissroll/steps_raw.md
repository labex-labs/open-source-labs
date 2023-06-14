# Swiss Roll and Swiss-Hole Reduction

## Introduction

This lab compares two popular non-linear dimensionality techniques, Locally Linear Embedding (LLE) and T-distributed Stochastic Neighbor Embedding (t-SNE), on the classic Swiss Roll dataset. We will explore how they both deal with the addition of a hole in the data.

## Steps

### Step 1: Generate Swiss Roll Dataset

We start by generating the Swiss Roll dataset using the `make_swiss_roll()` function from `sklearn.datasets`. This function generates a 3D dataset with a spiral shape.

```python
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

sr_points, sr_color = datasets.make_swiss_roll(n_samples=1500, random_state=0)
```

### Step 2: Visualize Swiss Roll Dataset

We can visualize the generated Swiss Roll dataset using a 3D scatter plot with different colors representing different points.

```python
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
fig.add_axes(ax)
ax.scatter(sr_points[:, 0], sr_points[:, 1], sr_points[:, 2], c=sr_color, s=50, alpha=0.8)
ax.set_title("Swiss Roll in Ambient Space")
ax.view_init(azim=-66, elev=12)
_ = ax.text2D(0.8, 0.05, s="n_samples=1500", transform=ax.transAxes)
```

### Step 3: Compute LLE and t-SNE Embeddings of Swiss Roll Dataset

We compute the LLE and t-SNE embeddings of the Swiss Roll dataset using the `manifold.locally_linear_embedding()` and `manifold.TSNE()` functions from `sklearn`, respectively.

```python
sr_lle, sr_err = manifold.locally_linear_embedding(sr_points, n_neighbors=12, n_components=2)

sr_tsne = manifold.TSNE(n_components=2, perplexity=40, random_state=0).fit_transform(sr_points)
```

### Step 4: Visualize LLE and t-SNE Embeddings of Swiss Roll Dataset

We can visualize the LLE and t-SNE embeddings of the Swiss Roll dataset using scatter plots with different colors representing different points.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sr_lle[:, 0], sr_lle[:, 1], c=sr_color)
axs[0].set_title("LLE Embedding of Swiss Roll")
axs[1].scatter(sr_tsne[:, 0], sr_tsne[:, 1], c=sr_color)
_ = axs[1].set_title("t-SNE Embedding of Swiss Roll")
```

### Step 5: Generate Swiss-Hole Dataset

We generate the Swiss-Hole dataset by adding a hole to the Swiss Roll dataset using the `hole=True` parameter in the `make_swiss_roll()` function.

```python
sh_points, sh_color = datasets.make_swiss_roll(n_samples=1500, hole=True, random_state=0)
```

### Step 6: Visualize Swiss-Hole Dataset

We can visualize the generated Swiss-Hole dataset using a 3D scatter plot with different colors representing different points.

```python
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
fig.add_axes(ax)
ax.scatter(sh_points[:, 0], sh_points[:, 1], sh_points[:, 2], c=sh_color, s=50, alpha=0.8)
ax.set_title("Swiss-Hole in Ambient Space")
ax.view_init(azim=-66, elev=12)
_ = ax.text2D(0.8, 0.05, s="n_samples=1500", transform=ax.transAxes)
```

### Step 7: Compute LLE and t-SNE Embeddings of Swiss-Hole Dataset

We compute the LLE and t-SNE embeddings of the Swiss-Hole dataset using the `manifold.locally_linear_embedding()` and `manifold.TSNE()` functions from `sklearn`, respectively.

```python
sh_lle, sh_err = manifold.locally_linear_embedding(sh_points, n_neighbors=12, n_components=2)

sh_tsne = manifold.TSNE(n_components=2, perplexity=40, init="random", random_state=0).fit_transform(sh_points)
```

### Step 8: Visualize LLE and t-SNE Embeddings of Swiss-Hole Dataset

We can visualize the LLE and t-SNE embeddings of the Swiss-Hole dataset using scatter plots with different colors representing different points.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sh_lle[:, 0], sh_lle[:, 1], c=sh_color)
axs[0].set_title("LLE Embedding of Swiss-Hole")
axs[1].scatter(sh_tsne[:, 0], sh_tsne[:, 1], c=sh_color)
_ = axs[1].set_title("t-SNE Embedding of Swiss-Hole")
```

## Summary

This lab compared the LLE and t-SNE embeddings of the classic Swiss Roll dataset and the Swiss-Hole dataset. We visualized the datasets and their embeddings using scatter plots. We observed that LLE was able to unroll the Swiss Roll and Swiss-Hole datasets effectively, while t-SNE preserved the general structure of the data but tended to clump sections of points together.
