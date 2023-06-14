# Robust Linear Model Estimation

## Introduction

In this lab, we will demonstrate how to robustly fit a linear model to faulty data using the RANSAC algorithm in scikit-learn. The ordinary linear regressor is sensitive to outliers, and the fitted line can easily be skewed away from the true underlying relationship of data. The RANSAC regressor automatically splits the data into inliers and outliers, and the fitted line is determined only by the identified inliers. We will use the make_regression dataset from scikit-learn to generate random data with outliers, and then fit both a linear model and a RANSAC regressor to the data.

## Steps

### Step 1: Import libraries and generate data

We will import the necessary libraries, generate random data using the make_regression dataset, and add outliers to the data.

```python
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

# Generate data
n_samples = 1000
n_outliers = 50

X, y, coef = datasets.make_regression(
    n_samples=n_samples,
    n_features=1,
    n_informative=1,
    noise=10,
    coef=True,
    random_state=0,
)

# Add outlier data
np.random.seed(0)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)
```

### Step 2: Fit a linear model

We will fit a linear model to the data using scikit-learn's LinearRegression class.

```python
# Fit line using all data
lr = linear_model.LinearRegression()
lr.fit(X, y)
```

### Step 3: Fit a RANSAC regressor

We will fit a RANSAC regressor to the data using scikit-learn's RANSACRegressor class.

```python
# Robustly fit linear model with RANSAC algorithm
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
```

### Step 4: Predict data of estimated models

We will predict the data of the linear model and the RANSAC regressor and compare their results.

```python
# Predict data of estimated models
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)
```

### Step 5: Compare estimated coefficients

We will compare the estimated coefficients of the true model, the linear model, and the RANSAC regressor.

```python
# Compare estimated coefficients
print("Estimated coefficients (true, linear regression, RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)
```

### Step 6: Visualize the results

We will plot the data and the fitted lines of the linear model and the RANSAC regressor.

```python
# Visualize the results
lw = 2
plt.scatter(
    X[inlier_mask], y[inlier_mask], color="yellowgreen", marker=".", label="Inliers"
)
plt.scatter(
    X[outlier_mask], y[outlier_mask], color="gold", marker=".", label="Outliers"
)
plt.plot(line_X, line_y, color="navy", linewidth=lw, label="Linear regressor")
plt.plot(
    line_X,
    line_y_ransac,
    color="cornflowerblue",
    linewidth=lw,
    label="RANSAC regressor",
)
plt.legend(loc="lower right")
plt.xlabel("Input")
plt.ylabel("Response")
plt.show()
```

## Summary

In this lab, we demonstrated how to robustly fit a linear model to faulty data using the RANSAC algorithm in scikit-learn. We generated random data using the make_regression dataset, added outliers to the data, fit both a linear model and a RANSAC regressor to the data, predicted the data of the two models, compared their estimated coefficients, and visualized the results. The RANSAC regressor automatically splits the data into inliers and outliers, and the fitted line is determined only by the identified inliers, making it a more robust method for fitting models to data with outliers.
