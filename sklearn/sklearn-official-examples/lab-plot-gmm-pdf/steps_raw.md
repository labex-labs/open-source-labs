# Density Estimation with Gaussian Mixture Models

## Introduction

In this lab, we will use the scikit-learn library to generate a Gaussian mixture dataset. We will then fit a Gaussian Mixture Model (GMM) to the dataset and plot the density estimation of the mixture of Gaussians. GMMs can be used to model and estimate the probability distribution of a dataset.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries: NumPy for numerical computations and Matplotlib for visualizations. We will also import the GaussianMixture class from the scikit-learn library to fit the GMM to our dataset.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import mixture
```

### Step 2: Generate Data

Next, we will generate a Gaussian mixture dataset with two components. We will create a shifted Gaussian dataset centered on (20, 20) and a zero-centered stretched Gaussian dataset. We will then concatenate the two datasets into the final training set.

```python
n_samples = 300

# generate random sample, two components
np.random.seed(0)

# generate spherical data centered on (20, 20)
shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

# generate zero centered stretched Gaussian data
C = np.array([[0.0, -0.7], [3.5, 0.7]])
stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

# concatenate the two datasets into the final training set
X_train = np.vstack([shifted_gaussian, stretched_gaussian])
```

### Step 3: Fit Gaussian Mixture Model

We will now fit a GMM to the dataset using the GaussianMixture class from scikit-learn. We will set the number of components to 2 and the covariance type to "full".

```python
# fit a Gaussian Mixture Model with two components
clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)
```

### Step 4: Plot Density Estimation

We will now plot the density estimation of the mixture of Gaussians. We will create a meshgrid of points over the range of the dataset and calculate the negative log-likelihood predicted by the GMM for each point. We will then display the predicted scores as a contour plot and scatter plot the training data.

```python
# display predicted scores by the model as a contour plot
x = np.linspace(-20.0, 30.0)
y = np.linspace(-20.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)

plt.title("Density Estimation with Gaussian Mixture Models")
plt.axis("tight")
plt.show()
```

## Summary

In this lab, we learned how to use scikit-learn to generate a Gaussian mixture dataset and fit a GMM to the dataset. We also plotted the density estimation of the mixture of Gaussians using a contour plot.
