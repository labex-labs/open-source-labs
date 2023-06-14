# Scikit-learn Tutorial: Weighted Samples

## Introduction

In this tutorial, we will learn how to plot a decision function of a weighted dataset using scikit-learn. We will also learn how to assign different weights to the samples in the dataset to show how the weights affect the decision function.

## Steps

### Step 1: Import Required Libraries

We start by importing the necessary libraries for our project.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
```

### Step 2: Create a Weighted Dataset

We create a weighted dataset using the numpy library. We generate 20 points with random values and assign a bigger weight to the last 10 samples.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
sample_weight = 100 * np.abs(np.random.randn(20))
sample_weight[:10] *= 10
```

### Step 3: Plot the Weighted Dataset

We plot the weighted dataset using the matplotlib library. The size of the points is proportional to its weight.

```python
xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))
fig, ax = plt.subplots()
ax.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    s=sample_weight,
    alpha=0.9,
    cmap=plt.cm.bone,
    edgecolor="black",
)
```

### Step 4: Fit the Unweighted Model

We fit an unweighted model using the SGDClassifier algorithm from the scikit-learn library. We then plot the decision function of the unweighted model.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
no_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["solid"])
```

### Step 5: Fit the Weighted Model

We fit a weighted model using the same algorithm as in Step 4, but this time we pass the sample_weight argument to the fit method. We then plot the decision function of the weighted model.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
samples_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["dashed"])
```

### Step 6: Add Legend and Display the Plot

We add a legend to the plot to differentiate between the unweighted and weighted models. We then display the plot.

```python
no_weights_handles, _ = no_weights.legend_elements()
weights_handles, _ = samples_weights.legend_elements()
ax.legend(
    [no_weights_handles[0], weights_handles[0]],
    ["no weights", "with weights"],
    loc="lower left",
)

ax.set(xticks=(), yticks=())
plt.show()
```

## Summary

In this tutorial, we learned how to plot a decision function of a weighted dataset using scikit-learn. We also learned how to assign different weights to the samples in the dataset to show how the weights affect the decision function.
