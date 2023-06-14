# Support Vector Regression

## Introduction

In this lab, we will use Support Vector Regression (SVR) to fit a model to a 1D dataset using linear, polynomial, and Radial Basis Function (RBF) kernels. We will use Python's scikit-learn library to perform the SVR.

## Steps

### Step 1: Generate Sample Data

First, we generate a sample dataset consisting of 40 random values between 0 and 5. We then compute the sine function of each value and add some noise to every 5th value.

```python
import numpy as np

# Generate sample data
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))
```

### Step 2: Fit Regression Model

Next, we fit an SVR model to our sample dataset using a linear, polynomial, and RBF kernel. We set the hyperparameters for each model and train them on our sample dataset.

```python
from sklearn.svm import SVR

# Fit regression model
svr_rbf = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr_lin = SVR(kernel="linear", C=100, gamma="auto")
svr_poly = SVR(kernel="poly", C=100, gamma="auto", degree=3, epsilon=0.1, coef0=1)

svrs = [svr_rbf, svr_lin, svr_poly]

for svr in svrs:
    svr.fit(X, y)
```

### Step 3: Visualize Results

Finally, we visualize the results of our SVR models by plotting them against the sample dataset. We also plot the support vectors and other training data.

```python
import matplotlib.pyplot as plt

# Look at the results
lw = 2

kernel_label = ["RBF", "Linear", "Polynomial"]
model_color = ["m", "c", "g"]

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 10), sharey=True)

for ix, svr in enumerate(svrs):
    axes[ix].plot(
        X,
        svr.predict(X),
        color=model_color[ix],
        lw=lw,
        label="{} model".format(kernel_label[ix]),
    )
    axes[ix].scatter(
        X[svr.support_],
        y[svr.support_],
        facecolor="none",
        edgecolor=model_color[ix],
        s=50,
        label="{} support vectors".format(kernel_label[ix]),
    )
    axes[ix].scatter(
        X[np.setdiff1d(np.arange(len(X)), svr.support_)],
        y[np.setdiff1d(np.arange(len(X)), svr.support_)],
        facecolor="none",
        edgecolor="k",
        s=50,
        label="other training data",
    )
    axes[ix].legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.1),
        ncol=1,
        fancybox=True,
        shadow=True,
    )

fig.text(0.5, 0.04, "data", ha="center", va="center")
fig.text(0.06, 0.5, "target", ha="center", va="center", rotation="vertical")
fig.suptitle("Support Vector Regression", fontsize=14)
plt.show()
```

## Summary

In this lab, we learned how to use Support Vector Regression (SVR) to fit a model to a 1D dataset using linear, polynomial, and RBF kernels. We generated sample data, fit regression models using scikit-learn, and visualized the results.
