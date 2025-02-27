# Ajuster le modèle de régression ridge noyau

Maintenant, ajustons un modèle de régression ridge noyau aux données. Nous utiliserons le noyau RBF (Radial Basis Function), qui est couramment utilisé pour la régression non linéaire.

```python
# Fit Kernel Ridge Regression model
alpha = 1.0  # Paramètre de régularisation
gamma = 0.1  # Coefficient du noyau pour le noyau RBF
krr = KernelRidge(alpha=alpha, kernel='rbf', gamma=gamma)
krr.fit(X, y)
```
