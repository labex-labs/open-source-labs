# GPR Examples

GPR with noise-level estimation: This example illustrates GPR with a sum-kernel including a WhiteKernel for estimating the noise level of the data.

```python
from sklearn.gaussian_process.kernels import WhiteKernel

# Create a GPR model with an RBF kernel and a WhiteKernel
kernel = RBF() + WhiteKernel()
model = GaussianProcessRegressor(kernel=kernel)

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict using the trained model
y_pred = model.predict(X_test)
```

Comparison of GPR and Kernel Ridge Regression: Both kernel ridge regression (KRR) and GPR learn a target function using the "kernel trick". GPR learns a generative, probabilistic model and can provide confidence intervals, while KRR only provides predictions.

```python
from sklearn.kernel_ridge import KernelRidge

# Create a Kernel Ridge Regression model
krr_model = KernelRidge(kernel='rbf')

# Fit the KRR model to the training data
krr_model.fit(X_train, y_train)

# Predict using the KRR model
krr_y_pred = krr_model.predict(X_test)

# Compare the results with GPR
gpr_model = GaussianProcessRegressor(kernel=RBF())
gpr_model.fit(X_train, y_train)
gpr_y_pred = gpr_model.predict(X_test)
```

GPR on Mauna Loa CO2 data: This example demonstrates complex kernel engineering and hyperparameter optimization using gradient ascent on the log-marginal-likelihood. The data consists of monthly average atmospheric CO2 concentrations collected at the Mauna Loa Observatory in Hawaii. The objective is to model the CO2 concentration as a function of time.

```python
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, RationalQuadratic, WhiteKernel

# Create a GPR model with a composed kernel
kernel = 34.4**2 * RBF(length_scale=41.8) + 3.27**2 * RBF(length_scale=180) * ExpSineSquared(length_scale=1.44, periodicity=1) + 0.446**2 * RationalQuadratic(alpha=17.7, length_scale=0.957) + 0.197**2 * RBF(length_scale=0.138) + WhiteKernel(noise_level=0.0336)
model = GaussianProcessRegressor(kernel=kernel)

# Fit the model to the data
model.fit(X_train, y_train)

# Predict using the trained model
y_pred = model.predict(X_test)
```
