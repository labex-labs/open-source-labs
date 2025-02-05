# GPC Examples

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
