# Kernel Ridge Regression-Modell anpassen

Jetzt passen wir ein Kernel Ridge Regression-Modell an die Daten an. Wir werden den RBF (Radial Basis Function)-Kernel verwenden, der für die nicht-lineare Regression häufig eingesetzt wird.

```python
# Fit Kernel Ridge Regression model
alpha = 1.0  # Regularization parameter
gamma = 0.1  # Kernel coefficient for RBF kernel
krr = KernelRidge(alpha=alpha, kernel='rbf', gamma=gamma)
krr.fit(X, y)
```
