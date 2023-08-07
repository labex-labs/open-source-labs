# Fit Kernel Ridge Regression Model

Now, let's fit a Kernel Ridge Regression model to the data. We will use the RBF (Radial Basis Function) kernel, which is commonly used for non-linear regression.

```python
# Fit Kernel Ridge Regression model
alpha = 1.0  # Regularization parameter
gamma = 0.1  # Kernel coefficient for RBF kernel
krr = KernelRidge(alpha=alpha, kernel='rbf', gamma=gamma)
krr.fit(X, y)
```
