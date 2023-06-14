# Plotting Predictions with Cross-Validation

## Introduction

In this lab, we will learn how to use cross-validation to visualize model predictions and errors using the `cross_val_predict` and `PredictionErrorDisplay` functions in scikit-learn. We will load the diabetes dataset, create an instance of a linear regression model, and use cross-validation to obtain an array of predictions. We will then use `PredictionErrorDisplay` to plot the actual versus predicted values, as well as the residuals versus predicted values.

## Steps

### Step 1: Load and Prepare Data

First, we will load the diabetes dataset and prepare it for modeling. We will use `load_diabetes` function from scikit-learn to load the dataset into two arrays, `X` and `y`.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)
```

### Step 2: Create a Linear Regression Model

Next, we will create an instance of a linear regression model using the `LinearRegression` class from scikit-learn.

```python
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
```

### Step 3: Generate Cross-Validated Predictions

We will use `cross_val_predict` function from scikit-learn to generate cross-validated predictions.

```python
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(lr, X, y, cv=10)
```

### Step 4: Visualize Prediction Errors

We will use `PredictionErrorDisplay` from scikit-learn to visualize the prediction errors. We will plot the actual versus predicted values, as well as the residuals versus predicted values.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import PredictionErrorDisplay

fig, axs = plt.subplots(ncols=2, figsize=(8, 4))
PredictionErrorDisplay.from_predictions(
    y,
    y_pred=y_pred,
    kind="actual_vs_predicted",
    subsample=100,
    ax=axs[0],
    random_state=0,
)
axs[0].set_title("Actual vs. Predicted values")
PredictionErrorDisplay.from_predictions(
    y,
    y_pred=y_pred,
    kind="residual_vs_predicted",
    subsample=100,
    ax=axs[1],
    random_state=0,
)
axs[1].set_title("Residuals vs. Predicted Values")
fig.suptitle("Plotting cross-validated predictions")
plt.tight_layout()
plt.show()
```

### Step 5: Interpret Results

From the visualizations, we can see that the actual versus predicted plot shows a relatively linear relationship with some variation. The residuals versus predicted values plot shows a relatively random pattern with no clear trend, indicating that the linear regression model may be a good fit for the data. However, it is important to note that we used `cross_val_predict` for visualization purposes only. It would be problematic to quantitatively assess the model performance by computing a single performance metric from the concatenated predictions returned by `cross_val_predict` when the different CV folds vary by size and distributions. It is recommended to compute per-fold performance metrics using `cross_val_score` or `cross_validate` instead.

## Summary

In this lab, we learned how to use cross-validation to visualize model predictions and errors using the `cross_val_predict` and `PredictionErrorDisplay` functions in scikit-learn. We loaded the diabetes dataset, created an instance of a linear regression model, and used cross-validation to obtain an array of predictions. We then used `PredictionErrorDisplay` to plot the actual versus predicted values, as well as the residuals versus predicted values. Finally, we interpreted the results and discussed the importance of using per-fold performance metrics for model evaluation.
