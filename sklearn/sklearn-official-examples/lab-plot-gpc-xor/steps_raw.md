# Gaussian Process Classification on XOR Dataset

## Introduction

In this lab, we will go through an example of Gaussian process classification (GPC) on XOR dataset using scikit-learn. We will compare the results obtained by using a stationary, isotropic kernel (RBF) and a non-stationary kernel (DotProduct).

## Steps

### Step 1: Importing Libraries

In this step, we will import the necessary libraries required for this lab.

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF, DotProduct
```

### Step 2: Creating XOR Dataset

In this step, we will create an XOR dataset using numpy. We will use logical_xor function to create labels based on the input features.

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
rng = np.random.RandomState(0)
X = rng.randn(200, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```

### Step 3: Fitting the Model

In this step, we will fit the Gaussian Process Classifier to the dataset. We will use two different kernels for comparison - RBF and DotProduct.

```python
plt.figure(figsize=(10, 5))
kernels = [1.0 * RBF(length_scale=1.15), 1.0 * DotProduct(sigma_0=1.0) ** 2]
for i, kernel in enumerate(kernels):
    clf = GaussianProcessClassifier(kernel=kernel, warm_start=True).fit(X, Y)

    # plot the decision function for each datapoint on the grid
    Z = clf.predict_proba(np.vstack((xx.ravel(), yy.ravel())).T)[:, 1]
    Z = Z.reshape(xx.shape)

    plt.subplot(1, 2, i + 1)
    image = plt.imshow(
        Z,
        interpolation="nearest",
        extent=(xx.min(), xx.max(), yy.min(), yy.max()),
        aspect="auto",
        origin="lower",
        cmap=plt.cm.PuOr_r,
    )
    contours = plt.contour(xx, yy, Z, levels=[0.5], linewidths=2, colors=["k"])
    plt.scatter(X[:, 0], X[:, 1], s=30, c=Y, cmap=plt.cm.Paired, edgecolors=(0, 0, 0))
    plt.xticks(())
    plt.yticks(())
    plt.axis([-3, 3, -3, 3])
    plt.colorbar(image)
    plt.title(
        "%s\n Log-Marginal-Likelihood:%.3f"
        % (clf.kernel_, clf.log_marginal_likelihood(clf.kernel_.theta)),
        fontsize=12,
    )

plt.tight_layout()
plt.show()
```

### Step 4: Visualizing the Results

In this step, we will visualize the results obtained by fitting the model. We will plot the decision function for each datapoint on the grid and scatter plot for the input features.

### Summary

In this lab, we went through an example of Gaussian process classification (GPC) on XOR dataset using scikit-learn. We compared the results obtained by using a stationary, isotropic kernel (RBF) and a non-stationary kernel (DotProduct).
