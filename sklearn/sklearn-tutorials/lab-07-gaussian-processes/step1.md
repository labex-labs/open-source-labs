# Gaussian Process Regression (GPR)

GaussianProcessRegressor class implements Gaussian processes for regression tasks. It requires specifying a prior for the GP, such as the mean and covariance functions. The hyperparameters of the kernel are optimized during the fitting process. Let's see an example of using GPR for regression.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# Create a GPR model with an RBF kernel
kernel = RBF()
model = GaussianProcessRegressor(kernel=kernel)

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict using the trained model
y_pred = model.predict(X_test)
```
