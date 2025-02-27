# Berechne den Regularisierungspfad mit positivem Elastic Net

In diesem Schritt berechnen wir den Regularisierungspfad mit der positiven Elastic Net-Technik und visualisieren die Ergebnisse mit matplotlib.

```python
# Berechne den Regularisierungspfad mit positivem Elastic Net
alphas_positive_enet, coefs_positive_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8, positive=True)

# Zeige die Ergebnisse mit matplotlib an
plt.figure(4)
neg_log_alphas_positive_enet = -np.log10(alphas_positive_enet)
for coef_e, coef_pe, c in zip(coefs_enet, coefs_positive_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)
    l2 = plt.plot(neg_log_alphas_positive_enet, coef_pe, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("Koeffizienten")
plt.title("Elastic Net und positives Elastic Net")
plt.legend((l1[-1], l2[-1]), ("Elastic Net", "Positives Elastic Net"), loc="lower left")
plt.axis("tight")
plt.show()
```
