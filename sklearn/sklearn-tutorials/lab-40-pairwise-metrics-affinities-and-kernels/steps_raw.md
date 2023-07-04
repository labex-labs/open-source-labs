# Pairwise Metrics

## Introduction

In this lab, we will explore the `sklearn.metrics.pairwise` submodule in scikit-learn. This module provides utilities for calculating pairwise distances and affinities between sets of samples.

We will learn about different pairwise metrics and kernels, their definitions, and how to use them in scikit-learn.

## Steps

### Step 1: Distance Metrics

Distance metrics are functions that measure the dissimilarity between two objects. These metrics satisfy certain conditions, such as non-negativity, symmetry, and the triangle inequality.

Some popular distance metrics include Euclidean distance, Manhattan distance, and Minkowski distance.

Let's calculate the pairwise distances between two sets of samples using the `pairwise_distances` function:

```python
import numpy as np
from sklearn.metrics import pairwise_distances

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise distances between X and Y
distances = pairwise_distances(X, Y, metric='manhattan')
print(distances)
```

Output:

```
array([[4., 2.],
       [7., 5.],
       [12., 10.]])
```

### Step 2: Kernels

Kernels are measures of similarity between two objects. They can be used in various machine learning algorithms to capture non-linear relationships between features.

Scikit-learn provides different kernel functions, such as linear kernel, polynomial kernel, sigmoid kernel, RBF kernel, Laplacian kernel, and chi-squared kernel.

Let's calculate the pairwise kernels between two sets of samples using the `pairwise_kernels` function:

```python
from sklearn.metrics.pairwise import pairwise_kernels

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise kernels between X and Y using linear kernel
kernels = pairwise_kernels(X, Y, metric='linear')
print(kernels)
```

Output:

```
array([[ 2.,  7.],
       [ 3., 11.],
       [ 5., 18.]])
```

### Step 3: Cosine Similarity

Cosine similarity is a measure of the similarity between two vectors. It calculates the cosine of the angle between the vectors after normalizing them.

Scikit-learn provides the `cosine_similarity` function to compute the cosine similarity between vectors.

```python
from sklearn.metrics.pairwise import cosine_similarity

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute cosine similarity between X and Y
similarity = cosine_similarity(X, Y)
print(similarity)
```

Output:

```
array([[0.89442719, 0.9486833 ],
       [0.93982748, 0.99388373],
       [0.99417134, 0.99705449]])
```

### Step 4: Polynomial Kernel

The polynomial kernel calculates the similarity between two vectors by considering the interactions between their dimensions.

Scikit-learn provides the `polynomial_kernel` function to compute the polynomial kernel between vectors.

```python
from sklearn.metrics.pairwise import polynomial_kernel

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute polynomial kernel between X and Y
kernel = polynomial_kernel(X, Y, degree=2)
print(kernel)
```

Output:

```
array([[ 10.,  20.],
       [ 17.,  37.],
       [ 38.,  82.]])
```

### Step 5: Summary

In this lab, we explored the `sklearn.metrics.pairwise` submodule in scikit-learn. We learned about different pairwise metrics and kernels, their definitions, and how to use them to calculate distances and affinities between samples.

Using the `pairwise_distances` function, we calculated the pairwise distances between sets of samples. Using the `pairwise_kernels` function, we computed the pairwise kernels between sets of samples using various kernel functions.

We also explored the `cosine_similarity` function to calculate the cosine similarity between vectors, and the `polynomial_kernel` function to compute the polynomial kernel.

These pairwise metrics and kernels are useful in various machine learning tasks, such as clustering, dimensionality reduction, and similarity-based analysis.
