# Theil-Sen Regression Tutorial

## Introduction

In this tutorial, we will learn about Theil-Sen Regression and its implementation using Python scikit-learn library. We will also see how it differs from Ordinary Least Squares (OLS) and Robust Random Sample Consensus (RANSAC) regression.

## Steps

### Step 1: Import Libraries and Generate Dataset

First, let's import the necessary libraries and generate a synthetic dataset for the regression analysis.

```python
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, TheilSenRegressor
from sklearn.linear_model import RANSACRegressor

np.random.seed(0)
n_samples = 200
x = np.random.randn(n_samples)
w = 3.0
c = 2.0
noise = 0.1 * np.random.randn(n_samples)
y = w * x + c + noise
X = x[:, np.newaxis]
```

### Step 2: Plot the Data

Now, let's plot the generated dataset.

```python
plt.scatter(x, y, color="indigo", marker="x", s=40)
plt.axis("tight")
_ = plt.title("Original Data")
```

### Step 3: Fit Linear Regression Models

Next, we will fit three linear regression models using OLS, Theil-Sen, and RANSAC methods.

```python
estimators = [
    ("OLS", LinearRegression()),
    ("Theil-Sen", TheilSenRegressor(random_state=42)),
    ("RANSAC", RANSACRegressor(random_state=42)),
]
colors = {"OLS": "turquoise", "Theil-Sen": "gold", "RANSAC": "lightgreen"}
lw = 2

line_x = np.array([-3, 3])
for name, estimator in estimators:
    t0 = time.time()
    estimator.fit(X, y)
    elapsed_time = time.time() - t0
    y_pred = estimator.predict(line_x.reshape(2, 1))
    plt.plot(
        line_x,
        y_pred,
        color=colors[name],
        linewidth=lw,
        label="%s (fit time: %.2fs)" % (name, elapsed_time),
    )
```

### Step 4: Plot the Regression Lines

Finally, we will plot the regression lines of the fitted models.

```python
plt.axis("tight")
plt.legend(loc="upper left")
_ = plt.title("Regression Lines")
```

## Summary

In this tutorial, we learned about Theil-Sen Regression and its implementation using Python scikit-learn library. We also saw how it differs from Ordinary Least Squares (OLS) and Robust Random Sample Consensus (RANSAC) regression. By following the above steps, we were able to generate a synthetic dataset, fit linear regression models, and plot the regression lines.
