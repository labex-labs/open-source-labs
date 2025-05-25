# Visualização de Dados

Nesta etapa, visualizaremos as previsões feitas pelo regressor de processo gaussiano.

```python
plt.plot(X, y, label="Sinal esperado")
plt.scatter(x=X_train[:, 0], y=y_train, color="black", alpha=0.4, label="Observações")
plt.errorbar(X, y_mean, y_std)
plt.legend()
plt.xlabel("X")
plt.ylabel("y")
_ = plt.title(
    (
        f"Inicial: {kernel}\nÓptimo: {gpr.kernel_}\nLog-Verossimilhança-Marginal: "
        f"{gpr.log_marginal_likelihood(gpr.kernel_.theta)}"
    ),
    fontsize=8,
)
```
