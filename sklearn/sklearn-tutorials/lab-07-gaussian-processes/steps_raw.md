# Gaussian Processes

## Introduction

In this lab, we will explore Gaussian Processes (GP), a supervised learning method used for regression and probabilistic classification problems. Gaussian Processes are versatile and can interpolate observations, provide probabilistic predictions, and handle different types of kernels. In this lab, we will focus on Gaussian Process Regression (GPR) and Gaussian Process Classification (GPC) using the scikit-learn library.

## Steps

### Step 1: Gaussian Process Regression (GPR)

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

### Step 2: GPR Examples

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

### Step 3: Gaussian Process Classification (GPC)

GaussianProcessClassifier class implements GPC for probabilistic classification. It places a GP prior on a latent function, which is then squashed through a link function to obtain the class probabilities. GPC supports multi-class classification by performing either one-versus-rest or one-versus-one based training and prediction.

```python
from sklearn.gaussian_process import GaussianProcessClassifier

# Create a GPC model with an RBF kernel
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict using the trained model
y_pred = model.predict(X_test)
```

### Step 4: GPC Examples

Probabilistic predictions with GPC: This example illustrates the predicted probability of GPC with different choices of hyperparameters.

```python
# Create a GPC model with an RBF kernel
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict the class probabilities of the test data
y_prob = model.predict_proba(X_test)
```

Illustration of GPC on the XOR dataset: This example demonstrates the use of GPC on the XOR dataset. We compare the results of using a stationary, isotropic kernel (RBF) and a non-stationary kernel (DotProduct).

```python
# Create GPC models with different kernels
isotropic_kernel = RBF(length_scale=1.0)
non_stationary_kernel = DotProduct(sigma_0=1.0)

# Fit the models to the XOR dataset
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
non_stationary_model = GaussianProcessClassifier(kernel=non_stationary_kernel)
isotropic_model.fit(X_xor, y_xor)
non_stationary_model.fit(X_xor, y_xor)

# Predict using the trained models
isotropic_y_pred = isotropic_model.predict(X_test)
non_stationary_y_pred = non_stationary_model.predict(X_test)
```

GPC on the iris dataset: This example illustrates GPC on the iris dataset using an isotropic RBF kernel and an anisotropic RBF kernel. It shows how different choices of hyperparameters can affect the predicted probability.

```python
# Create GPC models with different kernels and fit them to the iris dataset
isotropic_kernel = RBF(length_scale=1.0)
anisotropic_kernel = RBF(length_scale=[1.0, 2.0])
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
anisotropic_model = GaussianProcessClassifier(kernel=anisotropic_kernel)
isotropic_model.fit(X_train, y_train)
anisotropic_model.fit(X_train, y_train)

# Predict the class probabilities
isotropic_y_prob = isotropic_model.predict_proba(X_test)
anisotropic_y_prob = anisotropic_model.predict_proba(X_test)
```

## Summary

In this lab, we explored Gaussian Processes (GP) and their applications for regression and classification tasks. We learned how to use the GaussianProcessRegressor and GaussianProcessClassifier classes from scikit-learn, and how to specify different types of kernels for GPs. We also saw examples of GPR for regression tasks and GPC for multi-class classification tasks, demonstrating the versatility and capabilities of Gaussian Processes.
