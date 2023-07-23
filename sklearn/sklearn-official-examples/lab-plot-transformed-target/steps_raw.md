# Scikit-learn TransformedTargetRegressor

## Introduction

In this lab, we will learn how to use the TransformedTargetRegressor from the scikit-learn library. We will apply it to two different datasets to observe the benefits of transforming the target values before training a linear regression model. We will use synthetic data and the Ames housing data set to illustrate the impact of transforming the target values.

## Steps

### Step 1: Import necessary libraries and load synthetic data

We start by importing necessary libraries and loading synthetic data. We generate a synthetic random regression dataset and modify the targets by translating all targets such that all entries are non-negative and applying an exponential function to obtain non-linear targets which cannot be fitted using a simple linear model. We then use a logarithmic (np.log1p) and an exponential function (np.expm1) to transform the targets before training a linear regression model and using it for prediction.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import median_absolute_error, r2_score, PredictionErrorDisplay

# Generate synthetic data
X, y = make_regression(n_samples=10_000, noise=100, random_state=0)

# Modify the targets
y = np.expm1((y + abs(y.min())) / 200)
y_trans = np.log1p(y)
```

### Step 2: Plot the target distributions

We plot the probability density functions of the target before and after applying the logarithmic functions.

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_xlim([0, 2000])
ax0.set_ylabel("Probability")
ax0.set_xlabel("Target")
ax0.set_title("Target distribution")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("Probability")
ax1.set_xlabel("Target")
ax1.set_title("Transformed target distribution")

f.suptitle("Synthetic data", y=1.05)
plt.tight_layout()
```

### Step 3: Train and evaluate a linear regression model on the original targets

We train and evaluate a linear regression model on the original targets. Due to the non-linearity, the model trained will not be precise during prediction.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("Linear Regression on original targets:")
for key, val in score.items():
    print(f"{key}: {val}")
```

### Step 4: Train and evaluate a linear regression model on the transformed targets

We train and evaluate a linear regression model on the transformed targets using TransformedTargetRegressor. The logarithmic function linearizes the targets, allowing better prediction even with a similar linear model as reported by the median absolute error (MedAE).

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(), func=np.log1p, inverse_func=np.expm1
).fit(X_train, y_train)
y_pred_ridge_with_trans_target = ridge_cv_with_trans_target.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge_with_trans_target):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge_with_trans_target):.3f}",
}

print("\nLinear Regression on transformed targets:")
for key, val in score.items():
    print(f"{key}: {val}")
```

### Step 5: Plot actual vs predicted values for both models

We plot actual vs predicted values for both models and add the score in the legend of each axis.

```python
f, (ax0, ax1) = plt.subplots(1, 2, sharey=True)

PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge,
    kind="actual_vs_predicted",
    ax=ax0,
    scatter_kwargs={"alpha": 0.5},
)
PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge_with_trans_target,
    kind="actual_vs_predicted",
    ax=ax1,
    scatter_kwargs={"alpha": 0.5},
)

for ax, y_pred in zip([ax0, ax1], [y_pred_ridge, y_pred_ridge_with_trans_target]):
    for name, score in score.items():
        ax.plot([], [], " ", label=f"{name}={score}")
    ax.legend(loc="upper left")

ax0.set_title("Ridge regression \n without target transformation")
ax1.set_title("Ridge regression \n with target transformation")
f.suptitle("Synthetic data", y=1.05)
plt.tight_layout()
```

### Step 6: Load and preprocess Ames housing data

We load the Ames housing data set and preprocess it by keeping only numeric columns and removing columns with NaN or Inf values. The target to be predicted is the selling price of each house.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import quantile_transform

ames = fetch_openml(name="house_prices", as_frame=True, parser="pandas")

# Keep only numeric columns
X = ames.data.select_dtypes(np.number)

# Remove columns with NaN or Inf values
X = X.drop(columns=["LotFrontage", "GarageYrBlt", "MasVnrArea"])

# Let the price be in k$
y = ames.target / 1000
y_trans = quantile_transform(
    y.to_frame(), n_quantiles=900, output_distribution="normal", copy=True
).squeeze()
```

### Step 7: Plot target distributions for Ames housing data

We plot the probability density functions of the target before and after applying the QuantileTransformer.

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_ylabel("Probability")
ax0.set_xlabel("Target")
ax0.set_title("Target distribution")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("Probability")
ax1.set_xlabel("Target")
ax1.set_title("Transformed target distribution")

f.suptitle("Ames housing data: selling price", y=1.05)
plt.tight_layout()
```

### Step 8: Train and evaluate a linear regression model on the original targets for Ames housing data

We train and evaluate a linear regression model on the original targets for Ames housing data.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("\nLinear Regression on original targets:")
for key, val in score.items():
    print(f"{key}: {val}")
```

### Step 9: Train and evaluate a linear regression model on the transformed targets for Ames housing data

We train and evaluate a linear regression model on the transformed targets using TransformedTargetRegressor for Ames housing data.

```python
ridge_cv_with_trans_target = TransformedTargetRegressor(
    regressor=RidgeCV(),
    transformer=QuantileTransformer(n_quantiles=900, output_distribution="normal"),
).fit(X_train, y_train)
y_pred_ridge_with_trans_target = ridge_cv_with_trans_target.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge_with_trans_target):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge_with_trans_target):.3f}",
}

print("\nLinear Regression on transformed targets:")
for key, val in score.items():
    print(f"{key}: {val}")
```

### Step 10: Plot actual vs predicted values and residuals vs predicted values for both models

We plot actual vs predicted values and residuals vs predicted values for both models and add the score in the legend of each axis.

```python
f, (ax0, ax1) = plt.subplots(2, 2, sharey="row", figsize=(6.5, 8))

PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge,
    kind="actual_vs_predicted",
    ax=ax0[0],
    scatter_kwargs={"alpha": 0.5},
)
PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge_with_trans_target,
    kind="actual_vs_predicted",
    ax=ax0[1],
    scatter_kwargs={"alpha": 0.5},
)

for ax, y_pred in zip([ax0[0], ax0[1]], [y_pred_ridge, y_pred_ridge_with_trans_target]):
    for name, score in score.items():
        ax.plot([], [], " ", label=f"{name}={score}")
    ax.legend(loc="upper left")

ax0[0].set_title("Ridge regression \n without target transformation")
ax0[1].set_title("Ridge regression \n with target transformation")

PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge,
    kind="residual_vs_predicted",
    ax=ax1[0],
    scatter_kwargs={"alpha": 0.5},
)
PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge_with_trans_target,
    kind="residual_vs_predicted",
    ax=ax1[1],
    scatter_kwargs={"alpha": 0.5},
)
ax1[0].set_title("Ridge regression \n without target transformation")
ax1[1].set_title("Ridge regression \n with target transformation")

f.suptitle("Ames housing data: selling price", y=1.05)
plt.tight_layout()
plt.show()
```

## Summary

In this lab, we learned how to use the TransformedTargetRegressor from the scikit-learn library. We applied it to two different datasets to observe the benefits of transforming the target values before training a linear regression model. We used synthetic data and the Ames housing data set to illustrate the impact of transforming the target values. We observed that the logarithmic function linearized the targets, allowing better prediction even with a similar linear model as reported by the median absolute error (MedAE). We also observed that the effect of the transformer was weaker for the Ames housing data set, but still resulted in an increase in R2 and a large decrease of the MedAE.
