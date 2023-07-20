# Dimensionality Reduction with Pipeline and GridSearchCV

## Introduction

This lab demonstrates the use of `Pipeline` and `GridSearchCV` in scikit-learn to optimize over different classes of estimators in a single CV run. We will be using a support vector classifier to predict hand-written digits from the popular MNIST dataset.

## Steps

### Step 1: Import necessary libraries and load data

We will begin by importing the necessary libraries and load the digits dataset from scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.decomposition import PCA, NMF
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.preprocessing import MinMaxScaler

X, y = load_digits(return_X_y=True)
```

### Step 2: Create a pipeline and define parameter grid

We will create a pipeline that does dimensionality reduction followed by prediction with a support vector classifier. We will use unsupervised PCA and NMF dimensionality reductions, along with univariate feature selection during the grid search.

```python
pipe = Pipeline(
    [
        ("scaling", MinMaxScaler()),
        # the reduce_dim stage is populated by the param_grid
        ("reduce_dim", "passthrough"),
        ("classify", LinearSVC(dual=False, max_iter=10000)),
    ]
)

N_FEATURES_OPTIONS = [2, 4, 8]
C_OPTIONS = [1, 10, 100, 1000]
param_grid = [
    {
        "reduce_dim": [PCA(iterated_power=7), NMF(max_iter=1_000)],
        "reduce_dim__n_components": N_FEATURES_OPTIONS,
        "classify__C": C_OPTIONS,
    },
    {
        "reduce_dim": [SelectKBest(mutual_info_classif)],
        "reduce_dim__k": N_FEATURES_OPTIONS,
        "classify__C": C_OPTIONS,
    },
]
reducer_labels = ["PCA", "NMF", "KBest(mutual_info_classif)"]
```

### Step 3: Create a GridSearchCV object and fit data

We will create a `GridSearchCV` object using the pipeline and parameter grid we defined in the previous step. We will then fit the data to the object.

```python
grid = GridSearchCV(pipe, n_jobs=1, param_grid=param_grid)
grid.fit(X, y)
```

### Step 4: Plot results

We will plot the results of the `GridSearchCV` using a bar chart. This will allow us to compare the accuracy of different feature reduction techniques.

```python
import pandas as pd

mean_scores = np.array(grid.cv_results_["mean_test_score"])
# scores are in the order of param_grid iteration, which is alphabetical
mean_scores = mean_scores.reshape(len(C_OPTIONS), -1, len(N_FEATURES_OPTIONS))
# select score for best C
mean_scores = mean_scores.max(axis=0)
# create a dataframe to ease plotting
mean_scores = pd.DataFrame(
    mean_scores.T, index=N_FEATURES_OPTIONS, columns=reducer_labels
)

ax = mean_scores.plot.bar()
ax.set_title("Comparing feature reduction techniques")
ax.set_xlabel("Reduced number of features")
ax.set_ylabel("Digit classification accuracy")
ax.set_ylim((0, 1))
ax.legend(loc="upper left")

plt.show()
```

### Step 5: Caching transformers within a Pipeline

We will now demonstrate how to store the state of a specific transformer, since it could be used again. Using a pipeline in `GridSearchCV` triggers such situations. Therefore, we use the argument `memory` to enable caching.

```python
from joblib import Memory
from shutil import rmtree

# Create a temporary folder to store the transformers of the pipeline
location = "cachedir"
memory = Memory(location=location, verbose=10)
cached_pipe = Pipeline(
    [("reduce_dim", PCA()), ("classify", LinearSVC(dual=False, max_iter=10000))],
    memory=memory,
)

# This time, a cached pipeline will be used within the grid search

# Delete the temporary cache before exiting
memory.clear(warn=False)
rmtree(location)
```

### Summary

In this lab, we used `Pipeline` and `GridSearchCV` in scikit-learn to optimize over different classes of estimators in a single CV run. We also demonstrated how to store the state of a specific transformer using the `memory` argument to enable caching. This can be particularly useful when fitting a transformer is costly.
