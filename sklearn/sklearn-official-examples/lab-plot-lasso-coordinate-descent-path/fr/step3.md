# Calculer le chemin de régularisation à l'aide de la Lasso positive

Dans cette étape, nous allons calculer le chemin de régularisation à l'aide de la technique de Lasso positive et afficher les résultats à l'aide de matplotlib.

```python
# Calculer le chemin de régularisation à l'aide de la Lasso positive
alphas_positive_lasso, coefs_positive_lasso, _ = lasso_path(X, y, eps=eps, positive=True)

# Afficher les résultats à l'aide de matplotlib
plt.figure(2)
neg_log_alphas_positive_lasso = -np.log10(alphas_positive_lasso)
for coef_l, coef_pl, c in zip(coefs_lasso, coefs_positive_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)
    l2 = plt.plot(neg_log_alphas_positive_lasso, coef_pl, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Lasso et Lasso positive")
plt.legend((l1[-1], l2[-1]), ("Lasso", "Lasso positive"), loc="lower left")
plt.axis("tight")
plt.show()
```
