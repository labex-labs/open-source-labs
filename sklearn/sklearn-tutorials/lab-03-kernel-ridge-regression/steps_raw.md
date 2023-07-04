# Kernel Ridge Regression

## Introduction

In this lab, we will learn about Kernel Ridge Regression (KRR) and its implementation using the scikit-learn library in Python. KRR combines ridge regression with the kernel trick to learn a linear function in the space induced by the kernel. It is a non-linear regression method that can handle non-linear relationships between input and output variables.

## Steps

### Step 1: Import Libraries

First, let's import the required libraries for this lab.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.kernel_ridge import KernelRidge
```

### Step 2: Generate Synthetic Data

Next, let's generate some synthetic data to work with. We will create a sinusoidal target function and add some random noise to it.

```python
# Generate input data
np.random.seed(0)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel()
y += 0.5 * (0.5 - np.random.rand(y.size))
```

### Step 3: Fit Kernel Ridge Regression Model

Now, let's fit a Kernel Ridge Regression model to the data. We will use the RBF (Radial Basis Function) kernel, which is commonly used for non-linear regression.

```python
# Fit Kernel Ridge Regression model
alpha = 1.0  # Regularization parameter
gamma = 0.1  # Kernel coefficient for RBF kernel
krr = KernelRidge(alpha=alpha, kernel='rbf', gamma=gamma)
krr.fit(X, y)
```

### Step 4: Visualize the Predicted Function

Once the model is trained, let's visualize the predicted function along with the original data points.

```python
# Generate test data points
X_test = np.linspace(0, 5, 100)[:, None]

# Predict the target values
y_pred = krr.predict(X_test)

# Visualize the data and the predicted function
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_test, y_pred, color='red', label='Predicted Function')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```

### Step 5: Optimize Hyperparameters

In the previous step, we used default hyperparameter values for alpha and gamma. To improve the model's performance, we can optimize these hyperparameters using grid search.

```python
from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid = {'alpha': [1e-3, 1e-2, 1e-1, 1, 10],
              'gamma': [1e-3, 1e-2, 1e-1, 1, 10]}

# Perform grid search
grid_search = GridSearchCV(krr, param_grid, cv=5)
grid_search.fit(X, y)

# Get the best hyperparameters
best_alpha = grid_search.best_params_['alpha']
best_gamma = grid_search.best_params_['gamma']
best_krr = grid_search.best_estimator_

print("Best alpha:", best_alpha)
print("Best gamma:", best_gamma)
```

### Step 6: Visualize the Optimized Predicted Function

Finally, let's visualize the predicted function using the optimized hyperparameters.

```python
# Predict the target values using the optimized model
y_pred_opt = best_krr.predict(X_test)

# Visualize the data and the optimized predicted function
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_test, y_pred_opt, color='green', label='Optimized Predicted Function')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```

## Summary

In this lab, we learned about Kernel Ridge Regression (KRR) and how to implement it using the scikit-learn library in Python. We generated synthetic data, fit a KRR model to the data, visualized the predicted function, and optimized the hyperparameters using grid search. KRR is a powerful non-linear regression method that can handle complex relationships between variables.
