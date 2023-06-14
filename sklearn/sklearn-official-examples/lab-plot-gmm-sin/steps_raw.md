# Gaussian Mixture Model Sine Curve

## Introduction

In this lab, we will use the Gaussian Mixture Model algorithm to fit a dataset that follows a noisy sine curve. We will use two different types of Gaussian Mixture Models, namely the Expectation-Maximization algorithm and the Bayesian Gaussian Mixture Model with a Dirichlet process prior.

## Steps

### Step 1: Load Required Libraries

We will start by loading the required libraries for this lab.

```python
import itertools

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn import mixture
```

### Step 2: Generate Dataset

Next, we will generate a dataset that follows a noisy sine curve.

```python
# Parameters
n_samples = 100

# Generate random sample following a sine curve
np.random.seed(0)
X = np.zeros((n_samples, 2))
step = 4.0 * np.pi / n_samples

for i in range(X.shape[0]):
    x = i * step - 6.0
    X[i, 0] = x + np.random.normal(0, 0.1)
    X[i, 1] = 3.0 * (np.sin(x) + np.random.normal(0, 0.2))
```

### Step 3: Fit a Gaussian Mixture Model with EM

We will fit a classical Gaussian Mixture Model with 10 components fit with the Expectation-Maximization algorithm.

```python
# Fit a Gaussian mixture with EM using ten components
gmm = mixture.GaussianMixture(
    n_components=10, covariance_type="full", max_iter=100
).fit(X)
```

### Step 4: Plot the Results of EM Algorithm

We will plot the results of the Expectation-Maximization algorithm.

```python
def plot_results(X, Y, means, covariances, index, title):
    splot = plt.subplot(5, 1, 1 + index)
    for i, (mean, covar, color) in enumerate(zip(means, covariances, color_iter)):
        v, w = linalg.eigh(covar)
        v = 2.0 * np.sqrt(2.0) * np.sqrt(v)
        u = w[0] / linalg.norm(w[0])
        # as the DP will not use every component it has access to
        # unless it needs it, we shouldn't plot the redundant
        # components.
        if not np.any(Y == i):
            continue
        plt.scatter(X[Y == i, 0], X[Y == i, 1], 0.8, color=color)

        # Plot an ellipse to show the Gaussian component
        angle = np.arctan(u[1] / u[0])
        angle = 180.0 * angle / np.pi  # convert to degrees
        ell = mpl.patches.Ellipse(mean, v[0], v[1], angle=180.0 + angle, color=color)
        ell.set_clip_box(splot.bbox)
        ell.set_alpha(0.5)
        splot.add_artist(ell)

    plt.xlim(-6.0, 4.0 * np.pi - 6.0)
    plt.ylim(-5.0, 5.0)
    plt.title(title)
    plt.xticks(())
    plt.yticks(())

plot_results(
    X, gmm.predict(X), gmm.means_, gmm.covariances_, 0, "Expectation-maximization"
)
```

### Step 5: Fit a Bayesian Gaussian Mixture Model with a Dirichlet process prior

We will now fit a Bayesian Gaussian Mixture Model with a Dirichlet process prior. We will set a low value of the concentration prior to make the model favor a lower number of active components.

```python
dpgmm = mixture.BayesianGaussianMixture(
    n_components=10,
    covariance_type="full",
    weight_concentration_prior=1e-2,
    weight_concentration_prior_type="dirichlet_process",
    mean_precision_prior=1e-2,
    covariance_prior=1e0 * np.eye(2),
    init_params="random",
    max_iter=100,
    random_state=2,
).fit(X)
```

### Step 6: Plot the Results of Bayesian GMM with Low Concentration Prior

We will plot the results of the Bayesian Gaussian Mixture Model with a Dirichlet process prior and a low value of the concentration prior.

```python
plot_results(
    X,
    dpgmm.predict(X),
    dpgmm.means_,
    dpgmm.covariances_,
    1,
    "Bayesian Gaussian mixture models with a Dirichlet process prior "
    r"for $\gamma_0=0.01$.",
)
```

### Step 7: Sample from Bayesian GMM with Low Concentration Prior

We will now sample from the Bayesian Gaussian Mixture Model with a Dirichlet process prior and a low value of the concentration prior.

```python
X_s, y_s = dpgmm.sample(n_samples=2000)
plot_samples(
    X_s,
    y_s,
    dpgmm.n_components,
    0,
    "Gaussian mixture with a Dirichlet process prior "
    r"for $\gamma_0=0.01$ sampled with $2000$ samples.",
)
```

### Step 8: Fit a Bayesian Gaussian Mixture Model with a Dirichlet process prior

We will now fit a Bayesian Gaussian Mixture Model with a Dirichlet process prior. We will set a high value of the concentration prior to give the model more liberty to model the fine-grained structure of the data.

```python
dpgmm = mixture.BayesianGaussianMixture(
    n_components=10,
    covariance_type="full",
    weight_concentration_prior=1e2,
    weight_concentration_prior_type="dirichlet_process",
    mean_precision_prior=1e-2,
    covariance_prior=1e0 * np.eye(2),
    init_params="kmeans",
    max_iter=100,
    random_state=2,
).fit(X)
```

### Step 9: Plot the Results of Bayesian GMM with High Concentration Prior

We will plot the results of the Bayesian Gaussian Mixture Model with a Dirichlet process prior and a high value of the concentration prior.

```python
plot_results(
    X,
    dpgmm.predict(X),
    dpgmm.means_,
    dpgmm.covariances_,
    2,
    "Bayesian Gaussian mixture models with a Dirichlet process prior "
    r"for $\gamma_0=100$",
)
```

### Step 10: Sample from Bayesian GMM with High Concentration Prior

We will now sample from the Bayesian Gaussian Mixture Model with a Dirichlet process prior and a high value of the concentration prior.

```python
X_s, y_s = dpgmm.sample(n_samples=2000)
plot_samples(
    X_s,
    y_s,
    dpgmm.n_components,
    1,
    "Gaussian mixture with a Dirichlet process prior "
    r"for $\gamma_0=100$ sampled with $2000$ samples.",
)
```

## Summary

In this lab, we used the Gaussian Mixture Model algorithm to fit a dataset that follows a noisy sine curve. We used two different types of Gaussian Mixture Models, namely the Expectation-Maximization algorithm and the Bayesian Gaussian Mixture Model with a Dirichlet process prior. We plotted the results and sampled from both models to compare their performance. The choice of the best model is subjective and depends on whether we want to focus on the big picture or closely follow the high density regions of the signal.
