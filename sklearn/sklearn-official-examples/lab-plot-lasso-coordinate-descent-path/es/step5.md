# Calcular la trayectoria de regularización usando Elastic Net positivo

En este paso, calcularemos la trayectoria de regularización usando la técnica de Elastic Net positivo y mostraremos los resultados usando matplotlib.

```python
# Calcular la trayectoria de regularización usando Elastic Net positivo
alphas_positive_enet, coefs_positive_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8, positive=True)

# Mostrar los resultados usando matplotlib
plt.figure(4)
neg_log_alphas_positive_enet = -np.log10(alphas_positive_enet)
for coef_e, coef_pe, c in zip(coefs_enet, coefs_positive_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)
    l2 = plt.plot(neg_log_alphas_positive_enet, coef_pe, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Elastic Net y Elastic Net positivo")
plt.legend((l1[-1], l2[-1]), ("Elastic Net", "Elastic Net positivo"), loc="lower left")
plt.axis("tight")
plt.show()
```
