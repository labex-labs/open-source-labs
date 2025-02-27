# Calculer le chemin de régularisation à l'aide de l'Elastic Net

Dans cette étape, nous allons calculer le chemin de régularisation à l'aide de la technique Elastic Net et afficher les résultats à l'aide de matplotlib.

```python
from sklearn.linear_model import enet_path

# Calculer le chemin de régularisation à l'aide de l'Elastic Net
alphas_enet, coefs_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8)

# Afficher les résultats à l'aide de matplotlib
plt.figure(3)
neg_log_alphas_enet = -np.log10(alphas_enet)
for coef_e, c in zip(coefs_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Chemin de l'Elastic Net")
plt.axis("tight")
plt.show()
```
