# Gradient Boosting Regression

## Introduction

In this lab, we will use Gradient Boosting to build a predictive model for diabetes regression task. We will train the model on the diabetes dataset and obtain the results from `sklearn.ensemble.GradientBoostingRegressor` with least squares loss and 500 regression trees of depth 4.

## Steps

### Step 1: Load the Data

First, we will load the diabetes dataset.

```python
diabetes = datasets.load_diabetes()
X, y = diabetes.data, diabetes.target
```

### Step 2: Data Preprocessing

Next, we will split our dataset to use 90% for training and leave the rest for testing. We will also set the regression model parameters.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=13)

params = {
    "n_estimators": 500,
    "max_depth": 4,
    "min_samples_split": 5,
    "learning_rate": 0.01,
    "loss": "squared_error",
}
```

### Step 3: Fit Regression Model

Now we will initiate the gradient boosting regressors and fit it with our training data. Let's also look and the mean squared error on the test data.

```python
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

mse = mean_squared_error(y_test, reg.predict(X_test))
print("The mean squared error (MSE) on test set: {:.4f}".format(mse))
```

### Step 4: Plot Training Deviance

Finally, we will visualize the results. To do that we will first compute the test set deviance and then plot it against boosting iterations.

```python
test_score = np.zeros((params["n_estimators"],), dtype=np.float64)
for i, y_pred in enumerate(reg.staged_predict(X_test)):
    test_score[i] = mean_squared_error(y_test, y_pred)

fig = plt.figure(figsize=(6, 6))
plt.subplot(1, 1, 1)
plt.title("Deviance")
plt.plot(
    np.arange(params["n_estimators"]) + 1,
    reg.train_score_,
    "b-",
    label="Training Set Deviance",
)
plt.plot(
    np.arange(params["n_estimators"]) + 1, test_score, "r-", label="Test Set Deviance"
)
plt.legend(loc="upper right")
plt.xlabel("Boosting Iterations")
plt.ylabel("Deviance")
fig.tight_layout()
plt.show()
```

### Step 5: Plot Feature Importance

For this example, we will use impurity-based feature importances to identify the most predictive features.

```python
feature_importance = reg.feature_importances_
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + 0.5
fig = plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.barh(pos, feature_importance[sorted_idx], align="center")
plt.yticks(pos, np.array(diabetes.feature_names)[sorted_idx])
plt.title("Feature Importance (MDI)")
```

### Step 6: Plot Permutation Importance

We will use the permutation method to identify the most predictive features.

```python
result = permutation_importance(
    reg, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
sorted_idx = result.importances_mean.argsort()
plt.subplot(1, 2, 2)
plt.boxplot(
    result.importances[sorted_idx].T,
    vert=False,
    labels=np.array(diabetes.feature_names)[sorted_idx],
)
plt.title("Permutation Importance (test set)")
fig.tight_layout()
plt.show()
```

## Summary

In this lab, we used Gradient Boosting to build a predictive model for diabetes regression task. We loaded the data, preprocessed it, fit the regression model, and visualized the results by plotting the training deviance, feature importance, and permutation importance.
