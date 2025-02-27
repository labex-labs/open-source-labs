# Berechne den Regularisierungspfad mit Elastic Net

In diesem Schritt berechnen wir den Regularisierungspfad mit der Elastic Net-Technik und visualisieren die Ergebnisse mit matplotlib.

```python
from sklearn.linear_model import enet_path

# Berechne den Regularisierungspfad mit Elastic Net
alphas_enet, coefs_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8)

# Zeige die Ergebnisse mit matplotlib an
plt.figure(3)
neg_log_alphas_enet = -np.log10(alphas_enet)
for coef_e, c in zip(coefs_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("Koeffizienten")
plt.title("Elastic Net-Pfad")
plt.axis("tight")
plt.show()
```
