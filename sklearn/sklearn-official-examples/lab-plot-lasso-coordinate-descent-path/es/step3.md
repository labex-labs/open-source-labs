# Calcular la trayectoria de regularización usando Lasso positivo

En este paso, calcularemos la trayectoria de regularización usando la técnica de Lasso positivo y mostraremos los resultados usando matplotlib.

```python
# Calcular la trayectoria de regularización usando Lasso positivo
alphas_positive_lasso, coefs_positive_lasso, _ = lasso_path(X, y, eps=eps, positive=True)

# Mostrar los resultados usando matplotlib
plt.figure(2)
neg_log_alphas_positive_lasso = -np.log10(alphas_positive_lasso)
for coef_l, coef_pl, c in zip(coefs_lasso, coefs_positive_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)
    l2 = plt.plot(neg_log_alphas_positive_lasso, coef_pl, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Lasso y Lasso positivo")
plt.legend((l1[-1], l2[-1]), ("Lasso", "Lasso positivo"), loc="lower left")
plt.axis("tight")
plt.show()
```
