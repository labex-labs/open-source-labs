# Gaussian Process Classification

## Introduction

This lab demonstrates how to use Gaussian Process Classification (GPC) in scikit-learn library for Python. The aim is to show how to train and test a GPC model, plot iso-probability lines, and evaluate the classification performance.

## Steps

### Step 1: Import Required Libraries

First, we need to import the required libraries.

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import DotProduct, ConstantKernel as C
```

### Step 2: Prepare Data

We will generate some synthetic data for classification. The function to be classified is defined as:

```python
def g(x):
    """The function to predict (classification will then consist in predicting
    whether g(x) <= 0 or not)"""
    return 5.0 - x[:, 1] - 0.5 * x[:, 0] ** 2.0
```

Then, we need to create the design of experiments and observations.

```python
# A few constants
lim = 8

# Design of experiments
X = np.array(
    [
        [-4.61611719, -6.00099547],
        [4.10469096, 5.32782448],
        [0.00000000, -0.50000000],
        [-6.17289014, -4.6984743],
        [1.3109306, -6.93271427],
        [-5.03823144, 3.10584743],
        [-2.87600388, 6.74310541],
        [5.21301203, 4.26386883],
    ]
)

# Observations
y = np.array(g(X) > 0, dtype=int)
```

### Step 3: Train the Model

We will use a GPC model to classify the data. First, we need to specify the kernel function.

```python
kernel = C(0.1, (1e-5, np.inf)) * DotProduct(sigma_0=0.1) ** 2
```

Then, we can create a GPC model and train it using the data.

```python
gp = GaussianProcessClassifier(kernel=kernel)
gp.fit(X, y)
```

### Step 4: Evaluate the Model

We will evaluate the classification performance of the trained GPC model. We will generate a grid of points and calculate the predicted probabilities for each point using the trained model.

```python
# Evaluate real function and the predicted probability
res = 50
x1, x2 = np.meshgrid(np.linspace(-lim, lim, res), np.linspace(-lim, lim, res))
xx = np.vstack([x1.reshape(x1.size), x2.reshape(x2.size)]).T

y_true = g(xx)
y_prob = gp.predict_proba(xx)[:, 1]
y_true = y_true.reshape((res, res))
y_prob = y_prob.reshape((res, res))
```

### Step 5: Plot the Results

We will plot the iso-probability lines and the classification boundary of the GPC model.

```python
# Plot the probabilistic classification iso-values
fig = plt.figure(1)
ax = fig.gca()
ax.axes.set_aspect("equal")
plt.xticks([])
plt.yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")

cax = plt.imshow(y_prob, cmap=cm.gray_r, alpha=0.8, extent=(-lim, lim, -lim, lim))
norm = plt.matplotlib.colors.Normalize(vmin=0.0, vmax=0.9)
cb = plt.colorbar(cax, ticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0], norm=norm)
cb.set_label(r"${\rm \mathbb{P}}\left[\widehat{G}(\mathbf{x}) \leq 0\right]$")
plt.clim(0, 1)

plt.plot(X[y <= 0, 0], X[y <= 0, 1], "r.", markersize=12)

plt.plot(X[y > 0, 0], X[y > 0, 1], "b.", markersize=12)

plt.contour(x1, x2, y_true, [0.0], colors="k", linestyles="dashdot")

cs = plt.contour(x1, x2, y_prob, [0.666], colors="b", linestyles="solid")
plt.clabel(cs, fontsize=11)

cs = plt.contour(x1, x2, y_prob, [0.5], colors="k", linestyles="dashed")
plt.clabel(cs, fontsize=11)

cs = plt.contour(x1, x2, y_prob, [0.334], colors="r", linestyles="solid")
plt.clabel(cs, fontsize=11)

plt.show()
```

### Summary

In this lab, we have learned how to use Gaussian Process Classification (GPC) in scikit-learn library for Python. We have shown how to train and test a GPC model, plot iso-probability lines, and evaluate the classification performance.
