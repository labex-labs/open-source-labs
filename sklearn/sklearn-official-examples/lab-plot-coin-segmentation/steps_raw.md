# Segmenting Greek Coins with Spectral Clustering

## Introduction

In this lab, we will use spectral clustering to segment an image of Greek coins into multiple partly-homogeneous regions. Spectral clustering is a powerful technique that can be used to identify clusters in a dataset based on the similarity between their features. In this lab, we will use spectral clustering to segment an image by creating a graph from voxel-to-voxel difference on an image and then breaking the image into multiple partly-homogeneous regions.

## Steps

### Step 1: Load and preprocess the image

We will start by loading the image of Greek coins and pre-processing it to make it easier to work with. We will resize the image to 20% of the original size and apply a Gaussian filter for smoothing prior to down-scaling to reduce aliasing artifacts.

```python
# load the coins as a numpy array
orig_coins = coins()

# Resize it to 20% of the original size to speed up the processing
# Applying a Gaussian filter for smoothing prior to down-scaling
# reduces aliasing artifacts.
smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(smoothened_coins, 0.2, mode="reflect", anti_aliasing=False)
```

### Step 2: Convert the image into a graph with the value of the gradient on the edges

We will convert the image into a graph with the value of the gradient on the edges. The smaller beta is, the more independent the segmentation is of the actual image. For beta=1, the segmentation is close to a voronoi.

```python
# Convert the image into a graph with the value of the gradient on the
# edges.
graph = image.img_to_graph(rescaled_coins)

# Take a decreasing function of the gradient: an exponential
beta = 10
eps = 1e-6
graph.data = np.exp(-beta * graph.data / graph.data.std()) + eps
```

### Step 3: Apply spectral clustering

We will apply spectral clustering using the default eigen_solver='arpack'. Any implemented solver can be used: eigen_solver='arpack', 'lobpcg', or 'amg'. Choosing eigen_solver='amg' requires an extra package called 'pyamg'. The quality of segmentation and the speed of calculations is mostly determined by the choice of the solver and the value of the tolerance 'eigen_tol'.

```python
# Apply spectral clustering using the default eigen_solver='arpack'.
# Any implemented solver can be used: eigen_solver='arpack', 'lobpcg', or 'amg'.
# Choosing eigen_solver='amg' requires an extra package called 'pyamg'.
# The quality of segmentation and the speed of calculations is mostly determined
# by the choice of the solver and the value of the tolerance 'eigen_tol'.
n_regions = 26
n_regions_plus = 3
for assign_labels in ("kmeans", "discretize", "cluster_qr"):
    t0 = time.time()
    labels = spectral_clustering(
        graph,
        n_clusters=(n_regions + n_regions_plus),
        eigen_tol=1e-7,
        assign_labels=assign_labels,
        random_state=42,
    )
    t1 = time.time()
    labels = labels.reshape(rescaled_coins.shape)
```

### Step 4: Visualize the segmentation

We will visualize the resulting regions by plotting the original image and overlaying the contours of the segmented regions.

```python
plt.figure(figsize=(5, 5))
plt.imshow(rescaled_coins, cmap=plt.cm.gray)
plt.xticks(())
plt.yticks(())
title = "Spectral clustering: %s, %.2fs" % (assign_labels, (t1 - t0))
print(title)
plt.title(title)
for l in range(n_regions):
    colors = [plt.cm.nipy_spectral((l + 4) / float(n_regions + 4))]
    plt.contour(labels == l, colors=colors)
plt.show()
```

## Summary

In this lab, we used spectral clustering to segment an image of Greek coins into multiple partly-homogeneous regions. We preprocessed the image, converted it into a graph with the value of the gradient on the edges, applied spectral clustering, and visualized the resulting regions. Spectral clustering is a powerful technique that can be used to identify clusters in a dataset based on the similarity between their features.
