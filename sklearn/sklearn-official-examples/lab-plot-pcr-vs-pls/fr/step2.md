# Définir la cible

Dans le cadre de cet exemple, nous définissons la cible `y` de sorte qu'elle soit fortement corrélée avec une direction ayant une faible variance. Nous projetons `X` sur la deuxième composante et ajoutons du bruit à celle-ci.

```python
y = X.dot(pca.components_[1]) + rng.normal(size=n_samples) / 2

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

axes[0].scatter(X.dot(pca.components_[0]), y, alpha=0.3)
axes[0].set(xlabel="Données projetées sur la première composante PCA", ylabel="y")
axes[1].scatter(X.dot(pca.components_[1]), y, alpha=0.3)
axes[1].set(xlabel="Données projetées sur la deuxième composante PCA", ylabel="y")
plt.tight_layout()
plt.show()
```
