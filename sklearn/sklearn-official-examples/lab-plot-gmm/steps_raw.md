# Gaussian Mixture Model

## Introduction

This lab will guide you through the implementation of Gaussian Mixture Models (GMMs) using the scikit-learn library in Python. GMMs are probabilistic models that assume that the data is generated from a mixture of several Gaussian distributions. They are widely used in various fields such as computer vision, finance, and bioinformatics for clustering and density estimation tasks.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries for this lab. We will use NumPy for numerical computing, Matplotlib for data visualization, and scikit-learn for GMM implementation.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import mixture
```

### Step 2: Generate Data

In this step, we will generate a sample dataset that consists of two Gaussian distributions with different means and covariances.

```python
n_samples = 500

np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
X = np.r_[
    np.dot(np.random.randn(n_samples, 2), C),
    0.7 * np.random.randn(n_samples, 2) + np.array([-6, 3]),
]
```

### Step 3: Implement Gaussian Mixture Model

In this step, we will implement the Gaussian Mixture Model using the `GaussianMixture` class of scikit-learn. We will fit the model to our dataset and predict the cluster labels for each data point. Finally, we will plot the results.

```python
# Create a GMM object with 5 components
gmm = mixture.GaussianMixture(n_components=5, covariance_type="full")

# Fit the GMM to the data
gmm.fit(X)

# Predict the cluster labels
Y_ = gmm.predict(X)

# Plot the results
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("Gaussian Mixture Model")
plt.show()
```

### Step 4: Implement Bayesian Gaussian Mixture Model

In this step, we will implement the Bayesian Gaussian Mixture Model using the `BayesianGaussianMixture` class of scikit-learn. This model has a Dirichlet process prior that automatically adapts the number of clusters based on the data. We will fit the model to our dataset and predict the cluster labels for each data point. Finally, we will plot the results.

```python
# Create a Bayesian GMM object with 5 components
dpgmm = mixture.BayesianGaussianMixture(n_components=5, covariance_type="full")

# Fit the Bayesian GMM to the data
dpgmm.fit(X)

# Predict the cluster labels
Y_ = dpgmm.predict(X)

# Plot the results
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("Bayesian Gaussian Mixture Model with a Dirichlet process prior")
plt.show()
```

## Summary

In this lab, we have learned how to implement Gaussian Mixture Models using the scikit-learn library in Python. We have also learned how to generate a dataset, fit the models to the data, and plot the results. GMMs are powerful tools for clustering and density estimation tasks and are widely used in various fields.
