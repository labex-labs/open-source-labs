# Visualización de datos

En este paso, visualizaremos las predicciones hechas por el regresor de procesos gaussianos.

```python
plt.plot(X, y, label="Señal esperada")
plt.scatter(x=X_train[:, 0], y=y_train, color="black", alpha=0.4, label="Observaciones")
plt.errorbar(X, y_mean, y_std)
plt.legend()
plt.xlabel("X")
plt.ylabel("y")
_ = plt.title(
    (
        f"Initial: {kernel}\nOptimum: {gpr.kernel_}\nLog-Marginal-Likelihood: "
        f"{gpr.log_marginal_likelihood(gpr.kernel_.theta)}"
    ),
    fontsize=8,
)
```
