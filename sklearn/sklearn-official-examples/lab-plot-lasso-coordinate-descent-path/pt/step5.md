# Calcular o Caminho de Regularização Usando Rede Elástica Positiva

Neste passo, calcularemos o caminho de regularização usando a técnica Rede Elástica Positiva e exibiremos os resultados usando matplotlib.

```python
# Calcular o caminho de regularização usando a Rede Elástica Positiva
alphas_positive_enet, coefs_positive_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8, positive=True)

# Exibir os resultados usando matplotlib
plt.figure(4)
neg_log_alphas_positive_enet = -np.log10(alphas_positive_enet)
for coef_e, coef_pe, c in zip(coefs_enet, coefs_positive_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)
    l2 = plt.plot(neg_log_alphas_positive_enet, coef_pe, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coeficientes")
plt.title("Rede Elástica e Rede Elástica Positiva")
plt.legend((l1[-1], l2[-1]), ("Rede Elástica", "Rede Elástica Positiva"), loc="lower left")
plt.axis("tight")
plt.show()
```
