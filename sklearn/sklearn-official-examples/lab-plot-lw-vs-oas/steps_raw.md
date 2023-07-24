# Comparison of Covariance Estimators

## Introduction

Covariance estimation is an important task in statistical analysis. In this lab, we will compare two methods of covariance estimation: Ledoit-Wolf and OAS. We will use Gaussian distributed data to compare the estimated MSE of these two methods.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries for this lab. We will be using `numpy` for numerical calculations, `matplotlib` for visualizations, and `scikit-learn` for covariance estimation.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz, cholesky
from sklearn.covariance import LedoitWolf, OAS
```

### Step 2: Generate Data

Next, we will generate Gaussian distributed data with a covariance matrix that follows an AR(1) process. We will use `toeplitz` and `cholesky` functions from `scipy.linalg` to generate the covariance matrix.

```python
np.random.seed(0)

n_features = 100
r = 0.1
real_cov = toeplitz(r ** np.arange(n_features))
coloring_matrix = cholesky(real_cov)
```

### Step 3: Compute MSE and Shrinkage

We will compare the Ledoit-Wolf and OAS methods using the simulated data. We will compute the mean squared error (MSE) and shrinkage of both methods.

```python
n_samples_range = np.arange(6, 31, 1)
repeat = 100
lw_mse = np.zeros((n_samples_range.size, repeat))
oa_mse = np.zeros((n_samples_range.size, repeat))
lw_shrinkage = np.zeros((n_samples_range.size, repeat))
oa_shrinkage = np.zeros((n_samples_range.size, repeat))

for i, n_samples in enumerate(n_samples_range):
    for j in range(repeat):
        X = np.dot(np.random.normal(size=(n_samples, n_features)), coloring_matrix.T)

        lw = LedoitWolf(store_precision=False, assume_centered=True)
        lw.fit(X)
        lw_mse[i, j] = lw.error_norm(real_cov, scaling=False)
        lw_shrinkage[i, j] = lw.shrinkage_

        oa = OAS(store_precision=False, assume_centered=True)
        oa.fit(X)
        oa_mse[i, j] = oa.error_norm(real_cov, scaling=False)
        oa_shrinkage[i, j] = oa.shrinkage_
```

### Step 4: Plot Results

Finally, we will plot the results to compare the MSE and shrinkage of the Ledoit-Wolf and OAS methods.

```python
plt.subplot(2, 1, 1)
plt.errorbar(
    n_samples_range,
    lw_mse.mean(1),
    yerr=lw_mse.std(1),
    label="Ledoit-Wolf",
    color="navy",
    lw=2,
)
plt.errorbar(
    n_samples_range,
    oa_mse.mean(1),
    yerr=oa_mse.std(1),
    label="OAS",
    color="darkorange",
    lw=2,
)
plt.ylabel("Squared error")
plt.legend(loc="upper right")
plt.title("Comparison of covariance estimators")
plt.xlim(5, 31)

plt.subplot(2, 1, 2)
plt.errorbar(
    n_samples_range,
    lw_shrinkage.mean(1),
    yerr=lw_shrinkage.std(1),
    label="Ledoit-Wolf",
    color="navy",
    lw=2,
)
plt.errorbar(
    n_samples_range,
    oa_shrinkage.mean(1),
    yerr=oa_shrinkage.std(1),
    label="OAS",
    color="darkorange",
    lw=2,
)
plt.xlabel("n_samples")
plt.ylabel("Shrinkage")
plt.legend(loc="lower right")
plt.ylim(plt.ylim()[0], 1.0 + (plt.ylim()[1] - plt.ylim()[0]) / 10.0)
plt.xlim(5, 31)

plt.show()
```

## Summary

In this lab, we compared the Ledoit-Wolf and OAS methods for covariance estimation using Gaussian distributed data. We plotted the MSE and shrinkage of both methods and found that the OAS method has better convergence under the assumption that the data are Gaussian.
