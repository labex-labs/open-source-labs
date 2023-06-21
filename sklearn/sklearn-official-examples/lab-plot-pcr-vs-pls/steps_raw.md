# Principal Component Regression vs Partial Least Squares Regression

## Introduction

Principal Component Regression (PCR) and Partial Least Squares Regression (PLS) are two methods used in regression analysis. PCR involves applying PCA to training data, followed by training a regressor on the transformed samples. The PCA transformation is unsupervised, meaning that no information about the targets is used. As a result, PCR may perform poorly in some datasets where the target is strongly correlated with directions that have low variance.

PLS is both a transformer and a regressor, and it is quite similar to PCR. It also applies a dimensionality reduction to the samples before applying a linear regressor to the transformed data. The main difference with PCR is that the PLS transformation is supervised. Therefore, it does not suffer from the issue mentioned above.

In this lab, we will compare PCR and PLS on a toy dataset.

## Steps

### Step 1: Create a Dataset

We start by creating a simple dataset with two features. We use the numpy library to create the dataset and the matplotlib library to plot it.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
n_samples = 500
cov = [[3, 3], [3, 4]]
X = rng.multivariate_normal(mean=[0, 0], cov=cov, size=n_samples)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="samples")
plt.gca().set(
    aspect="equal",
    title="2-dimensional dataset with principal components",
    xlabel="first feature",
    ylabel="second feature",
)
plt.legend()
plt.show()
```

### Step 2: Define the Target

For the purpose of this example, we define the target `y` such that it is strongly correlated with a direction that has a small variance. We project `X` onto the second component and add some noise to it.

```python
y = X.dot(pca.components_[1]) + rng.normal(size=n_samples) / 2

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

axes[0].scatter(X.dot(pca.components_[0]), y, alpha=0.3)
axes[0].set(xlabel="Projected data onto first PCA component", ylabel="y")
axes[1].scatter(X.dot(pca.components_[1]), y, alpha=0.3)
axes[1].set(xlabel="Projected data onto second PCA component", ylabel="y")
plt.tight_layout()
plt.show()
```

### Step 3: Create the Regressors

We create two regressors: PCR and PLS, and for our illustration purposes, we set the number of components to 1. Before feeding the data to the PCA step of PCR, we first standardize it, as recommended by good practice. The PLS estimator has built-in scaling capabilities.

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rng)

pcr = make_pipeline(StandardScaler(), PCA(n_components=1), LinearRegression())
pcr.fit(X_train, y_train)
pca = pcr.named_steps["pca"]  # retrieve the PCA step of the pipeline

pls = PLSRegression(n_components=1)
pls.fit(X_train, y_train)
```

### Step 4: Compare the Regressors

We plot the projected data onto the first component against the target for both the PCR and PLS regressors. In both cases, this projected data is what the regressors will use as training data.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
axes[0].scatter(pca.transform(X_test), y_test, alpha=0.3, label="ground truth")
axes[0].scatter(
    pca.transform(X_test), pcr.predict(X_test), alpha=0.3, label="predictions"
)
axes[0].set(
    xlabel="Projected data onto first PCA component", ylabel="y", title="PCR / PCA"
)
axes[0].legend()
axes[1].scatter(pls.transform(X_test), y_test, alpha=0.3, label="ground truth")
axes[1].scatter(
    pls.transform(X_test), pls.predict(X_test), alpha=0.3, label="predictions"
)
axes[1].set(xlabel="Projected data onto first PLS component", ylabel="y", title="PLS")
axes[1].legend()
plt.tight_layout()
plt.show()
```

We print the R-squared scores of both estimators, which further confirms that PLS is a better alternative than PCR in this case.

```python
print(f"PCR r-squared {pcr.score(X_test, y_test):.3f}")
print(f"PLS r-squared {pls.score(X_test, y_test):.3f}")
```

### Step 5: Use PCR with 2 Components

We use PCR with 2 components to compare it with PLS.

```python
pca_2 = make_pipeline(PCA(n_components=2), LinearRegression())
pca_2.fit(X_train, y_train)
print(f"PCR r-squared with 2 components {pca_2.score(X_test, y_test):.3f}")
```

## Summary

In this lab, we compared PCR and PLS on a toy dataset. We found that PLS performed better than PCR when the target is strongly correlated with directions that have low variance.
