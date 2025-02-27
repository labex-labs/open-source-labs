# Ajustar el modelo de regresión Kernel Ridge

Ahora, ajustemos un modelo de regresión Kernel Ridge a los datos. Usaremos el kernel RBF (Función Base Radial), que se utiliza comúnmente para la regresión no lineal.

```python
# Fit Kernel Ridge Regression model
alpha = 1.0  # Regularization parameter
gamma = 0.1  # Kernel coefficient for RBF kernel
krr = KernelRidge(alpha=alpha, kernel='rbf', gamma=gamma)
krr.fit(X, y)
```
