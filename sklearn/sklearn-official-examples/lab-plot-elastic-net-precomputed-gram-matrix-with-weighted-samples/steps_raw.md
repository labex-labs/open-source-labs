# Precomputing Gram Matrix and Weighted Samples for Elastic Net

## Introduction

This lab demonstrates how to precompute the gram matrix while using weighted samples with an ElasticNet. It is important to note that if weighted samples are used, the design matrix must be centered and then rescaled by the square root of the weight vector before the gram matrix is computed.

## Steps

### Step 1: Loading the Dataset and Creating Sample Weights

We start by loading the dataset and creating some sample weights. We use the `make_regression` function from scikit-learn to generate a random regression dataset with 100,000 samples. Then, we generate a lognormal weight vector and normalize it to sum to the total number of samples.

```python
import numpy as np
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)

n_samples = int(1e5)
X, y = make_regression(n_samples=n_samples, noise=0.5, random_state=rng)

sample_weight = rng.lognormal(size=n_samples)
# normalize the sample weights
normalized_weights = sample_weight * (n_samples / (sample_weight.sum()))
```

### Step 2: Precomputing Gram Matrix with Weighted Samples

To fit the elastic net using the `precompute` option together with the sample weights, we must first center the design matrix and rescale it by the normalized weights prior to computing the gram matrix. We center the design matrix by subtracting the weighted average of each feature column from each row. Then, we rescale the centered design matrix by multiplying each row with the square root of the corresponding normalized weight. Finally, we compute the gram matrix by taking the dot product of the rescaled design matrix with its transpose.

```python
X_offset = np.average(X, axis=0, weights=normalized_weights)
X_centered = X - np.average(X, axis=0, weights=normalized_weights)
X_scaled = X_centered * np.sqrt(normalized_weights)[:, np.newaxis]
gram = np.dot(X_scaled.T, X_scaled)
```

### Step 3: Fitting the Elastic Net

We can now proceed with fitting. We must pass the centered design matrix to `fit` to prevent the elastic net estimator from detecting that it is uncentered and discarding the gram matrix we passed. However, if we pass the scaled design matrix, the preprocessing code will incorrectly rescale it a second time. We also pass the normalized weights to the `sample_weight` parameter of the `fit` function.

```python
from sklearn.linear_model import ElasticNet

lm = ElasticNet(alpha=0.01, precompute=gram)
lm.fit(X_centered, y, sample_weight=normalized_weights)
```

## Summary

This lab demonstrated how to precompute the gram matrix while using weighted samples with an ElasticNet. We first loaded a regression dataset and created a lognormal weight vector which was normalized to sum to the total number of samples. We then centered the design matrix, rescaled it by the normalized weights, and computed the gram matrix. Finally, we fit the elastic net using the precomputed gram matrix and the normalized weights.
