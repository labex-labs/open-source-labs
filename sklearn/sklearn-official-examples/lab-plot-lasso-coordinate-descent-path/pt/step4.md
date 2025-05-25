# Calcular o Caminho de Regularização Usando Rede Elástica

Neste passo, calcularemos o caminho de regularização usando a técnica Rede Elástica e exibiremos os resultados usando matplotlib.

```python
from sklearn.linear_model import enet_path

# Calcular o caminho de regularização usando a Rede Elástica
alphas_enet, coefs_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8)

# Exibir os resultados usando matplotlib
plt.figure(3)
neg_log_alphas_enet = -np.log10(alphas_enet)
for coef_e, c in zip(coefs_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coeficientes")
plt.title("Caminho da Rede Elástica")
plt.axis("tight")
plt.show()
```
