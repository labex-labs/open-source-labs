# Robust Linear Estimator Fitting

## Introduction

In this lab, we will learn how to use Python's scikit-learn library to perform robust linear estimator fitting. We will fit a sine function with a polynomial of order 3 for values close to zero and demo the robust fitting in different situations. We will use the median absolute deviation to non-corrupt new data to judge the quality of the prediction.

## Steps

### Step 1: Import Required Libraries and Generate Data

We first need to import the necessary libraries and generate data for our fitting. We will generate a sine function with some noise and corrupt the data by introducing errors in both X and y.

```python
from matplotlib import pyplot as plt
import numpy as np

from sklearn.linear_model import (
    LinearRegression,
    TheilSenRegressor,
    RANSACRegressor,
    HuberRegressor,
)
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

np.random.seed(42)

X = np.random.normal(size=400)
y = np.sin(X)
# Make sure that it X is 2D
X = X[:, np.newaxis]

X_test = np.random.normal(size=200)
y_test = np.sin(X_test)
X_test = X_test[:, np.newaxis]

y_errors = y.copy()
y_errors[::3] = 3

X_errors = X.copy()
X_errors[::3] = 3

y_errors_large = y.copy()
y_errors_large[::3] = 10

X_errors_large = X.copy()
X_errors_large[::3] = 10
```

### Step 2: Fit a Sine Function with a Polynomial of Order 3

We will fit a sine function with a polynomial of order 3 for values close to zero.

```python
x_plot = np.linspace(X.min(), X.max())
```

### Step 3: Demo Robust Fitting in Different Situations

We will now demo the robust fitting in different situations using four different estimators: OLS, Theil-Sen, RANSAC, and HuberRegressor.

```python
estimators = [
    ("OLS", LinearRegression()),
    ("Theil-Sen", TheilSenRegressor(random_state=42)),
    ("RANSAC", RANSACRegressor(random_state=42)),
    ("HuberRegressor", HuberRegressor()),
]
colors = {
    "OLS": "turquoise",
    "Theil-Sen": "gold",
    "RANSAC": "lightgreen",
    "HuberRegressor": "black",
}
linestyle = {"OLS": "-", "Theil-Sen": "-.", "RANSAC": "--", "HuberRegressor": "--"}
lw = 3
```

### Step 4: Plot the Results

We will now plot the results for each of the different situations.

```python
for title, this_X, this_y in [
    ("Modeling Errors Only", X, y),
    ("Corrupt X, Small Deviants", X_errors, y),
    ("Corrupt y, Small Deviants", X, y_errors),
    ("Corrupt X, Large Deviants", X_errors_large, y),
    ("Corrupt y, Large Deviants", X, y_errors_large),
]:
    plt.figure(figsize=(5, 4))
    plt.plot(this_X[:, 0], this_y, "b+")

    for name, estimator in estimators:
        model = make_pipeline(PolynomialFeatures(3), estimator)
        model.fit(this_X, this_y)
        mse = mean_squared_error(model.predict(X_test), y_test)
        y_plot = model.predict(x_plot[:, np.newaxis])
        plt.plot(
            x_plot,
            y_plot,
            color=colors[name],
            linestyle=linestyle[name],
            linewidth=lw,
            label="%s: error = %.3f" % (name, mse),
        )

    legend_title = "Error of Mean\nAbsolute Deviation\nto Non-corrupt Data"
    legend = plt.legend(
        loc="upper right", frameon=False, title=legend_title, prop=dict(size="x-small")
    )
    plt.xlim(-4, 10.2)
    plt.ylim(-2, 10.2)
    plt.title(title)
plt.show()
```

## Summary

In this lab, we learned how to use Python's scikit-learn library to perform robust linear estimator fitting. We fit a sine function with a polynomial of order 3 for values close to zero and demoed the robust fitting in different situations. We used the median absolute deviation to non-corrupt new data to judge the quality of the prediction.
