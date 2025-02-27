# Calculer le chemin de régularisation à l'aide de l'Elastic Net positif

Dans cette étape, nous allons calculer le chemin de régularisation à l'aide de la technique d'Elastic Net positif et afficher les résultats à l'aide de matplotlib.

```python
# Calculer le chemin de régularisation à l'aide de l'Elastic Net positif
alphas_positive_enet, coefs_positive_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8, positive=True)

# Afficher les résultats à l'aide de matplotlib
plt.figure(4)
neg_log_alphas_positive_enet = -np.log10(alphas_positive_enet)
for coef_e, coef_pe, c in zip(coefs_enet, coefs_positive_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)
    l2 = plt.plot(neg_log_alphas_positive_enet, coef_pe, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Elastic Net et Elastic Net positif")
plt.legend((l1[-1], l2[-1]), ("Elastic Net", "Elastic Net positif"), loc="lower left")
plt.axis("tight")
plt.show()
```
