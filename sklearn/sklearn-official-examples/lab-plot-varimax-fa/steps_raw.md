# Factor Analysis

## Introduction

Factor Analysis is a statistical method used to uncover patterns in data. It is often used to identify latent variables that explain correlations among observed variables. In this lab, we will use the Iris dataset to illustrate how Factor Analysis can be used to reveal the underlying structure of the data.

## Steps

### Step 1: Load the Iris dataset and plot covariance of features

We will begin by loading the Iris dataset and plotting the covariance of the features to see how they are correlated.

```python
import matplotlib.pyplot as plt
import numpy as np

from sklearn.decomposition import FactorAnalysis, PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Load Iris data
data = load_iris()
X = StandardScaler().fit_transform(data["data"])
feature_names = data["feature_names"]

# Plot covariance of Iris features
ax = plt.axes()

im = ax.imshow(np.corrcoef(X.T), cmap="RdBu_r", vmin=-1, vmax=1)

ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(list(feature_names), rotation=90)
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(list(feature_names))

plt.colorbar(im).ax.set_ylabel("$r$", rotation=0)
ax.set_title("Iris feature correlation matrix")
plt.tight_layout()
```

### Step 2: Run Factor Analysis with Varimax Rotation

We will now run Factor Analysis on the Iris dataset with Varimax rotation to uncover the underlying structure of the data. We will compare the results with PCA and Unrotated FA.

```python
# Run factor analysis with Varimax rotation
n_comps = 2

methods = [
    ("PCA", PCA()),
    ("Unrotated FA", FactorAnalysis()),
    ("Varimax FA", FactorAnalysis(rotation="varimax")),
]
fig, axes = plt.subplots(ncols=len(methods), figsize=(10, 8), sharey=True)

for ax, (method, fa) in zip(axes, methods):
    fa.set_params(n_components=n_comps)
    fa.fit(X)

    components = fa.components_.T
    print("\n\n %s :\n" % method)
    print(components)

    vmax = np.abs(components).max()
    ax.imshow(components, cmap="RdBu_r", vmax=vmax, vmin=-vmax)
    ax.set_yticks(np.arange(len(feature_names)))
    ax.set_yticklabels(feature_names)
    ax.set_title(str(method))
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Comp. 1", "Comp. 2"])
fig.suptitle("Factors")
plt.tight_layout()
plt.show()
```

### Step 3: Analyze the Results

We will now analyze the results of the Factor Analysis to see how the underlying structure of the Iris dataset is revealed.

### Step 4: Interpret the Results

We will now interpret the results of the Factor Analysis to gain insight into the underlying structure of the Iris dataset.

## Summary

In this lab, we used Factor Analysis with Varimax rotation to uncover the underlying structure of the Iris dataset. We compared the results with PCA and Unrotated FA and analyzed the results to gain insight into the underlying structure of the data.
