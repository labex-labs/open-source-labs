# Berechne den Regularisierungspfad mit positivem Lasso

In diesem Schritt berechnen wir den Regularisierungspfad mit der positiven Lasso-Technik und visualisieren die Ergebnisse mit matplotlib.

```python
# Berechne den Regularisierungspfad mit positivem Lasso
alphas_positive_lasso, coefs_positive_lasso, _ = lasso_path(X, y, eps=eps, positive=True)

# Zeige die Ergebnisse mit matplotlib an
plt.figure(2)
neg_log_alphas_positive_lasso = -np.log10(alphas_positive_lasso)
for coef_l, coef_pl, c in zip(coefs_lasso, coefs_positive_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)
    l2 = plt.plot(neg_log_alphas_positive_lasso, coef_pl, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("Koeffizienten")
plt.title("Lasso und positives Lasso")
plt.legend((l1[-1], l2[-1]), ("Lasso", "Positives Lasso"), loc="lower left")
plt.axis("tight")
plt.show()
```
