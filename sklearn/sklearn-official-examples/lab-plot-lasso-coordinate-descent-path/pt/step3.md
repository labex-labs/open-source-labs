# Calcular o Caminho de Regularização Usando Lasso Positivo

Neste passo, calcularemos o caminho de regularização usando a técnica Lasso positivo e exibiremos os resultados usando matplotlib.

```python
# Calcular o caminho de regularização usando o Lasso positivo
alphas_positive_lasso, coefs_positive_lasso, _ = lasso_path(X, y, eps=eps, positive=True)

# Exibir os resultados usando matplotlib
plt.figure(2)
neg_log_alphas_positive_lasso = -np.log10(alphas_positive_lasso)
for coef_l, coef_pl, c in zip(coefs_lasso, coefs_positive_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)
    l2 = plt.plot(neg_log_alphas_positive_lasso, coef_pl, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coeficientes")
plt.title("Lasso e Lasso Positivo")
plt.legend((l1[-1], l2[-1]), ("Lasso", "Lasso Positivo"), loc="lower left")
plt.axis("tight")
plt.show()
```
