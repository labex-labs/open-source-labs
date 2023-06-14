# Gaussian Process Classification on Iris Dataset

## Introduction

In this lab, we will explore how to use Gaussian Process Classification (GPC) on the Iris dataset. The Iris dataset is a famous dataset that contains information about the length and width of the sepal and petal of three different species of Iris flowers. We will use scikit-learn to implement GPC, which is a probabilistic approach for classification tasks.

## Steps

### Step 1: Importing necessary libraries and dataset

First, we will import the necessary libraries and load the Iris dataset from scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = np.array(iris.target, dtype=int)
```

### Step 2: Defining the kernel function

Next, we will define the kernel function. In this example, we will use the Radial Basis Function (RBF) kernel. We will define two versions of the RBF kernel: an isotropic version and an anisotropic version.

```python
kernel = 1.0 * RBF([1.0])
gpc_rbf_isotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)

kernel = 1.0 * RBF([1.0, 1.0])
gpc_rbf_anisotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)
```

### Step 3: Creating a mesh to plot in

Now, we will create a mesh to plot in. The mesh will be used to plot the predicted probabilities for each point on the mesh. We will also define the step size for the mesh.

```python
h = 0.02  # step size in the mesh

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
```

### Step 4: Plotting the predicted probabilities

Now, we will plot the predicted probabilities for each point on the mesh. We will create two subplots: one for the isotropic RBF kernel and one for the anisotropic RBF kernel. We will use the `predict_proba` method to get the predicted probabilities for each point on the mesh. We will then plot the predicted probabilities as a color plot on the mesh. We will also plot the training points for each species of Iris flower.

```python
titles = ["Isotropic RBF", "Anisotropic RBF"]
plt.figure(figsize=(10, 5))
for i, clf in enumerate((gpc_rbf_isotropic, gpc_rbf_anisotropic)):
    # Plot the predicted probabilities. For that, we will assign a color to
    # each point in the mesh [x_min, m_max]x[y_min, y_max].
    plt.subplot(1, 2, i + 1)

    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape((xx.shape[0], xx.shape[1], 3))
    plt.imshow(Z, extent=(x_min, x_max, y_min, y_max), origin="lower")

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=np.array(["r", "g", "b"])[y], edgecolors=(0, 0, 0))
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(
        "%s, LML: %.3f" % (titles[i], clf.log_marginal_likelihood(clf.kernel_.theta))
    )

plt.tight_layout()
plt.show()
```

## Summary

In this lab, we explored how to use Gaussian Process Classification (GPC) on the Iris dataset using scikit-learn. We defined two versions of the Radial Basis Function (RBF) kernel, an isotropic version, and an anisotropic version. We then created a mesh to plot the predicted probabilities for each point on the mesh and plotted the predicted probabilities as a color plot on the mesh. Finally, we plotted the training points for each species of Iris flower.
