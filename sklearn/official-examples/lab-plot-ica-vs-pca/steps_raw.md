# FastICA Tutorial

## Introduction

This lab demonstrates the use of FastICA and PCA algorithm, two popular independent component analysis techniques. Independent Component Analysis (ICA) is a method of separating multivariate signals into additive subcomponents that are maximally independent. This technique finds directions in the feature space corresponding to projections with high non-Gaussianity.

## Steps

### Step 1: Generate Sample Data

In this step, we generate sample data using a highly non-Gaussian process, 2 student T with a low number of degrees of freedom.

```python
import numpy as np

from sklearn.decomposition import PCA, FastICA

rng = np.random.RandomState(42)
S = rng.standard_t(1.5, size=(20000, 2))
S[:, 0] *= 2.0

# Mix data
A = np.array([[1, 1], [0, 2]])  # Mixing matrix

X = np.dot(S, A.T)  # Generate observations
```

### Step 2: Use PCA Algorithm

In this step, we use PCA algorithm to find orthogonal directions in the raw feature space that correspond to directions accounting for maximum variance.

```python
pca = PCA()
S_pca_ = pca.fit(X).transform(X)
```

### Step 3: Use FastICA Algorithm

In this step, we use FastICA algorithm, which finds directions in the feature space corresponding to projections with high non-Gaussianity.

```python
ica = FastICA(random_state=rng, whiten="arbitrary-variance")
S_ica_ = ica.fit(X).transform(X)  # Estimate the sources

S_ica_ /= S_ica_.std(axis=0)
```

### Step 4: Plot Results

In this step, we plot the results using matplotlib.

```python
import matplotlib.pyplot as plt

def plot_samples(S, axis_list=None):
    plt.scatter(
        S[:, 0], S[:, 1], s=2, marker="o", zorder=10, color="steelblue", alpha=0.5
    )
    if axis_list is not None:
        for axis, color, label in axis_list:
            axis /= axis.std()
            x_axis, y_axis = axis
            plt.quiver(
                (0, 0),
                (0, 0),
                x_axis,
                y_axis,
                zorder=11,
                width=0.01,
                scale=6,
                color=color,
                label=label,
            )

    plt.hlines(0, -3, 3)
    plt.vlines(0, -3, 3)
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.xlabel("x")
    plt.ylabel("y")


plt.figure()
plt.subplot(2, 2, 1)
plot_samples(S / S.std())
plt.title("True Independent Sources")

axis_list = [(pca.components_.T, "orange", "PCA"), (ica.mixing_, "red", "ICA")]
plt.subplot(2, 2, 2)
plot_samples(X / np.std(X), axis_list=axis_list)
legend = plt.legend(loc="lower right")
legend.set_zorder(100)

plt.title("Observations")

plt.subplot(2, 2, 3)
plot_samples(S_pca_ / np.std(S_pca_, axis=0))
plt.title("PCA recovered signals")

plt.subplot(2, 2, 4)
plot_samples(S_ica_ / np.std(S_ica_))
plt.title("ICA recovered signals")

plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.36)
plt.show()
```

## Summary

In this lab, we learned how to use FastICA and PCA algorithm in Python to perform independent component analysis and how to visualize the results using matplotlib.
