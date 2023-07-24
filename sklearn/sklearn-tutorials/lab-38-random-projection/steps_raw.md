# Random Projection

## Introduction

In this lab, we will explore random projection in dimensionality reduction using the scikit-learn library. Random projection is a technique that can be used to reduce the dimensionality of data while preserving the pairwise distances between samples. This can be useful for speeding up computations and reducing memory usage in machine learning algorithms.

## Steps

### Step 1: Import the required libraries

Let's start by importing the required libraries for this lab.

```python
import numpy as np
from sklearn import random_projection
```

### Step 2: Generate random data

Next, let's generate some random data that we can use for dimensionality reduction.

```python
X = np.random.rand(100, 10000)
```

Here, we generate a 2D array `X` with 100 samples and 10,000 features. This will be our original high-dimensional data.

### Step 3: Gaussian random projection

Now, let's apply Gaussian random projection to reduce the dimensionality of our data.

```python
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
```

In this step, we create an instance of the `GaussianRandomProjection` class and fit it to our data `X`. Then, we apply the transformation by calling the `fit_transform` method. The result is stored in the `X_new` variable.

### Step 4: Sparse random projection

Next, let's try another type of random projection called sparse random projection.

```python
transformer = random_projection.SparseRandomProjection()
X_new = transformer.fit_transform(X)
```

Here, we create an instance of the `SparseRandomProjection` class and apply it to our data `X` using the `fit_transform` method. The result is stored in the `X_new` variable.

### Step 5: Inverse transform

Random projection transformers have an option to compute the inverse of the projection matrix. Let's explore this feature by applying the inverse transform to our projected data.

```python
transformer = random_projection.SparseRandomProjection(compute_inverse_components=True)
X_new = transformer.fit_transform(X)

# Compute the inverse transform
X_new_inversed = transformer.inverse_transform(X_new)
```

In this step, we create an instance of the `SparseRandomProjection` class with the `compute_inverse_components` parameter set to `True`. Then, we fit the transformer to our data `X` and apply the transformation. Finally, we compute the inverse transform by calling the `inverse_transform` method on the projected data `X_new`.

### Step 6: Verification

To verify the correctness of the inverse transform, we can compare the original data `X` with the result of the inverse transform.

```python
X_new_again = transformer.transform(X_new_inversed)
np.allclose(X_new, X_new_again)
```

Here, we apply the transform to the inverse transformed data `X_new_inversed` and check if it is equal to the original projected data `X_new` using the `np.allclose` function.

## Summary

In this lab, we learned how to perform random projection for dimensionality reduction using the scikit-learn library. We explored both Gaussian random projection and sparse random projection techniques. We also learned how to compute the inverse transform of the projected data to recover the original data. Random projection can be a useful tool for reducing the dimensionality of high-dimensional data in machine learning tasks.
