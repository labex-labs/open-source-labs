# Definiere das Ziel

Zwecks dieses Beispiels definieren wir das Ziel `y` so, dass es stark mit einer Richtung korreliert, die eine geringe Varianz aufweist. Wir projizieren `X` auf die zweite Komponente und fügen ein wenig Rauschen hinzu.

```python
y = X.dot(pca.components_[1]) + rng.normal(size=n_samples) / 2

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

axes[0].scatter(X.dot(pca.components_[0]), y, alpha=0.3)
axes[0].set(xlabel="Projizierte Daten auf die erste PCA-Komponente", ylabel="y")
axes[1].scatter(X.dot(pca.components_[1]), y, alpha=0.3)
axes[1].set(xlabel="Projizierte Daten auf die zweite PCA-Komponente", ylabel="y")
plt.tight_layout()
plt.show()
```
