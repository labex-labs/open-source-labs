# Ajustar o Modelo de Regressão Kernel Ridge

Agora, vamos ajustar um modelo de Regressão Kernel Ridge aos dados. Usaremos o kernel RBF (Radial Basis Function), comumente utilizado para regressão não linear.

```python
# Ajustar o modelo de Regressão Kernel Ridge
alpha = 1.0  # Parâmetro de regularização
gamma = 0.1  # Coeficiente do kernel para o kernel RBF
krr = KernelRidge(alpha=alpha, kernel='rbf', gamma=gamma)
krr.fit(X, y)
```
