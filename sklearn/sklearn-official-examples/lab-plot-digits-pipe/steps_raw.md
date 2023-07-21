# Building a Pipeline for Dimensionality Reduction and Classification

## Introduction

In this lab, we will build a pipeline for dimensionality reduction and classification using Principal Component Analysis (PCA) and Logistic Regression. We will use the scikit-learn library to perform unsupervised dimensionality reduction on the digits dataset using PCA. We will then use a logistic regression model for classification. We will use GridSearchCV to set the dimensionality of the PCA and find the best combination of PCA truncation and classifier regularization.

## Steps

### Step 1: Import Required Libraries

We will first import the required libraries for the implementation of the pipeline.

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
```

### Step 2: Define Pipeline Components

We will define the pipeline components including the PCA, Standard Scaler and Logistic Regression. We will set the tolerance to a large value to make the example faster.

```python
# Define a pipeline to search for the best combination of PCA truncation
# and classifier regularization.
pca = PCA()
# Define a Standard Scaler to normalize inputs
scaler = StandardScaler()

logistic = LogisticRegression(max_iter=10000, tol=0.1)

pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])
```

### Step 3: Load Dataset and Define Parameters for GridSearchCV

We will load the digits dataset and define parameters for GridSearchCV. We will set the parameter for PCA truncation and classifier regularization.

```python
X_digits, y_digits = datasets.load_digits(return_X_y=True)

param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
```

### Step 4: Perform GridSearchCV

We will perform GridSearchCV to find the best combination of PCA truncation and classifier regularization.

```python
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
```

### Step 5: Print Best Parameters and Score

We will print the best parameters and score obtained from the GridSearchCV.

```python
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)
```

### Step 6: Plot PCA Spectrum

We will plot the PCA spectrum to visualize the explained variance ratio of each principal component.

```python
pca.fit(X_digits)

fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True, figsize=(6, 6))
ax0.plot(
    np.arange(1, pca.n_components_ + 1), pca.explained_variance_ratio_, "+", linewidth=2
)
ax0.set_ylabel("PCA explained variance ratio")

ax0.axvline(
    search.best_estimator_.named_steps["pca"].n_components,
    linestyle=":",
    label="n_components chosen",
)
ax0.legend(prop=dict(size=12))
```

### Step 7: Find Best Classifier Results

For each number of components, we will find the best classifier results.

```python
results = pd.DataFrame(search.cv_results_)
components_col = "param_pca__n_components"
best_clfs = results.groupby(components_col).apply(
    lambda g: g.nlargest(1, "mean_test_score")
)
```

### Step 8: Plot Classification Accuracy

We will plot the classification accuracy for each number of components.

```python
best_clfs.plot(
    x=components_col, y="mean_test_score", yerr="std_test_score", legend=False, ax=ax1
)
ax1.set_ylabel("Classification accuracy (val)")
ax1.set_xlabel("n_components")

plt.xlim(-1, 70)

plt.tight_layout()
plt.show()
```

## Summary

In this lab, we have learned how to build a pipeline for dimensionality reduction and classification using Principal Component Analysis (PCA) and Logistic Regression. We have used the scikit-learn library to perform unsupervised dimensionality reduction on the digits dataset using PCA. We have then used a logistic regression model for classification. We have used GridSearchCV to set the dimensionality of the PCA and find the best combination of PCA truncation and classifier regularization. We have plotted the PCA spectrum and classification accuracy for each number of components.
